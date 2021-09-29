import os
from pytube import YouTube
from logger import Logger


class Downloader:
    def __init__(self, logger: Logger):
        self.logger = logger

    def download(self, urls: list[str], out_dir=None):
        for url in urls:
            out_dir = out_dir if out_dir is not None else './'

            self.logger.log(f'Starting on video at {url}...')
            yt = YouTube(url)

            self.logger.log(f'Found video "{yt.title}". Getting MP4 stream...')
            all_streams = yt.streams.filter(mime_type='audio/mp4')
            stream = self._find_highest_bitrate(all_streams)
            self.logger.log(f'Found stream, size is {stream.filesize_approx}, bitrate {stream.abr}')
            file_name = stream.default_filename

            stream.download(out_dir)
            self.logger.log(f'Downloaded to {os.path.join(out_dir, file_name)}')

    def _find_highest_bitrate(self, streams):
        stream_brs = [{'id': s.itag, 'bitrate': int(s.abr.replace('kbps', '')), 'stream': s} for s in streams]
        sort = sorted(stream_brs, key=lambda x: x['bitrate'], reverse=True)
        stream = sort[0]['stream']

        return stream
