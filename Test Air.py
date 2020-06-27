n = 3
n = int(input())
lst = [x for x in range(1,n+1)]
for x in range(n-1):
    z = lst.pop(0)
    print("Z =", z)
    lst.append(z)
    print(lst)
    for y in range(n):
        d = lst.pop()
        lst.insert(0,d)
        print(*lst)





