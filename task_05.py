#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is for a function called defaults."""


def defaults(my_required, my_optional=True):
    """This function makes a logical comparison between two variables.

    Args:
        my_optional(boolean): An optional boolean parameter. Default: True
        my_required(boolean): A required boolean parameter.
        
    Returns:
        boolean: Returns a logical comparison of two parameters.

    Examples:

        >>> defaults(True, False)
        False

    """    
    return my_optional is my_required
