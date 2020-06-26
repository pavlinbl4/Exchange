def find(number,a):
    flag = False
    for x in a:
        if number == x:
            flag = True
            break
    return flag

def generate(n:int, m:int = -1, prefix = None):
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n+1):
        if find(number,prefix):
            continue
        prefix.append(number)
        generate(n, m -1, prefix)
        prefix.pop()
generate(int(input()))