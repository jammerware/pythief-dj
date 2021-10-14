from context.py_thief_context import PyThiefContext
import webbrowser


def lookup(ctx: PyThiefContext):
    for video in ctx.args.videos:
        ctx.talkback.say(f'Looking up "{video}"...')
        webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={video}')
