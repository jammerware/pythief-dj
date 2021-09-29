import re


class UrlResolverService:
    def __init__(self):
        self.url_regex = re.compile(r'[s\S]*?youtube\.com/watch\?v=([a-zA-Z0-9_]+)')
        self.id_regex = re.compile(r'[a-zA-Z0-9_]+')

    def get_url(self, video_id):
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

    def get_urls(self, video_ids):
        return [self.get_url(id) for id in video_ids]
