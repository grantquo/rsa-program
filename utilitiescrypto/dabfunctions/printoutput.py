OUTFILE = None
LOGFILE = None
######################################################################
def printoutput(outstring, outfile):
    """ Prints 'outstring' to 'stdout' and to 'outfile'.
        Parameters:
            outstring: the string to be printed
            outfile: the output file to be printed to
        Returns:
            nothing
    """
    print(outstring)
    sss = f'{outstring:s}\n'
    outfile.write(sss)
    outfile.flush()
