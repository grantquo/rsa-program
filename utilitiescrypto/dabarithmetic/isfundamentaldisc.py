""" Test for whether a discriminant is fundamental.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 20 October 2023
"""
import sys
import math

sys.path.append('/Users/buell/Current/Utilities/') # office directory

#pylint: disable=import-error
#pylint: disable=wrong-import-position
from DABArithmetic.dabarithmetic.mymod import mymod
#pylint: enable=import-error
#pylint: enable=wrong-import-position

######################################################################
def isfundamentaldisc(nnn):
    """ Test for whether a discriminant is fundamental.
        Parameters:
            nnn: the disc to test
        Returns:
            the 'True' or 'False' answer to the question

    """
    signum = 1
    if nnn < 0:
        signum = -1

    nroot = int(math.sqrt(signum*nnn) + 0.5)

    # Test to see if 'nnn' is a perfect square.
    if nroot*nroot == nnn*signum:
        return False

    discmod8 = mymod(nnn, 8)

    # Eliminate all 'nnn' but 0 or 1 mod 4
    if discmod8 == (2, 3, 6, 7):
        return False

    # Eliminate 0 mod 16.
    if (discmod8 == 0) and (mymod(nnn, 16) == 0):
        return False

    # Eliminate 4 times (3 mod 4).
    if discmod8 == 4:
        discby4 = nnn//4
        discby4mod4 = mymod(discby4, 4)
        if discby4mod4 == 3:
            return False

    # At this point 'nnn' is 8*odd, 4*(1 mod4), or 1 or 5 mod 8
    # Check the odd primes.
    div = 3
    while div < nroot:
#        print('test nroot, div %d %d' % (nnn, div))
        if (nnn % div) == 0:
#            print('divides nroot, div %d %d' % (nnn, div))
            ndiv = nnn//div
            if (ndiv % div) == 0:
#                print('divides twice nroot, div %d %d' % (nnn, div))
                return False
        div += 2

    return True
