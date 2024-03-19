""" Program to test if an integer is a perfect square.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
import math
######################################################################
def isperfectsquare(nnn):
    """ Test for perfectsquare-ness.  Take the square root, convert
        to an 'int', and square that value.
        Parameters:
            nnn: the integer to test
        Returns:
            'True' or 'False'
    """
    nroot = math.sqrt(nnn)
    nroot = int(nroot + 0.5)
    nrootsquared = nroot * nroot
    return nrootsquared == nnn
