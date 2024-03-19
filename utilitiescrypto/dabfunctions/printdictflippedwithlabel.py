import sys

sys.path.append('/Users/buell/Current/Utilities/')

from DABUtilities.dabfunctions.printlistwithlabel import printlistwithlabel

######################################################################
def printdictflippedwithlabel(header, label, theformat, thedict, outfile):
    """ This will flip key-value to be value-key as for a frequency
        count, creating a list that can be sorted (thus by frequency)
        and printed to 'stdout'. If 'label' is not an empty string,
        then 'label' will be printed preceding each line.
        Parameters:
            header: a header line
            label: a label for each line
            theformat: the format for print the 'value' 
            thedict: the dict from which to print
            outfile: the file to be printed to
        Returns:
            nothing
    """
    thelist = []
    for key, value in thedict.items():
        thelist.append([value, key])
    printlistwithlabel(header, label, theformat, sorted(thelist), 2, outfile)
