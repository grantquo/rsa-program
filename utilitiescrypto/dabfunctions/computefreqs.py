from collections import Counter
######################################################################
def computefreqs(tokenlist):
    """ This creates a 'Counter' for frequency counting and then
        does a frequency count of tokens in the input list, returning
        the frequency 'Counter'.
        Parameters:
            tokenlist: the list of tokens to be freq-ed
        Returns:
            the freq Counter
    """
    freqs = Counter()
    for token in tokenlist:
        freqs[token] = freqs[token] + 1
    return freqs
