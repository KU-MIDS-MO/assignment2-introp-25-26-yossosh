def breakdown_time(seconds):
    ### Replace with your own code (begin) ###
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    
    time = {}
    for unit in [3600, 60, 1]:
        breakdown = seconds // unit
        if breakdown > 0:
            time[unit] = breakdown
        seconds %= unit
    
    return time
    ### Replace with your own code (end)   ###