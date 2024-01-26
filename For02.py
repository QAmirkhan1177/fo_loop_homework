def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    l=[]
    for i in range(n):
        l.append(str(i))
    return ','.join(l)
print(main(5))