import sys
from args_parser import ArgsParser
from downloader import Downloader
from logger import Logger
from url_resolver_service import UrlResolverService

if __name__ == "__main__":
    argsParser = ArgsParser()
    args = argsParser.parse(sys.argv[1:])

    if args.videos is None or len(args.videos) == 0:
        exit()

    logger = Logger()
    downloader = Downloader(logger)
    resolver = UrlResolverService()

    video_urls = resolver.get_urls(args.videos)

    downloader.download(video_urls)
    logger.log(f'All done! Downloaded {len(video_urls)} files.')
