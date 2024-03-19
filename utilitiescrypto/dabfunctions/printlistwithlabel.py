######################################################################
def printlistwithlabel(header, linelabel, theformat, thelist, itemcount, outfile):
    """ This will print the 'header' and then each item in the list to
        'stdout'. If 'label' is not an empty string, then 'label' will be
        printed preceding the item.
        Parameters:
            header: a header line
            linelabel: a label for each line
            theformat: format for the 'value'
            thelist: the list to be printed
            itemcount: the number of items
            outfile: the file to be printed to
        Returns:
            nothing
    """
    if outfile == 'stdout':
        print('%s' % (header))
    else:
        outfile.write('%s\n' % (header))

    for item in thelist:
        if itemcount != 2:
            if len(linelabel) == 0:
                if outfile == 'stdout':
                    print(theformat % (str(item)))
                else:
                    outfile.write(theformat % (str(item)))
                    outfile.write('\n')
            else:
                if outfile == 'stdout':
                    print('%s ' + theformat % (linelabel, str(item)))
                else:
                    outfile.write('%s ' + theformat % (linelabel, str(item)))
                    outfile.write('\n')
        else:
            if len(linelabel) == 0:
                if outfile == 'stdout':
                    print(theformat % (item[0], item[1]))
                else:
                    outfile.write(theformat % (item[0], item[1]))
                    outfile.write('\n')
            else:
                localformat = '%s ' + theformat
                if outfile == 'stdout':
                    print(localformat % (linelabel, item[0], item[1]))
                else:
                    outfile.write(localformat % (linelabel, item[0], item[1]))
                    outfile.write('\n')
    return
