#!/usr/bin/env python
""" Program to find a primitive root for a prime.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
import sys
def primroot(theprime):
    """ Primitive root computation, done very naively.
        Parameters:
            theprime: the prime for which to find a prim root
        Returns:
            the primitive root, or dies with an error message
    """

    for theroot in range(2, theprime):
        exponent = 1
        product = theroot
        while product != 1:
            product = (product*theroot) % theprime
            exponent += 1
            if exponent > theprime-1:
                sss = f'ERROR FOR INPUT {theprime}'
                print(sss)
                sys.exit()

        if exponent == theprime-1:
            return theroot
