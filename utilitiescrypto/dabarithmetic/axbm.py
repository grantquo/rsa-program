""" This is the function for solving
        a * x == b (mod m)
    Parameters:
        ainput: the 'a' value
        binput: the 'b' value
        minput: the modulus 'm' value
    Returns:
        xxx that solves the congruence

        returns  1     if congruence is 0 = 0
                -value if congruence is (0) = (<>0)
                -g = gcd(a,m) if g does not divide b

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
import sys

#sys.path.append('/Users/buell/Current/PythonUtilities/') # office directory

## Buell local path addition
#sys.path.append('/Users/buell/Current/Utilities/')

## CS401 local path addition
sys.path.append('/home/kingkoobie/cs401/utilitiescrypto/dabarithmetic')

#pylint: disable=import-error
#pylint: disable=wrong-import-position

#from DABArithmetic.dabarithmetic.mymod import mymod
# from dabarithmetic.mymod import mymod

#pylint: enable=import-error
#pylint: enable=wrong-import-position

def mymod(aaa, nnn):
    """ Do modular reduction 'aaa mod nnn' returning a positive value.
        Parameters:
            aaa:
            nnn:
        Returns:
            aaa mod nnn as a positive value
    """
    return ((aaa % nnn) + nnn) % nnn


def axbm(ainput, binput, minput):
    """ Compute 'x', such that a*x = b (mod m).
        Returns 'x' as value of function.
        Parameters:
            ainput: the 'a' value
            binput: the 'b' value
            minput: the modulus 'm' value
        Returns:
            'x' that solves the congruence
    """
#    sss = f'\nZORK a, b, m {ainput:4d} {binput:4d} {minput:4d}'
#    print(sss)
    ## If ainput is zero mod minput
    ##     and binput is zero mod minput
    ##         then return 1, since we have 0 = 0
    aaa = mymod(ainput, minput)
    if aaa == 0:
        bbb = mymod(binput, minput)
        if bbb == 0:
#            return -minput
            return 1
        else:
#            print('NOSOLUTION: zero is not zero')
            return -1

    mmm = minput
#    aaa = ((ainput % mmm) + mmm) % mmm ## we assume m is positive?
    aaa = mymod(ainput, mmm)
    qqq = int(mmm//aaa)
    rrr = mmm % aaa
    nnn1 = 0
    nnn2 = 1
    sgn = 1
    while rrr != 0:
        sgn = - sgn
        nnn3 = nnn2 * qqq + nnn1
        nnn1 = nnn2
        nnn2 = nnn3
        mmm = aaa
        aaa = rrr
        qqq = int(mmm//aaa)
        rrr = mmm % aaa

    bbb = int(binput // aaa)
    ttt = binput % aaa
    if ttt != 0:
        print('NOSOLUTION: gcd does not divide b')
        return -aaa

    # The check value 'ttt' is zero, so we have a gcd.
    xxx = (bbb * nnn2) % minput
    if sgn == -1:
        xxx = -xxx
    if xxx < 0:
        xxx += minput
    return xxx
