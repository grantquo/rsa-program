D = 10958688116747337191
E = 1111111
P = 4294900427
Q = 4294901243
MODULUS = 18446173182483530761
PHIOFMODULUS = 18446173173893729092

import math

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


print(f"P={P}\nQ={Q}\nE={E}")
phimodtest = (P-1)*(Q-1)
print(f"PHIMOD={PHIOFMODULUS}\nphimodtest={phimodtest}")
modtest = P*Q
print(f"MOD={MODULUS}\nmodtest={modtest}")

block = 1371073485396775450
print(f"text block:{block}")

encrypted = starstar(block, E, MODULUS)
print(f"encrypted test={encrypted}\nencrypted num= 10635173266219078295")

listthing = euclid(E, phimodtest)
print(listthing)

decrypted = starstar(encrypted, D, MODULUS)
print(f"decrypted={decrypted}\nblock={block}")