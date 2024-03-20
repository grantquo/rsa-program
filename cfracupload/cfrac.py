#!/usr/bin/env python
""" Program to run the continued fraction algorithm.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 20 February 2024
"""
import sys
from math import sqrt
from math import log

## Buell local path addition
#sys.path.append('/Users/buell/Current/Utilities/')

## CS401 local path addition
sys.path.append('/Users/buell/Current/cscrypto/examples/utilitiescrypto/')

#pylint: disable=import-error
#pylint: disable=wrong-import-position

from dabarithmetic.euclid import euclid

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
def docfrac(nnn, primeslist, printdetail):
    """ Function to run CFRAC on an integer to be factored.
        Parameters:
            nnn: the integer to try to factor
            primeslist: the list of primes
            printdetail: do we print every step or not?
        Returns:
            a list of the steps along the way
    """
    rootn = sqrt(nnn + 0.0)
    print(nnn, rootn, int(rootn))

    bigpi = 0
    bigqi = 1
    ai = int(rootn)
    piminus2 = 0
    piminus1 = 1
    qiminus2 = 1
    qiminus1 = 0

    thelist = []
    minusmultiplier = 1
    for iii in range(26):
        pi = ai * piminus1 + piminus2
        pi = (pi + nnn) % nnn
        qi = ai * qiminus1 + qiminus2
        qi = (qi + nnn) % nnn

        bigpiplus = ai * bigqi - bigpi
        bigqiplus = (nnn - bigpiplus * bigpiplus) // bigqi
        aiplus = int((bigpiplus + rootn) / bigqiplus)

        sublist = [iii, piminus1, qiminus1, bigpi, bigqi, ai]
        smoothness = factorbigqi(bigqi, minusmultiplier)
        sublist = sublist + smoothness
        thelist.append(sublist)

        test = pi*pi - nnn*qi*qi + minusmultiplier*bigqiplus

        sss = f'pi,minus1,minus2 {pi:5d} {piminus1:5d} {piminus2:5d}\n'
        sss += f'qi,minus1,minus2 {qi:5d} {qiminus1:5d} {qiminus2:5d}\n'
        sss += f'bigpiplus,bigpi  {bigpiplus:5d} {bigpi:5d}\n'
        sss += f'bigqiplus,bigqi  {bigqiplus:5d} {bigqi:5d}\n'
        sss += f'aiplus,ai,test   {aiplus:5d} {ai:5d} {test:d}\n'
        printoutput(sss, OUTFILE)

        ## Now shift the values.
        piminus2 = piminus1
        piminus1 = pi
        qiminus2 = qiminus1
        qiminus1 = qi
        bigpi = bigpiplus
        bigqi = bigqiplus
        ai = aiplus
        minusmultiplier = -minusmultiplier

    return thelist

######################################################################
def factorbigqi(bigqi, signum):
    """ Function for testing smoothness.
        Parameters:
            bigqi: the value to test
            signum: the minus sign
        Returns:
            the list of factors
    """
    ## primes are -1, 2, 3, 5, 13, 17, 19
    subm = 0 
    sub2 = 1 
    sub3 = 2 
    sub5 = 3 
    sub13 = 4 
    sub17 = 5 
    sub19 = 6 
    subbig = 7 
    factors = [0,0,0,0,0,0,0,0]
    if signum < 0:
        factors[subm] = 1

    localbig = bigqi

    ## We're going to brute force this in the naive and clumsy way.
    if localbig % 2 == 0:
        while localbig % 2 == 0:
            factors[sub2] += 1
            localbig = localbig // 2

    if localbig % 3 == 0:
        while localbig % 3 == 0:
            factors[sub3] += 1
            localbig = localbig // 3

    if localbig % 5 == 0:
        while localbig % 5 == 0:
            factors[sub5] += 1
            localbig = localbig // 5

    if localbig % 13 == 0:
        while localbig % 13 == 0:
            factors[sub13] += 1
            localbig = localbig // 13

    if localbig % 17 == 0:
        while localbig % 17 == 0:
            factors[sub17] += 1
            localbig = localbig // 17

    if localbig % 19 == 0:
        while localbig % 19 == 0:
            factors[sub19] += 1
            localbig = localbig // 19

    if localbig == 1:
        factors[subbig] = 0
    else:
        factors[subbig] = localbig

    return factors

