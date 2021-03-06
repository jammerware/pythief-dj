# Pythief DJ

[![PyPI version](https://badge.fury.io/py/pythief-dj.svg)](https://badge.fury.io/py/pythief-dj)

A semi-simple tool for... "borrowing"... audio from YouTube videos.

## Here's why I do this

It's common DJ etiquette (or really just like, person-etiquette) to **purchase songs that you use for your craft**. I wholeheartedly endorse this ideal and do it myself. However, I'm also a bedroom DJ who mixes a lot of stuff that people never hear, and very often, I want to try mixing a song before I use it in one of my [patented adorable newbie videos](https://www.youtube.com/watch?v=4VfiK_wxq3Y). YouTube is a great source for use cases like this, despite the moral dubiousness of yoinking audio from it. 

However, I also found YouTube ripping a very tedious process. You search, find your video, go to one of a million "YouTube to Mp3 FAST!" sites, click multiple times, download, save, and so on, so I wrote this tool to automate some of it. I don't have the search thing figured out yet (it can be tricky to identify the right video for a song - for example, some music videos edit the original audio for dramatic effect), but right now, you can use this to download audio from multiple YouTube videos by URL, which is a step up for _my_ workflow, anyway.

## Getting started

1. Install [Python 3.9+](https://www.python.org/downloads/)
2. Install [FFmpeg](https://www.ffmpeg.org/) and make sure it's in your system path by opening a command line/terminal and typing "ffmpeg"
3. Install this tool by opening a command prompt/terminal and typing `pip install pythief-dj`.
4. Download your first video by running `pythief-dj [VIDEO URL]` (replace `[VIDEO URL]` with the URL of the YouTube video of your choice.)

## Note

Pythief DJ automatically tries to download the highest-quality audio stream available, but most videos encode audio at a maximum of 128kbps. This is obviously far short of the 320kbps minimum that we shoot for as DJs, but it's sufficient for trying a song out at home. Want better quality? **Buy the song** on a service like iTunes, Amazon Music, Beatport, etc.

## Advanced tricks for turbocharged music borrowing

As a general note, you can type `pythief-dj` without any arguments to see options you can supply to Pythief DJ that change its behavior. It looks like this right now:

```
Usage: pythief-dj [OPTIONS] [VIDEOS]...

Download audio for the videos specified in VIDEOS, in --txt, or both.

Options:
  -d, --dry-run / --do-it-live  If enabled, dry run treats your input as
                                search terms rather than specific videos and
                                opens a browser tab for each term on YouTube.
                                It doesn't download anything.
  -k, --keep-raw BOOLEAN        Keep the raw MP4 files downloaded from YouTube
                                that this tool converts to MP3 for use (false
                                by default).
  -f, --format TEXT             The format into which you wish to convert the
                                audio data from the video (mp3 by default).
  -o, --out-dir DIRECTORY       The directory into which you want to save the
                                files downloaded
  -t, --txt PATH                Path to a text file containing the videos to
                                download. One per line.
  --help                        Show this message and exit.
```

Also...

### Specifying videos
- Video URLs can be specified either with a complete URL (e.g. [https://www.youtube.com/watch?v=F7cihvwCXes](https://www.youtube.com/watch?v=F7cihvwCXes)) OR with the YouTube video ID, which is the part of the URL after "v" (e.g. `F7cihvwCXes`.)
- You can download multiple songs at a time by adding a space between each URL, e.g. `pythief-dj [VIDEO 1] [VIDEO 2]` (etc.)
- You can also create a text file of video URLs to make entry easier. Just place each URL or video ID on one line. 
  - This is pretty brittle - if you enter anything but the URL on the line, stuff will probably break. Sorry.
  - This doesn't actually have to be a `.txt` file - anything text-encoded will do.
  - This method can be combined with URLs supplied as arguments to Pythief DJ. So if you have a text file with a few videos and a URL of another you want to add, you can enter `pythief-dj --txt myfile.txt https://youtube.com/watch?v=somevideoid` to download all of them at once.

### Output

- By default, Pythief DJ spits everything into a folder called `pythief-dj-output` in the same folder you ran the command. You can control this using the `--out-dir` argument.
- The audio downloaded from YouTube come down as MP4 audio, which is massive and doesn't have dramatically better quality than MP3. Pythief DJ stores these in an intermediate directory in the output directory and then throws them away when it's done. If you want to keep them, just specify `--keep-raw`.

## Things I'll add eventually

I'm a grad student, so my disposable time is not in high quantities. On the other hand, you never know when I'll want to avoid work. Look for these to come eventually, and if you have ideas, [open an issue](https://github.com/jammerware/pythief-dj/issues/new).

- **Configurable verbosity:** Right now, it just kind of burbles at random times as it does its thing, but I'll eventually add levels of verbosity you can ask for as you run the command.
- **Entry of videos by CSV:** The use case I'm thinking of here is that you might want to pre-specify the artist/title in advance, along additional ID3 tags like genre. 
- **Magical automatic YouTube search**: I'm currently tussling with YouTube's OAuth API, but when I'm done, I can at least try to find a song's video if you don't have the URL.

## Acknowledgments

You can see `requirements.txt` for all of my dependencies, but I'm relying heavily on `pytube`, `pydub`, and FFMpeg, all of which are doing an incredible amount of heavy lifting in this script. Thanks to those projects.