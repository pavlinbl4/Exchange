def is_power(n):
    if n == 1:
        return True
    if n%2 == 0:
        return is_power(n/2)
    else:
        return False

print((is_power(1048576)))

