######################################################################
def getfileaslist(filename):
    """ This will open 'filename' as a file, read the entire text,
        tokenize the entire text, and then return the token list as
        a list.
        Parameters:
            filename: the file to be read and returned as a list
        Returns:
            the list of tokens
    """
    with open(filename, encoding='utf-8') as thefile:
        thetext = thefile.read()
    thelist = thetext.split()

    return thelist
