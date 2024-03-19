""" This is my version of an argument parser.
"""
#import sys
import argparse
#######################################################################
def parseargs(arglist):
    """ This is my version of an argument parser.
        Parameters:
            arglist: the command line list of args
        Returns:
            the result of parsing with the system parser
    """
    parser = argparse.ArgumentParser()

    for onearg in arglist:
        parser.add_argument(onearg[0], onearg[1], help=onearg[2])
    args = parser.parse_args()

    return args
