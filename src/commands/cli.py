import sys

import click
from commands.lookup import lookup
from context.py_thief_args import PyThiefArgs
from context.py_thief_context import PyThiefContext
from auth.auth_service import AuthService
from download.downloader import Downloader
from services.mp3ifier import Mp3ifier
from services.storage import Storage
from services.talkback import Talkback, TalkbackVerbosity
from services.url_resolver_service import UrlResolverService


@click.command()
@click.argument('videos', nargs=-1)
@click.option('-d', '--dry-run/--do-it-live', default=False, type=click.BOOL, help="If enabled, dry run treats your input as search terms rather than specific videos and opens a browser tab for each term on YouTube. It doesn't download anything.")
@click.option('-k', '--keep-raw', default=False, type=click.BOOL, help="Keep the raw MP4 files downloaded from YouTube that this tool converts to MP3 for use (false by default).")
@click.option('-f', '--format', default='mp3', help='The format into which you wish to convert the audio data from the video (mp3 by default).')
@click.option('-o', '--out-dir', default='pythief-dj-output', type=click.Path(file_okay=False, resolve_path=True), help="The directory into which you want to save the files downloaded")
@click.option('-t', '--txt', type=click.Path(exists=True, resolve_path=True), help="Path to a text file containing the videos to download. One per line.")
def cli(**kwargs):
    """Download audio for the videos specified in VIDEOS, in --txt, or both."""
    if len(sys.argv) < 2:
        _echo_command_help(cli)
        sys.exit()

    args = PyThiefArgs.from_kwargs(kwargs)
    if not args.is_valid:
        click.echo('Invalid args. Want some help?')
        _echo_command_help(cli)
        sys.exit(1)

    # services
    # auth_service = AuthService()
    # auth_service.start()

    # build the context
    talkback = Talkback(TalkbackVerbosity.HIGH)
    storage = Storage.from_out_root(args.out_dir)
    context = PyThiefContext(args, storage, talkback)

    if context.args.dry_run:
        lookup(context)
        exit()

    # resolve video URLs from args passed
    resolver = UrlResolverService()
    video_urls = resolver.resolve(context)

    # get mp4s
    downloader = Downloader(context)
    downloaded = downloader.download(video_urls)

    # convert to the desired format
    Mp3ifier(context).mp3ify(downloaded)

    # clean up raws if directed
    if not args.keep_raw:
        context.storage.delete_raw()

    context.talkback.say(f'All done! Downloaded {len(video_urls)} file{"" if len(video_urls) == 1 else "s"}.')


def _echo_command_help(command: click.Command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))
