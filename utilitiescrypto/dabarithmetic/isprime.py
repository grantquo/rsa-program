""" Totally naive program to test for primality.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
import math

######################################################################
def isprime(nnn):
    """ Totally naive test for primality -- odd number trial division.
        Parameters:
            nnn: the integer to test
        Returns:
            True or False according to the result.

    """

    ## 2 is a prime
    if nnn == 2:
        return True

    ## Other even numbers are not prime.
    if nnn%2 == 0:
        return False

    ## Trial divide by odd numbers.
    nroot = math.sqrt(nnn)
    nroot = int(nroot + 0.5)
    div = 3
    while div <= nroot:
        if nnn%div == 0:
            return False
        div += 2
    return True
