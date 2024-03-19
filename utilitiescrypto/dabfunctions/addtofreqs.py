######################################################################
def addtofreqs(thelist, freqs):
    """ This takes in a token list and a freq dictionary and
        increments the dictionary for each token in the list.
        It then returns the updated version of the dictionary.
        THIS REQUIRES A DEFAULTDICT AND NOT JUST A DICT
        Parameters:
            thelist: the tokens to add freq counts for
            freqs: the Counter to add freq counts into
        Returns:
            the updated version of freqs
    """
    for token in thelist:
        freqs[token] += 1
    return freqs
