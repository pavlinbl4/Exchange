n = int(input())
print(n//3600%24,str(n//600%6) + str(n//60%10),str(n%3600%60//6) +str(n%3600%60%6),sep=":")