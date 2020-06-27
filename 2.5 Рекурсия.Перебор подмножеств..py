def podm(mn,n):
    if n == 0:

        print("END")
    else:
        print(mn)
        mn.pop(n-1)
        podm(mn,n-1)





    





# mn = input().split(" ") # создаю список из вводимых данных
# mn.sort()
mn = [ 1,2,3,4]
n = len(mn)
#print(mn)
podm(mn,n)


