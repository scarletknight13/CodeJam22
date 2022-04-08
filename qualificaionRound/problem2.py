for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    s = '+-' * m + '+'
    t = '|.' * m + '|'
    sf = '..' + '+-' * (m - 1) + '+'
    tf = '..' + '|.' * (m - 1) + '|'
    mat = []
    print('Case #%d: ' % (i + 1))
    for j in range(n):
        if(j == 0):
            mat.append(sf)
            mat.append(tf)
        else:
            mat.append(s)
            mat.append(t)
    mat.append(s)
    for j in mat:
        print(j)
        