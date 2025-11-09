def swap_ends(L, k):
    ### Replace with your own code (begin) ###
    len_L = len(L)
    
    if k <= 0 or len_L == 0 or k > len_L // 2:
        return (L.copy(), 0)
    
    new_L = L.copy()
    
    new_L[:k] = L[-k:]
    new_L[-k:] = L[:k]
    return (new_L, k)
    ### Replace with your own code (end)   ###