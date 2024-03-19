""" Extended Euclidean algorithm.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 19 October 2023
"""
import sys

######################################################################
def euclid(ainput, binput):
    """ Extended euclidean algorithm.
        Parameters:
            ainput: the 'a' value
            binput: the 'b' value
        Returns:
            a list [x, y, g] where a*x + b*y = g, the gcd
    """
    if ainput >= 0:
        signa = 1
        aaa = ainput
    else:
        signa = -1
        aaa = -ainput

    if binput >= 0:
        signb = 1
        bbb = binput
    else:
        signb = -1
        bbb = -binput

    if aaa == 0:
        xxx = 0
        yyy = signb
        ggg = bbb
        return [xxx, yyy, ggg]

    if bbb == 0:
        xxx = signa
        yyy = 0
        ggg = aaa
        return [xxx, yyy, ggg]

    yprevious = 0
    ycurrent = 1
    qqq = int(aaa / bbb)
    rrr = aaa % bbb
    sign = 1
#    print('outside %d = %d * %d + %d: %d, %d' % (a, b, q, r, ycurrent, sign))
    while rrr != 0:
        sign = -sign
        ynext = qqq * ycurrent + yprevious
        yprevious = ycurrent
        ycurrent = ynext
        aaa = bbb
        bbb = rrr
        qqq = int(aaa / bbb)
        rrr = aaa % bbb
#        print('inside %d = %d * %d + %d: %d, %d' % (a, b, q, r, ycurrent, sign))
    yyy = ycurrent
    if sign != signb:
        yyy = -ycurrent
    xxx = (bbb - binput * yyy) // ainput
    ggg = bbb

    if ainput*xxx + binput*yyy != ggg:
        print("ERROR euclid fails ", ainput, xxx, binput, yyy, \
                                     ainput*xxx + binput*yyy, ggg)
        sys.exit(1)
    return [xxx, yyy, ggg]
