=======
Read me
=======

Tedmund is a really really basic terminal-based slide presentation
system.

You build slides with it, then run it as a Python script to do your
presentation. It comes with some formatting helpers to make slides
come out decent.


Quick start
===========

**Install**

    ::

        $ pip install tedmund

**Write slides**

    ::

        $ vim mypresentation.py

        from temund import *


        title("""
        Welcome to my slides
        """)


        info("""
        My slides come in three varieties:

        * title
        * info
        * code
        """)


        info("""
        Now for an example.
        """)


        code("""
        from tedmund import *

        title('''
        Title slide!
        ''')
        info('''
        This is an info slide with bullets!

        * bullet 1
        * bullet 2
        ''')
        code('''
        from tedmund import *
        ...
        ''')
        """)


    run_slides()

**Present**

    ::

        $ python mypresentation.py

    Use:

    * 'a' for previous slide,
    * 'd' for next slide,
    * and 'q' for quit.

    Why those keys? Because I do a lot of WASD games.


Project details
===============

:Code:          http://github.com/willkg/tedmund
:Issue tracker: https://github.com/willkg/tedmund/issues
:License:       BSD 3-clause; see LICENSE file


Why is it called Tedmund?
=========================

This is how I name my software projects.


Status
======

July 19th, 2013

Initial writing for a beer-and-tell.
