from os.path import exists
import re
from args.parsed_args import ParsedArgs


class UrlResolverService:
    def __init__(self):
        self.url_regex = re.compile(r'[s\S]*?youtube\.com/watch\?v=([a-zA-Z0-9_]+)')
        self.id_regex = re.compile(r'[a-zA-Z0-9_]+')

    def _get_url(self, video_id: str) -> str:
        url_match = self.url_regex.search(video_id)
        final_id = None

        if url_match is not None:
            final_id = url_match.groups(1)

        id_match = self.id_regex.search(video_id)
        if id_match is not None:
            final_id = video_id

        if final_id is not None:
            return f'https://youtube.com/watch?v={final_id}'

        raise ValueError(
            f'video_id ("{video_id}") was neither a valid YouTube video link nor a video id (the part that goes after "v" in the address of the video.')

    def _resolve_from_args(self, video_ids) -> list[str]:
        return [self._get_url(id) for id in video_ids]

    def _resolve_from_text_file(self, path: str):
        if not exists(path):
            raise ValueError(f"Text file path {path} doesn't exist.")

        lines: list[str] = []

        with open(path, 'r') as f:
            lines = list(filter(lambda x: x != '', [line.strip() for line in f.readlines()]))

        if len(lines) == 0:
            raise ValueError(f"Text file at path {path} seems empty?")

        return self._resolve_from_args(lines)

    def resolve(self, args: ParsedArgs):
        # read videos passed manually
        video_urls: list[str] = []
        if args.videos is not None:
            video_urls += self._resolve_from_args(args.videos)

        # read videos passed in the text file
        if args.text is not None and args.text != '':
            video_urls += self._resolve_from_text_file(args.text)

        return video_urls
