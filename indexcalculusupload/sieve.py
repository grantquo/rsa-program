#!/usr/bin/env python
""" Program to sieve for complete factorings for an index calculus.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell.
    Date: 19 March 2024
"""
import sys

from collections import defaultdict

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
def factor(nnn, facbase):
    """ Function to factor over the factor base.
        Parameters:
            nin: the number to factor
        Returns:
            factors: the factors of 'nnn'
    """
    factors = []
    nlocal = nnn
    if nlocal < 0:
        factors.append(-1)
        nlocal = -nlocal
    for prime in facbase:
        if nlocal % prime == 0:
            while nlocal % prime == 0:
                factors.append(prime)
                nlocal = nlocal // prime
                if nlocal == 1:
                    break
    factors.append(nlocal)

    return factors

######################################################################
def readdata(infilename: str):
    """ Read the input data and return the configuration data.
        Parameters:
            infilename: the file from which to read the config data
        Returns:
            the 'dict' of prime, square root, J, and factor base
    """
    assertexists(infilename)

    config = defaultdict()
    with open(infilename, encoding='utf-8') as thefile:
        for line in thefile:
            lsplit = line.split()
            config[lsplit[0]] = lsplit[1:]

    ## Things were read as 'str' data, so we convert to 'int'.
    for key, value in sorted(config.items()):
#        print(key, value)
        intval = [int(item) for item in value]
        config[key] = intval
#        print(key, config[key])

    return config

######################################################################
def main(infilename: str):
    """ Main program.
        Parameters:
            infilename: the file from which to read the config data
        Returns:
            nothing--output is printed
    """
    ##################################################################
    ## Measure process and wall clock times.
    dabtimer = DABTimer()
    logstring = dabtimer.timecall('BEGINNING')
    printoutput(logstring, LOGFILE)

    config = readdata(infilename)
    ppp = config['ppp'][0]
    hhh = config['hhh'][0]
    jjj = config['jjj'][0]
    facbase = list(config['fb'])
    sss = f'PRIME,H,J,FB {ppp:6d} {hhh:6d} {jjj:6d} {str(facbase):s}'
    printoutput(sss, OUTFILE)

    ## Run loops on small values of 'cc1' and 'cc2'.
    ## Since 'hhh' is about root('ppp'), 'product' becomes a little
    ##     larger than 'ppp'.
    ## Thus 'product - ppp' might be small enough to be smooth over 'facbase'.
    ## Run loops on small values of cc1 and cc2.
    for cc1 in range(-5, 5):
        for cc2 in range(cc1+1, 6):
            hhhplusc1 = hhh + cc1
            hhhplusc2 = hhh + cc2
            product = hhhplusc1 * hhhplusc2
            c1c2 = cc1 * cc2
            hhhtimessum = hhh * (cc1 + cc2)
            sss = f'{cc1:3d} {cc2:3d} {hhhplusc1:3d} {hhhplusc2:3d}'
            sss += f' {product:5d} {jjj:5d} {hhhtimessum:5d} {c1c2:5d}'
            testsmooth = product - ppp
            sss += f' {testsmooth:5d} '
            sss += str(factor(testsmooth, facbase))
#            print(cc1, cc2, hhhplusc1, hhhplusc2, product, jjj, hhhtimessum, c1c2)
            printoutput(sss, OUTFILE)

    ##################################################################
    ## Log the time and quit.
    logstring = dabtimer.timecall('ENDING')
    printoutput(logstring, LOGFILE)

######################################################################
## main Main MAIN
OPTIONS = parseargs([['-i', '--infilename', 'infilename'],
                     ['-o', '--outfilename', 'outfilename'],
                     ['-l', '--logfilename', 'logfilename']
                     ])
with open(OPTIONS.outfilename, 'w', encoding='utf-8') as OUTFILE:
    with open(OPTIONS.logfilename, 'w', encoding='utf-8') as LOGFILE:
        printoutput(f'ARGPARSE OPTIONS {OPTIONS}', LOGFILE)
        main(OPTIONS.infilename)
