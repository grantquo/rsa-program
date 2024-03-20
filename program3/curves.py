"""
============================================================
Grant Gutterman
3-20-2024
curves.py

Main file for elliptic curves point calculations.
============================================================
"""

import os
import math

def expo(aaa, bbb):
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
        multiplier *= multiplier
        localexponent = localexponent // 2
#        print(f'{localexponent:d} {multiplier:d} {runningproduct:d}'

    return runningproduct

def mymod(aaa, nnn):
    """ Do modular reduction 'aaa mod nnn' returning a positive value.
        Parameters:
            aaa:
            nnn:
        Returns:
            aaa mod nnn as a positive value
    """
    return ((aaa % nnn) + nnn) % nnn

def printpoints():
    pass

def jacob_coord(xxx3, yyy3, zin):
    xxx3_jacob = mymod((xxx3*expo(zin, 2)), 31)
    yyy3_jacob = mymod((yyy3*expo(zin, 3)), 31)
    return xxx3_jacob, yyy3_jacob

def satisfy_curve(xxx, prime):
    
    # !!! Curve equation is embedded in THIS function!
    # To change, see conditionals   |   |
    #                               V   V

    yyy1 = expo(xxx, 3)+3*xxx+4
    yyy2 = mymod(expo(xxx, 3)+3*xxx+4, prime)

    if type(yyy1) == int:
        point_found(xxx, yyy1, prime)
    if type(yyy2) == int:
        point_found(xxx, yyy2, prime)
    if type(mymod(yyy3, prime)) == int:
        point_found(xxx, yyy1, prime)

    return
    # x and y inputs must be jacob_coord output

def point_found(xxx, yyy, prime):
    return print(f"SOLUTION ! ( {xxx}, {yyy}, 1 )")

def loop_points(prime):
    
    #naively loop through x coordinates
    xxx = 0
    while xxx<=prime:
        satisfy_curve(xxx, prime)
        xxx+=1
    return

def zinverse(zzz, ppp):
    return mymod(expo(zzz, -1), ppp)

def double_point(xxx, yyy, zzz, coef_a):
    
    aaa = expo(yyy, 2)
    bbb = 4*xxx*aaa
    ccc = 8*expo(aaa, 2)
    ddd = 3*expo(xxx, 2)+coef_a*expo(zzz, 4)
    
    doubled_x = expo(ddd, 2)-2*bbb
    doubled_y = ddd*(bbb-doubled_x)-ccc
    doubled_z = 2*yyy*zzz
    print(f"in function:\ndoubled_x: {doubled_x}\ndoubled_y: {doubled_y}\ndoubled_z: {doubled_z}")
    
    return doubled_x, doubled_y, doubled_z

def add_point(xxx1, yyy1, zzz1, xxx2, yyy2):
    
    aaa = expo(zzz1, 2)
    bbb = aaa*zzz1
    ccc = xxx2*aaa
    ddd = yyy2*bbb
    eee = ccc-xxx1
    fff = ddd-yyy1
    ggg = expo(eee, 2)
    hhh = ggg*eee
    iii = xxx1*ggg
    
    xxx3 = expo(fff, 2)-(hhh+2*iii)
    yyy3 = fff*(iii-xxx3)-yyy1*hhh
    zzz3 = zzz1*eee
    
    return xxx3, yyy3, zzz3

# loop_points(31)
print(8%31)
print(mymod(15**2, 31))
print(mymod(16**2, 31))
