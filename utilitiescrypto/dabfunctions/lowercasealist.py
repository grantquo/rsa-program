######################################################################
def lowercasealist(tokenlist):
    """ This will take in a list of tokens, lowercase each token into
        a second list, and return the second list.
        Parameters:
            tokenlist: the list of tokens to be lowercased
        Returns:
            the list of lowercased tokens
    """
    ttt = []
    for word in tokenlist:
        word = word.lower()
        ttt.append(word)
    return ttt
