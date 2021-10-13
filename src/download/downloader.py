import os
import pathlib
from context.py_thief_context import PyThiefContext
from pytube import YouTube
from services.logger import Logger
from download.downloaded_song import DownloadedSong


class Downloader:
    def __init__(self, logger: Logger):
        self.logger = logger

    def download(self, urls: list[str], context: PyThiefContext):
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

            stream.download(context.storage.raw_root)
            path = os.path.join(context.storage.raw_root, file_name)
            self.logger.log(f'Downloaded to {path}.')

            downloaded.append(DownloadedSong(yt.title, url, path))

        return downloaded

    def _find_highest_bitrate(self, streams):
        stream_brs = [{'id': s.itag, 'bitrate': int(s.abr.replace('kbps', '')), 'stream': s} for s in streams]
        sort = sorted(stream_brs, key=lambda x: x['bitrate'], reverse=True)
        stream = sort[0]['stream']

        return stream
