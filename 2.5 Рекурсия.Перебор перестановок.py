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
generate(3)










# def change(lst, n, m): # функция производящая перестановку всех элементов списка кроме первого
#     if n == 1:
#             return
#     print(*lst)
#     d = lst.pop(1)
#     lst.insert(n, d)
#     change(lst, n - 1, m)
#     return n

# def change1(lst, n, m):
#     if n == 1:
#         return
#
# def loto(n): # функция создает список из n элементов и создает переменную m
#     lst = [x for x in range(1, n + 1)]
#     m = n
#     # change(lst, n, m)
#     change1(lst,n,m)
# n = 5
# loto(n)
