#!/usr/bin/env python
""" Program to do modular integer exponentiation. 

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
######################################################################
def starstar(aaa, bbb, nnn):
    """ Modular integer exponentiation.
        This computes a^b mod n using the efficient bit representation
        of the exponent.
        Parameters:
            aaa: the base
            bbb: the exponent
            nnn: the modulus
        Returns:
            aaa ^ bbb mod nnn list of the centroids

    """
    runningproduct = 1
    multiplier = aaa
    localexponent = bbb
    while localexponent > 0:
        rightmostbit = localexponent % 2
        if rightmostbit == 1:
            runningproduct *= multiplier
            runningproduct = runningproduct % nnn
        multiplier *= multiplier
        multiplier = multiplier % nnn
        localexponent = localexponent // 2
#        print(f'{localexponent:d} {multiplier:d} {runningproduct:d}'

    return runningproduct
