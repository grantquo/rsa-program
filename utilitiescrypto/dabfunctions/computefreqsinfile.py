from collections import Counter
######################################################################
def computefreqsinfile(filename, lower=False):
    """ This creates a 'Counter' for frequency counting and then does
        a frequency count of tokens in the input list, returning the
        freqs.
        Parameters:
            filename: the filename to read and do freqs for
            lower: do we lowercase or not?
        Returns:
            the freqs 'Counter'
    """
    freqs = Counter()
    with open(filename, encoding='utf-8') as thefile:
        thedata = thefile.read()
    if lower:
        thedata = thedata.lower()
    thesplit = thedata.split()
    for token in thesplit:
        freqs[token] += 1

    return freqs
