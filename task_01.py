#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Adds winks and nudges to end of statement and removes whitespaces.

    Args:
        wink(mixed): First element at the end of Know what I mean.
        numwink(int, optional): Number of times to repeat wink. Default: Two

    Returns:
        str: Statement with winks and nudges repeated at the end.

    Examples:

        >>> know_what_i_mean(';)')
        'Know what I mean? ;);)nudge nudge'

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
