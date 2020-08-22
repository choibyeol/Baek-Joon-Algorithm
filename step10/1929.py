def findN(N):
    divisor = 1
    pnum = 0
    for j in range(N):
        if(N % divisor == 0):
            pnum += 1
        divisor += 1
    if(pnum == 2):
        return 1

M, N = map(int, input().split())
for i in range(M, N+1):
    if(findN(i) == 1):
        print(i)

