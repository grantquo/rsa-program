#!/usr/bin/env python
""" Program to create numbers to factor with Pollard rho.
    The numbers are products of primes of equal size.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 27 October 2023
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
def dopollardpminus1(nnn, primeslist, printdetail):
    """ Function to run Pollard p-1 on an integer.
        Note that this is clumsy in that it exponentiates one prime
        at a time instead of building the huge exponent 'M'.
        Parameters:
            nnn: the integer to try to factor
            primeslist: the list of primes
            printdetail: do we print every step or not?
        Returns:
            either the gcd, or 1:
    """
    primeslist = [2] + primeslist
    explimit = 10
    base = 3
    prod = 3
    fullprod = 3
    success = 0
    rootn = sqrt(nnn + 0.0)
    dumpfreq = 10
    for pppsub, ppp in enumerate(primeslist):
#        printoutput(f'PRIME {ppp:14d}', OUTFILE)

        ## If the prime is bigger that root p-1, punt.
        if ppp > rootn:
            break

        if pppsub % dumpfreq == 0:
            sss = f'PPPSUB, PPP {pppsub} {ppp}'
            printoutput(sss, OUTFILE)

        ## Exponentiate the base to the prime power value.
        ## This is a kluge; we are not doing the bit by bit version.
        for _ in range(0, explimit):
            for _ in range(1, ppp):
                fullprod = fullprod * base
                prod = (prod * base) % nnn
            base = prod

        ## In this version, we do the gcd with every step.
        xxx, yyy, ggg = euclid(prod - 1, nnn)
        if ggg > 1:
            cofactor = nnn // ggg
            ## We can leave in the verification that the factoring worked.
            testvalue = ggg * cofactor - nnn
            sss = f'GCD {nnn:10d} {pppsub:7d} {ppp:10d} {ggg:10d}'
            sss += f' {cofactor:10d} {testvalue:d}'
            printoutput(sss, OUTFILE)
            success = 1
            return success

    return success

######################################################################
def dopollardrho(nnn, epactestimate, printdetail):
    """ Function to run Pollard rho on an integer.
        To make things go faster, we will keep a running product of
        the differences between 'xxm' and 'xx2m'.  In this way, if
        we wanted to speed things up, we could do the gcd only every
        so often, instead of every time.
        Parameters:
            nnn: the integer to try to factor
            epactestimate: the worst case of root(p) times ln(p)
            printdetail: do we print intermediate output or not?
        Returns:
            nothing -- it factors or it doesn't
    """
    prod = 1
    xxm = 2
    xx2m = 3 # for 'xxm' squared minus 1
#    xx2m = 5 # for 'xxm' squared plus 1  ## One can do plus 1 or minus 1.
    diff = xx2m - xxm
    prod = (prod * diff) % nnn
    count = 1
    if printdetail:
        sss = 'count,xm,x2m,diff,prod'
        sss += f' {" ":3s} {count:6d} {xxm:10d} {xx2m:10d} {diff:10d} {prod:10d}'
        printoutput(sss, OUTFILE)

    iterationlimit = 1000000000
#    iterationlimit = 100
    while count < iterationlimit:
        count += 1
        xxm = (xxm * xxm - 1) % nnn
        xx2m = (xx2m * xx2m - 1) % nnn
        xx2m = (xx2m * xx2m - 1) % nnn
#        xxm = (xxm * xxm + 1) % nnn
#        xx2m = (xx2m * xx2m + 1) % nnn
#        xx2m = (xx2m * xx2m + 1) % nnn

        ## Something to be aware of.  If we do the percent operator on
        ## a negative number, does it round down toward negative infinity,
        ## or truncate toward zero, and does it return a negative number
        ## or the least positive?  Since we are subtracting, the difference
        ## could be negative, but it won't be less than minus 'nnn'.  So we
        ## add 'nnn' to get a positive number before modding down by 'nnn'.
        diff = (xx2m - xxm + nnn) % nnn
        prod = (prod * diff) % nnn
        xxx, yyy, ggg = euclid(prod, nnn)

        if ggg > 1:
            if printdetail:
                sss = 'count,xm,x2m,diff,prod,gcd'
                sss += f' {count:6d} {xxm:10d} {xx2m:10d}'
                sss += f' {diff:10d} {prod:10d} {ggg:10d}'
                printoutput(sss, OUTFILE)

            epactqt = epactestimate/count
            sss = f'N,M,EP,FACTOR,QUOTIENT {nnn:10d}'
            sss += f' {count:8d} {epactqt:10.6f} {ggg:10d} {nnn//ggg:10d}'
            printoutput(sss, OUTFILE)

            return 1

        if printdetail:
            sss = 'count,xm,x2m,diff,prod,gcd'
            sss += f' {count:6d} {xxm:10d} {xx2m:10d} {diff:10d}'
            sss += f' {prod:10d} {ggg:10d}'
            printoutput(sss, OUTFILE)
    return 0

######################################################################
def dotrialdivision(nnn, primeslist, printdetail):
    """ Function for trial division.
        Parameters:
            nnn: the number to try to factor
            primeslist: the list of primes to use for trial division
            printdetail: do we print intermediate output or not?
        Returns:
            the list of the centroids
    """
    if printdetail:
        sss = f'\nFACTOR {nnn:24d}'
        printoutput(sss, OUTFILE)
    success = 0
    done = False
    for ppp in primeslist:
        if nnn < ppp*ppp:
            if printdetail:
                sss = f'PRIME COFACTOR {nnn:24d}'
                printoutput(sss, OUTFILE)
                done = True
            success = 1
        if done:
            break
        if 0 == nnn % ppp:
            while 0 == nnn % ppp:
                if done:
                    success = 1
                    break
                newnnn = nnn // ppp
                if printdetail:
                    sss = f'FACTOR {ppp:24d} {nnn:24d} {newnnn:24d}'
                    printoutput(sss, OUTFILE)
                nnn = newnnn

    return success

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

    ## Compute the big O of the epact.
    lastnnn = nnnlist[-1]
    thesquareroot = sqrt(lastnnn)
    thefourthroot = sqrt(thesquareroot)
    thelog = log(thesquareroot)
    epact = thefourthroot * thelog
    sss = f'EPACT {lastnnn} {thelog} {epact}'
    printoutput(sss, OUTFILE)

    ## First we will do trial division, and time the computation.
    printoutput(DABTIMER.timecall('BEGIN TRIAL'), OUTFILE)
    successes = 0
    for nnn in nnnlist:
        successes += dotrialdivision(nnn, primeslist, printdetail)
    sss = f'RHO SUCCESSES {successes}'
    printoutput(sss, OUTFILE)
    printoutput(DABTIMER.timecall('END TRIAL'), OUTFILE)

    ## Now we'll do Pollard rho.
    printoutput(DABTIMER.timecall('BEGIN RHO'), OUTFILE)
    successes = 0
    for nnn in nnnlist:
        successes += dopollardrho(nnn, epact, printdetail)
    sss = f'RHO SUCCESSES {successes}'
    printoutput(sss, OUTFILE)
    printoutput(DABTIMER.timecall('END RHO'), OUTFILE)

    ## And finally, Pollard p minus 1.
    printoutput(DABTIMER.timecall('BEGIN PMINUS1'), OUTFILE)
    successes = 0
    for nnn in nnnlist:
        successes += dopollardpminus1(nnn, primeslist, printdetail)
    sss = f'PMINUS1 SUCCESSES {successes}'
    printoutput(sss, OUTFILE)
    printoutput(DABTIMER.timecall('END PMINUS1'), OUTFILE)

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
