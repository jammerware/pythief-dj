import argparse
from parsed_args import ParsedArgs


class ArgsParser:
    def parse(self, raw_args) -> ParsedArgs:
        parser = argparse.ArgumentParser(
            description='Download one or more YouTube audio files by url or video ID (the part that comes after "v=" in the url)', exit_on_error=False)

        parser.add_argument(
            '--out-dir', '-o', help="The directory into which you want to save the files downloaded", default='./')
        parser.add_argument(
            '--videos', help="The IDs or URLs of the video(s) you want to download (required)", nargs='+')

        return parser.parse_args(raw_args)
