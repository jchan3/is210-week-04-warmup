#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is for the function too_many_kittens."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function determines if there are too many kittens without a
        litterbox and catfood for each kitten.

    Args:
        kittenswink(int): Number of kittens.
        litterboxesnumwink(int): Number of available litterboxes
        catfood(boolean): Represents whether or not any catfood exists.

    Returns:
        boolean: Represents if there is at least one litterbox and some catfood
        for each kitten.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

    """
    return not (litterboxes >= kittens and catfood)
