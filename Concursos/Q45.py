L = [0,1,1,2,3]
for k in range(4, -4, -1):
    print( L[k] + L[k % len(L)] )