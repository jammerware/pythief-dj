import os
import re
from pathlib import Path
from pydub import AudioSegment
from context.py_thief_args import PyThiefArgs
from context.py_thief_context import PyThiefContext
from download.downloaded_song import DownloadedSong


class Mp3ifier:
    def __init__(self, ctx: PyThiefContext):
        self._ctx = ctx
        self._title_regex = re.compile(r'\s*([\S ]+\S)\s*\-\s*(\S[\S ]+\S)')
        self._safe_file_regex = re.compile(r'[<>:"/\\|\?\*]')

    def mp3ify(self, songs: list[DownloadedSong]):
        out_dir = Path(self._ctx.args.out_dir)

        if not out_dir.is_dir():
            out_dir.mkdir(parents=True)

        for song in songs:
            self._ctx.talkback.say(f'Converting song at "{song.path}"...')
            audio = AudioSegment.from_file(song.path)

            # try to find the artist/song title from the video title
            artist = None
            title = None
            match = self._title_regex.search(song.title)
            if match is not None:
                artist = match.group(1)
                title = match.group(2)

            # export with a (hopefully) better file name and ID3 tags set
            file_name = f'{song.title}.mp3'
            tags = None

            if artist is not None and title is not None:
                file_name = f'{artist} - {title}.mp3'
                tags = {'artist': artist, 'title': title}

            # make file name OS safe
            file_name = self._safe_file_regex.sub('', file_name)
            self._ctx.talkback.say(f'Resolved file name as "{file_name}"...')

            # save as mp3
            audio.export(out_dir.joinpath(Path(file_name)), format='mp3', tags=tags)
            self._ctx.talkback.say(f'Saved.')
