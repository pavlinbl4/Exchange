def call(n):
    print(int(n))
    if n == 1:
        return n
    elif n%2 == 0:
        return call(n/2)
    else:
        return call(n*3 + 1)
call(17)
