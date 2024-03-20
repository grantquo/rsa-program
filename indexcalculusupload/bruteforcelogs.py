#!/usr/bin/env python
""" Brute force the log computation, for small primes.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell.
    Date: 26 November 2023
"""
import sys

#from collections import defaultdict

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
def main(infilename: str):
    """ Main program for doing brute force log computations.
        Parameters:
            infilename: file with the prime
        Returns:
            nothing--writes output
    """
    ##################################################################
    ## Measure process and wall clock times.
    dabtimer = DABTimer()
    logstring = dabtimer.timecall('BEGINNING')
    printoutput(logstring, LOGFILE)

    assertexists(infilename)

    with open(infilename, encoding='utf-8') as thefile:
        ppp = int(thefile.read())

    print(ppp)
    exp = 1
    root = 2
    power = 2
    while power != 1:
        power *= root
        power = power % ppp
        exp += 1
        sss = f'RESIDUE AND EXP {power:5d} {exp:5d}'
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
