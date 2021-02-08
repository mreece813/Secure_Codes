""" Michael Reece
    RUID: 177000762
    10/3/2019    """


def replace_element(L, oldel, newel):
    """ replaces and old number with a new one at every occurrence """
    if len(L) < 2:
        if L[0] == oldel:
            L[0] = newel
        return L 
    else:
        L =  replace_element(L[-1:], oldel, newel) + replace_element(L[:-1], oldel, newel)
        return L

def num_double_letters(astr):
    """ checks if there are any double letters in the astr"""
    if len(astr) == 1:
        return 0
    else:
        if astr[0] == astr[1]:
            return 1 + num_double_letters(astr[1:])
        else:
            return 0 + num_double_letters(astr[1:])


def has_repeats(L):
    """checks if there are any repeats in the list L"""
    if len(L) == 1:
        return False
    elif L[0] == L[1]:
        return True
    else:
        if len(L) > 2:
            L1 = L[0:1] + L[2:]
            if has_repeats(L1):
                return True
            else:
                L1 = L[1:]
                if has_repeats(L1):
                    return True
                else:
                    return False
