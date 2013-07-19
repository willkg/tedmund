import sys
import tty
import termios

from blessings import Terminal

from tedmund._version import __version__, __releasedate__


__all__ = ['title', 'info', 'code', 'run_slides', '__version__', '__releasedate__']


TERM = Terminal()
SLIDES = []


class Title(object):
    def __init__(self, text):
        self.text = text.strip()

    def display(self):
        # Title slides get centered vertically and horizontally
        # line-by-line.

        # Clear screen
        print TERM.clear()

        textlines = self.text.splitlines()
        y = (TERM.height - len(textlines)) / 2

        for i, line in enumerate(textlines):
            textlines[i] = (
                (' ' * ((TERM.width - len(line)) / 2)) +
                TERM.bold + line + TERM.normal)

        # Paint slide
        with TERM.location(0, y):
            for line in textlines:
                print line


class Info(object):
    def __init__(self, text):
        self.text = text.strip()

    def display(self):
        # Slides start 3 lines down and 5 characters in.

        # Clear screen
        print TERM.clear()

        textlines = self.text.splitlines()
        y = 3

        for i, line in enumerate(textlines):
            if line.startswith('* '):
                line = TERM.blue + '* ' + TERM.normal + line[2:]

            textlines[i] = (' ' * 5) + line

        # Paint slide
        with TERM.location(0, y):
            for line in textlines:
                print line


class Code(object):
    def __init__(self, text):
        self.text = text.strip()

    def display(self):
        # Slides start 3 lines down and 5 characters in.

        # Clear screen
        print TERM.clear()

        textlines = self.text.splitlines()
        y = 3

        for i, line in enumerate(textlines):
            textlines[i] = (' ' * 5) + line

        # Paint slide
        with TERM.location(0, y):
            for line in textlines:
                print line


def add_slide(slide):
    print 'Adding slide {0}'.format(len(SLIDES))
    SLIDES.append(slide)


def title(text):
    add_slide(Title(text))


def info(text):
    add_slide(Info(text))


def code(text):
    add_slide(Code(text))


def getch():
    """Get a single character"""
    # Based on http://code.activestate.com/recipes/134892/
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_slide_number(pageno, total):
    with TERM.location(0, TERM.height - 1):
        if pageno == 0:
            print '     BEGINNING'
        elif pageno + 1 == total:
            print '     THE END'
        else:
            print '     {0:2} / {1:2}'.format(pageno + 1, total)


def run_slides():
    print TERM.enter_fullscreen()

    pageno = 0

    SLIDES[pageno].display()
    print_slide_number(pageno, len(SLIDES))

    while 0 <= pageno < len(SLIDES):
        SLIDES[pageno].display()
        print_slide_number(pageno, len(SLIDES))

        c = getch()
        if c == 'd':
            pageno += 1
        elif c == 'a':
            pageno -= 1
        elif c == 'q':
            break

    print TERM.clear()
    print TERM.exit_fullscreen()
