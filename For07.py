def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    
    n=0
    for i in range(0,N,2):
        n+=i
    return n 
print(main(10))