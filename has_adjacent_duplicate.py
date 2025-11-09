def has_adjacent_duplicate(L):
    ### Replace with your own code (begin) ###
    if not len(L) > 1:
        return False

    for i in range (len(L) - 1):
        if L[i] == L[i + 1]:
            return True
        
    return False
    ### Replace with your own code (end)   ###