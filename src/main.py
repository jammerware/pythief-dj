import os
import sys
from dotenv import load_dotenv
from args.args_parser import ArgsParser
from auth.auth_service import AuthService
from download.downloader import Downloader
from logger import Logger
from mp3ifier import Mp3ifier
from url_resolver_service import UrlResolverService

if __name__ == "__main__":
    # load env
    load_dotenv(os.path.join(os.getcwd(), './.secret/.env'))

    # services
    # auth_service = AuthService()
    # auth_service.start()

    argsParser = ArgsParser()
    args = argsParser.parse(sys.argv[1:])

    if not args.is_valid():
        print('Invalid args.')
        exit(1)

    load_dotenv()
    logger = Logger()
    downloader = Downloader(logger)

    # resolve video URLs from args passed
    resolver = UrlResolverService()
    video_urls = resolver.resolve(args)

    # get mp4s
    downloaded = downloader.download(video_urls, args.out_dir)

    # convert to the desired format
    Mp3ifier().mp3ify(downloaded, args)

    logger.log(f'All done! Downloaded {len(video_urls)} files {"" if len(video_urls) == 1 else "s"}.')
