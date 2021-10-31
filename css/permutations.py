def findPermutation(n, p, q):
    r = []
    for i in range(n-1):
        if i>0:
            n = q[i]
            k = p.index(n)
            r.append(k)
    for s in p:
        if s not in r:
            r[0] = s
    return r

print (findPermutation(3, [3, 1, 2], [2, 1, 3]))
