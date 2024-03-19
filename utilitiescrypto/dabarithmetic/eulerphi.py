""" Euler phi function.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 20 October 2023
"""
######################################################################
def eulerphi(nnn):
    """ Euler phi function.
        This is a totally naive computation, since it basically does
        a naive factoring.
        Parameters:
            nnn: the integer to compute phi of
        Returns:
            the euler phi function of 'nnn'

    """
    ppp = 1
    iii = 2
    while nnn > 1:
        if (nnn % iii) == 0:
            ppp *= (iii-1)
            nnn /= iii
            while (nnn % iii) == 0:
                ppp *= iii
                nnn /= iii
        iii += 1
    return ppp
