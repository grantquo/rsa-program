""" This does Jacobi (ppp | qqq).

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Modified by Duncan A. Buell
    Date: 20 October 2023
"""
######################################################################
def jacobi(ppp, qqq):
    """ This does Jacobi (ppp | qqq).
        Parameters:
            ppp
            qqq: must be odd
        Returns:
            The Jacobi function (ppp | qqq)

    """
    if (ppp == 0) or (qqq == 0):
        return 0

    if qqq < 0:
        qqq = -qqq

    ## We have ppp and qqq both nonzero, qqq odd and positive.
    jvalue = 1
    if qqq == 1:
        return jvalue

    if ppp <= 0:
        ppp = -ppp
        if (qqq%4) == 3:
            jvalue = -jvalue

    ## Run the recursion.
    while True:
        ppp = ppp % qqq
        if ppp == 0:
            return jvalue
        while (ppp%2) == 0:
            ppp = ppp // 2
            qmod8 = qqq % 8
            if qmod8 in (3, 5):
                jvalue = -jvalue
            if ppp == 1:
                return jvalue
        if ppp == 1:
            return jvalue
        pmod4 = ppp % 4
        qmod4 = qqq % 4
        ttt = ppp
        ppp = qqq
        qqq = ttt
        if (pmod4 == 3) and (qmod4 == 3):
            jvalue = -jvalue
