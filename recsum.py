def recsum(n):
    if n==1:
        return 1
    else:
        return recsum(n-1)+n
