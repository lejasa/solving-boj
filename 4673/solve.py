# https://clolee.tistory.com/36
numList = []

def selfNum(k):
    for n in range(k):
        n = n + sum(list(map(int, str(n))))
        numList.append(n)
        if n >= k: break
        else : continue

print(selfNum(10000))
for i in range(1,10000):
    if i in numList: continue
    else: print(i)

