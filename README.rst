=======
Read me
=======

Tedmund is a terminal-based slide presentation system.

You build slides with it, then run it as a Python script to do your
presentation. It comes with some formatting helpers to make slides
come out decent.


Quick start
===========

Install::

    $ pip install tedmund

Write slides::

    $ vim mypresentation.py

    from temund import run_slides

    slides = [

    ]

    run_slides(slides)
    
Present::

    $ python mypresentation.py


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
