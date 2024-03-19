""" This does modular reduction guaranteed to return a positive
    value.  Assuming the first mod reduction returns a value in
    abs value smaller than the modulus, adding in the modulus
    and then modding down again should give a positive value.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
######################################################################
def mymod(aaa, nnn):
    """ Do modular reduction 'aaa mod nnn' returning a positive value.
        Parameters:
            aaa:
            nnn:
        Returns:
            aaa mod nnn as a positive value
    """
    return ((aaa % nnn) + nnn) % nnn
