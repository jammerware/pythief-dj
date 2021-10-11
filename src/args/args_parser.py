import os
import argparse
from args.parsed_args import ParsedArgs


class ArgsParser:
    def parse(self, raw_args) -> ParsedArgs:
        parser = argparse.ArgumentParser(
            description='Download one or more YouTube audio files by url or video ID (the part that comes after "v=" in the url)', exit_on_error=False)

        parser.add_argument(
            '--out-dir', help="The directory into which you want to save the files downloaded", default=os.path.join(os.getcwd(), 'pythief-dj-output'))
        parser.add_argument('--text', help="A text file with video IDs or URLs. One per line.")
        parser.add_argument(
            '--videos', help="The IDs or URLs of the video(s) you want to download (required)", nargs='*')
        parser.add_argument(
            '--format', help="The format into which you wish to convert the audio data from the video (mp3 by default).", default='mp3')
        parser.add_argument(
            '--keep-mp4s', help="Keep the raw MP4 files downloaded from YouTube that this tool converts to MP3 for use (false by default).", default=False
        )

        # I tried stupidly hard to make a typed parse happen here, but argparse is kind of being a jagoff
        # return parser.parse_args(raw_args, namespace=ParsedArgs())
        return ParsedArgs(vars(parser.parse_args(raw_args)))
