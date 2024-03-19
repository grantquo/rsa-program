######################################################################
def extractcounts(thelist):
    """ This takes a list as input and computes and returns:
            total character count of all tokens in the list
            token count of all tokens in the list
            line count of lines in the list.
        Parameters:
            thelist
        Returns:
            the three counts
    """
    charcount = 0
    wordcount = 0
    for item in thelist:
        for word in item:
            charcount = charcount + len(word)
            wordcount = wordcount + 1
    return (charcount, wordcount, len(thelist))
