from enum import IntEnum
import click


class TalkbackVerbosity(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Talkback:
    def __init__(self, verbosity: TalkbackVerbosity = TalkbackVerbosity.HIGH):
        self._verbosity = verbosity

    def say(self, msg: str, verbosity_level: TalkbackVerbosity = TalkbackVerbosity.LOW):
        if verbosity_level <= self.verbosity:
            click.echo(msg)

    @property
    def verbosity(self): return self._verbosity
