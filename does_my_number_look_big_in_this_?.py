def narcissistic( value ):
    ints = map (int, str(value))
    sum = 0;
    for n in ints:
        sum += n**len(ints)  
    if sum == value:
        return True;
    return False
        
