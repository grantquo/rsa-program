#!/usr/bin/env python
""" Program to do index calculus.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell.
    Date: 19 March 2024
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
#123456789012345678901234567890123456789012345678901234567890123456789
class TheMatrix():
    """ This is the docstring.
    """
    def __init__(self, infilename: str):
        self._numcols = -1
        self._numrows = -1
        self._logs = []
        self._header = []
        self._matrix = []
        self.readdata(infilename)


    ##################################################################
    ## Accessors.
    ##################################################################
    def getvalue(self, row, col):
        """ Function to access a single entry.
            Parameters:
                row: the row number
                col: the col number
            Returns:
                self._matrix[row][col]
        """
        return self._matrix[row][col]

    ##################################################################
    def getrow(self, row):
        """ Function to access a single row.
            Parameters:
                row: the row number
            Returns:
                self._matrix[row]
        """
        return self._matrix[row]

    ##################################################################
    ## Mutators and incrementers
    ##################################################################
    def setvalue(self, row, col, newvalue):
        """ Function to modify a single entry.
            Parameters:
                row: the row number
                col: the col number
                newvalue: the new value
            Returns:
                nothing--modifies a class variable
        """
        self._matrix[row][col] = newvalue

    ##################################################################
    ## General functions
    ##################################################################
    def display(self):
        """ Function to display the matrix.
            Parameters:
                none--all values come from inside the class
            Returns:
                nothing--prints output
        """
        ## The first row displayed is the row of actual logs (which we
        ##     have because the prime is small and we brute-forced).
        sss = f'{" ":5s} : '
#        for logsub, log in enumerate(logs):
        for colsub in range(self._numcols):
            log = self._logs[colsub]
            sss += f'{log:5d}'
            if colsub == 4:  # For 179, we have five primes in the FB.
                sss += '   '
#        print(sss)
        printoutput(sss, OUTFILE)
#        print('ZORKZORK', logs)

        ## The second row displayed is the row of FB and 'h+c' values for
        ##     which we are going to get the logarithms.
        ## This is the 'header' row.
        sss = f'{" ":5s} : '
#        for headsub, head in enumerate(header):
        for colsub in range(self._numcols):
            head = self._header[colsub]
            sss += f'{head:5d}'
            if colsub == 4:  # For 179, we have five primes in the FB.
                sss += '   '
#        print(sss)
        printoutput(sss, OUTFILE)
#        print('ZORKZORK', header)

        ## Now we print the actual matrix.
        for rowsub in range(self._numrows):
            sumoflogs = 0
            sss = f'{rowsub:5d} : '
            for colsub in range(self._numcols):
                item = self.getvalue(rowsub, colsub)
                sss += f'{item:5d}'
                if colsub == 4:  # For 179, we have five primes in the FB.
                    sss += '   '
                sumoflogs += item * self._logs[colsub]
            sumoflogs = (sumoflogs + 178) % 178
            sss += f'{sumoflogs:5d}'
            sss += f'{self._sols[rowsub]:5d}'
#            print(sss)
            printoutput(sss, OUTFILE)

    ##################################################################
    def readdata(self, infilename: str):
        """ Read the data into the variables.
            Parameters:
                infilename: the file name from which to read
            Returns:
                nothing--sets class variables
        """
        assertexists(infilename)
#        thefile = open(infilename)
        with open(infilename, encoding='utf-8') as thefile:
            lines = []
            for line in thefile:
                lines.append(line.strip())

        linecount = 0
        for line in lines:
            line = line.strip()
            lsplit = line.split()
    #        print('ZORK', lsplit)
            if linecount == 0:
                self._numrows = int(lsplit[0])
                self._numcols = int(lsplit[1])
                linecount += 1
            elif linecount == 1:
    #            print('ZORKZORK', lsplit)
                for item in lsplit:
                    self._logs.append(int(item))
                linecount += 1
            elif linecount == 2:
    #            print('ZORKZORKZORK', lsplit)
                for item in lsplit:
                    self._header.append(int(item))
                linecount += 1
            else:
                sss = f'ZORKZORKZORKZORK {str(lsplit):s}'
                printoutput(sss, OUTFILE)
                row = []
                for item in lsplit:
                    row.append(int(item))
                self._matrix.append(row)
                linecount += 1
            sss = f'ROWSCOLS {self._numrows:6d} {self._numcols:6d}'
            printoutput(sss, OUTFILE)
            sss = f'LOGS {str(self._logs):s}'
            printoutput(sss, OUTFILE)
            sss = f'HEADER   {str(self._header):s}'
            printoutput(sss, OUTFILE)
            for onerow in self._matrix:
                sss = f'{str(onerow):s}'
                printoutput(sss, OUTFILE)
            if linecount > self._numrows+2:
                break

        self._sols = []
        for _ in range(self._numrows):
            self._sols.append(0)
        self._sols[0] = 1

    ##################################################################
    def processcommands(self, commands):
        """ Process the commands to reduce the matrix.
            Parameters:
                commands: the commands to be processed
            Returns:
                nothing--output is printed
        """
        for command in commands:
            sss = f'\n{str(command):s}'
            printoutput(sss, OUTFILE)
            command = command.strip()
            comsplit = command.split()
            if comsplit[0] == 'swap':
                sss = f'\nSWAP {int(comsplit[1]):3d} {int(comsplit[2]):3d})'
                printoutput(sss, OUTFILE)
                self.swap(int(comsplit[1]), int(comsplit[2]))
            elif comsplit[0] == 'rowadd':
                dest = int(comsplit[1])
                source = int(comsplit[2])
                mult = int(comsplit[3])
#                sss = f'ADD  {int(dest):3d} {int(source):3d} {int(mult):3d}'
#                printoutput(sss, OUTFILE)
                self.rowadd(dest, source, mult)
            self.display()

    ##################################################################
    def rowadd(self, therow, theaddin, themultiplier):
        """ Function to add one row (times multiplier) to another row.
            Parameters:
                therow: the rows to be added to
                theaddin: the row to add in
                themultiplier: the multiplier times 'theaddin'
            Returns:
                nothing--changes class variables
        """
        for colsub, _ in enumerate(self.getrow(therow)):
            previous = self.getvalue(therow, colsub)
            newvalue = previous + themultiplier * int(self.getvalue(theaddin, colsub))
            self.setvalue(therow, colsub, newvalue)

    ##################################################################
    def swap(self, rowa, rowb):
        """ Function to swap two rows in the matrix.
            Parameters:
                rowa: a row
                rowb: another row
            Returns:
                nothing--changes class variables
        """
        for colsub in range(len(self._matrix[rowa])):
            temp = self._matrix[rowa][colsub]
            self._matrix[rowa][colsub] = self._matrix[rowb][colsub]
            self._matrix[rowb][colsub] = temp

## End of class
######################################################################


######################################################################
def main(infilename, commandfilename):
    """ Main function.
        Parameters:
            infilename: the file with the sieve results
        Returns:
            nothing--produces output
    """
    ##################################################################
    ## Measure process and wall clock times.
    dabtimer = DABTimer()
    logstring = dabtimer.timecall('BEGINNING')
    printoutput(logstring, LOGFILE)

    thematrix = TheMatrix(infilename)

    thematrix.display()

    assertexists(commandfilename)
    with open(commandfilename, encoding='utf-8') as commandfile:
        lines = []
        for line in commandfile:
            lines.append(line.strip())

    thematrix.processcommands(lines)

    ##################################################################
    ## Log the time and quit.
    logstring = dabtimer.timecall('ENDING')
    printoutput(logstring, LOGFILE)

######################################################################
## main Main MAIN
OPTIONS = parseargs([['-i', '--infilename', 'infilename'],
                     ['-c', '--commandfilename', 'commandfilename'],
                     ['-o', '--outfilename', 'outfilename'],
                     ['-l', '--logfilename', 'logfilename']
                     ])
with open(OPTIONS.outfilename, 'w', encoding='utf-8') as OUTFILE:
    with open(OPTIONS.logfilename, 'w', encoding='utf-8') as LOGFILE:
        printoutput(f'ARGPARSE OPTIONS {OPTIONS}', LOGFILE)
        main(OPTIONS.infilename, OPTIONS.commandfilename)
