import os
import pathlib
from pytube import YouTube
from logger import Logger
from download.downloaded_song import DownloadedSong


class Downloader:
    def __init__(self, logger: Logger):
        self.logger = logger

    def download(self, urls: list[str], out_dir):
        # ensure our outpath is ok
        raw_outpath = os.path.join(out_dir, "raw")
        pathlib.Path(raw_outpath).mkdir(parents=True, exist_ok=True)

        downloaded: list[DownloadedSong] = []

        for url in urls:
            self.logger.log(f'Starting on video at {url}...')
            yt = YouTube(url)

            self.logger.log(f'Found video "{yt.title}". Getting MP4 stream...')
            all_streams = yt.streams.filter(mime_type='audio/mp4')
            stream = self._find_highest_bitrate(all_streams)
            self.logger.log(
                f'Found stream. Bitrate is {stream.abr}, size is about {round(stream.filesize_approx / (10 ** 5), 2)}MB')
            file_name = stream.default_filename

            stream.download(raw_outpath)
            path = os.path.join(raw_outpath, file_name)
            self.logger.log(f'Downloaded to {os.path.join(raw_outpath, file_name)}')

            downloaded.append(DownloadedSong(yt.title, url, path))

        return downloaded

    def _find_highest_bitrate(self, streams):
        stream_brs = [{'id': s.itag, 'bitrate': int(s.abr.replace('kbps', '')), 'stream': s} for s in streams]
        sort = sorted(stream_brs, key=lambda x: x['bitrate'], reverse=True)
        stream = sort[0]['stream']

        return stream
