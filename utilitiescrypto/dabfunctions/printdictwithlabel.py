######################################################################
def printdictwithlabel(header, linelabel, theformat, thedict):
    """ This will print the 'header' and then each key-value pair in
        the dict to 'stdout'. If 'label' is not an empty string, then
        'label' will be printed preceding the item.
    """
    for first, second in thedict.items():
        if len(linelabel) == 0:
            print(theformat % (first, second))
        else:
            print(theformat % (linelabel, first, second))
    return
OUTFILE = None
LOGFILE = None
