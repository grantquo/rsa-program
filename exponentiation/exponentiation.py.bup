#!/usr/bin/env python
""" Program to compute modular exponentiation.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell.
    Date: 3 February 2024
"""
import sys
import math

## Buell local path addition
#sys.path.append('/Users/buell/Current/Utilities/')

## CS401 local path addition
sys.path.append('/Users/buell/Current/cscrypto/examples/utilitiescrypto/')

#pylint: disable=import-error
#pylint: disable=wrong-import-position
#from DABUtilities.dabfunctions.myargparse import parseargs
#from DABUtilities.dabfunctions.printoutput import printoutput
#from DABUtilities.dabfunctions.dabtimer import DABTimer

from dabfunctions.assertexists import assertexists
from dabfunctions.myargparse import parseargs
from dabfunctions.printoutput import printoutput
from dabfunctions.dabtimer import DABTimer

#pylint: enable=import-error
#pylint: enable=wrong-import-position

######################################################################
#123456789012345678901234567890123456789012345678901234567890123456789
######################################################################
def starstarlefttoright(aaa, bbb, nnn):
    """ Modular integer exponentiation bits taken left to right.
        This computes a^b mod n using the efficient bit representation
        of the exponent.
        Parameters:
            aaa: the base
            bbb: the exponent
            nnn: the modulus
        Returns:
            aaa ^ bbb mod nnn list of the centroids
    """
    bits = []
    bitsinteger = bbb
    while bitsinteger > 0:
        bit = bitsinteger % 2
        bits = [bit] + bits
        bitsinteger = bitsinteger // 2
    
    runningproduct = 1
    multiplier = aaa
    leftmostbit = bits[0]
    sss = f'APROD MULT LEFT BITS {runningproduct:3d} {multiplier:3d}'
    sss += f' {leftmostbit:3d} {str(bits)}'
    printoutput(sss, OUTFILE)
    result = 1
    while len(bits) > 0:
        leftmostbit = bits[0]
        if leftmostbit == 1:
            runningproduct *= multiplier
            runningproduct = runningproduct % nnn
        result = runningproduct
        sss = f'BPROD MULT LEFT BITS {runningproduct:3d} {multiplier:3d}'
        sss += f' {leftmostbit:3d} {str(bits)}'
        printoutput(sss, OUTFILE)
        runningproduct *= runningproduct
        runningproduct = runningproduct % nnn
        bits = bits[1:]
        sss = f'CPROD MULT LEFT BITS {runningproduct:3d} {multiplier:3d}'
        sss += f' {leftmostbit:3d} {str(bits)}'
        printoutput(sss, OUTFILE)

    return result

######################################################################
def starstarrighttoleft(aaa, bbb, nnn):
    """ Modular integer exponentiation bits taken right to left.
        This computes a^b mod n using the efficient bit representation
        of the exponent.
        Parameters:
            aaa: the base
            bbb: the exponent
            nnn: the modulus
        Returns:
            aaa ^ bbb mod nnn list of the centroids
    """
    bits = []
    bitsinteger = bbb
    while bitsinteger > 0:
        bit = bitsinteger % 2
        bits = [bit] + bits
        bitsinteger = bitsinteger // 2
    
    runningproduct = 1
    multiplier = aaa
    localexponent = bbb
    sss = f'APROD MULT LOCAL BITS {runningproduct:3d} {multiplier:3d}'
    sss += f' {localexponent:3d} {str(bits)}'
    printoutput(sss, OUTFILE)
    while localexponent > 0:
        rightmostbit = localexponent % 2
        if rightmostbit == 1:
            runningproduct *= multiplier
            runningproduct = runningproduct % nnn
        multiplier *= multiplier
        multiplier = multiplier % nnn
        localexponent = localexponent // 2
        bits = bits[:-1]
        sss = f'BPROD MULT LOCAL BITS {runningproduct:3d} {multiplier:3d}'
        sss += f' {localexponent:3d} {str(bits)}'
        printoutput(sss, OUTFILE)
#        print(f'{localexponent:d} {multiplier:d} {runningproduct:d}'

    return runningproduct

######################################################################
def main():
    """ Main program for modular exponentiation.
        Parameters:
            none
        Returns:
            nothing--prints output
    """
    ##################################################################
    ## Measure process and wall clock times.
    dabtimer = DABTimer()
    logstring = dabtimer.timecall('BEGINNING')
    printoutput(logstring, LOGFILE)

#    assertexists(infilename)
#    with open(infilename, encoding='utf-8') as thefile:
#        thedata = thefile.read()
#        ppp = [float(item) for item in thedata.split()]
#        sss = f'{str(ppp)}'
#        printoutput(sss, OUTFILE)

    result = starstarrighttoleft(3, 13, 17)
    sss =f'RESULT RL {result}\n'
    printoutput(sss, OUTFILE)

    result = starstarlefttoright(3, 13, 17)
    sss =f'RESULT LR {result}'
    printoutput(sss, OUTFILE)

    ##################################################################
    ## Log the time and quit.
    logstring = dabtimer.timecall('ENDING')
    printoutput(logstring, LOGFILE)

######################################################################
## main Main MAIN
OPTIONS = parseargs([['-o', '--outfilename', 'outfilename'],
                     ['-l', '--logfilename', 'logfilename']
                     ])
with open(OPTIONS.outfilename, 'w', encoding='utf-8') as OUTFILE:
    with open(OPTIONS.logfilename, 'w', encoding='utf-8') as LOGFILE:
        printoutput(f'ARGPARSE OPTIONS {OPTIONS}', LOGFILE)
        main()
