from collections import Counter
######################################################################
def computefreqsinlist(tokenlist, lower=False):
    """ This creates a 'Counter' for frequency counting and then does
        a frequency count of tokens in the input list, returning the
        'Counter'.
        Parameters:
            tokenlist: the list of tokens to be freq-ed
            lower: do we lower case or not?
        Returns:
            the 'Counter' of freqs
    """
    freqs = Counter()
    for token in tokenlist:
        if lower:
            token = token.lower()
        freqs[token] += 1
    return freqs