######################################################################
def readnnn(nnnfilename):
    """ Function for reading in the integers to factor.
        Parameters:
            nnnfilename: the file name from which to read the integers
        Returns:
            the list of the integers to factor
    """
    assertexists(nnnfilename)
    nnnlist = []
    with open(nnnfilename, encoding='utf-8') as thennn:
        for line in thennn:
            nnnlist.append(int(line.strip()))

    return nnnlist

######################################################################
def readprimes(primesfilename):
    """ Function for reading in the primes.
        Note that for trial division we hard code adding the 2, since
        the files of primes usually have only the odd primes.
        Parameters:
            primesfilename: the file name from which to read primes
        Returns:
            the list of the primes
    """
    assertexists(primesfilename)
    primes = [2]
    with open(primesfilename, encoding='utf-8') as theprimes:
        for line in theprimes:
            primes.append(int(line.strip()))

    return primes

######################################################################
def main(nnnfilename: str, primesfilename: str, printdetail: str):
    """ Main function.
        Parameters:
            nnnfilename: the file with the list of primes to try
        Returns:
            nothing
    """
    if printdetail == 'False':
        printdetail = False
    else:
        printdetail = True
    ##################################################################
    ## Measure process and wall clock times.
    printoutput(DABTIMER.timecall('BEGINNING'), LOGFILE)

    primeslist = readprimes(primesfilename)

    nnnlist = readnnn(nnnfilename)

    ## Run CFRAC on the numbers in the list.
    printoutput(DABTIMER.timecall('BEGIN CFRAC'), OUTFILE)
#    successes = 0
    for nnn in nnnlist:
        thelist = docfrac(nnn, primeslist, printdetail)
    hhh = ['i', 'p-1', 'q-1', 'Pi', 'Qi', 'ai']
    hhh = hhh + [-1, 2, 3, 5, 13, 17, 19]
    sss = f'{hhh[0]:>3s} {hhh[1]:>7s} {hhh[2]:>7s} {hhh[3]:>4s} {hhh[4]:>4s} {hhh[5]:>4s}'
    sss += f' {hhh[6]:3d} {hhh[7]:3d} {hhh[8]:3d} {hhh[9]:3d} {hhh[10]:3d} {hhh[11]:3d} {hhh[12]:3d}'
    printoutput(sss, OUTFILE)
    for sublist in thelist:
        sss = f'{sublist[0]:3d} {sublist[1]:7d} {sublist[2]:7d}'
        sss += f' {sublist[3]:4d} {sublist[4]:4d} {sublist[5]:4d}'
        for subscript in range(6, len(sublist)):
            sss += f' {sublist[subscript]:3d}'
        printoutput(sss, OUTFILE)
    printoutput(DABTIMER.timecall('END CFRAC'), OUTFILE)

    ##################################################################
    ## Log the time and quit.
    printoutput(DABTIMER.timecall('ENDING'), LOGFILE)

######################################################################
## main Main MAIN
OPTIONS = parseargs([['-i', '--nnnfilename', 'nnnfilename'],
                     ['-r', '--primesfilename', 'primesfilename'],
                     ['-p', '--printdetail', 'printdetail'],
                     ['-o', '--outfilename', 'outfilename'],
                     ['-l', '--logfilename', 'logfilename']
                     ])
DABTIMER = DABTimer()
with open(OPTIONS.outfilename, 'w', encoding='utf-8') as OUTFILE:
    with open(OPTIONS.logfilename, 'w', encoding='utf-8') as LOGFILE:
        printoutput(f'OPTIONS {OPTIONS}', LOGFILE)
        main(OPTIONS.nnnfilename, OPTIONS.primesfilename, OPTIONS.printdetail)
