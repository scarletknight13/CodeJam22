def dfs(node, dic, indexVal):
    # print(node)
    arr = []
    if node in dic:
        for i in dic[node]:
            temp = dfs(i, dic, indexVal)
            # print(temp)
            arr.append(temp)

    arr.sort()
    # print(node, arr)
    if arr:
        arr[0] = max(indexVal[node],  arr[0])
    else:
        arr.append(indexVal[node])

    return sum(arr)

for i in range(int(input())):
    n = int(input())
    f = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    dic = {}
    indexVal = {}
    indexVal[0] = 0
    for j, val in enumerate(f):
        indexVal[j + 1] = val
    for j in range(n):
        if j == 0:
            dic[0] = [1]
        else:
            if p[j] in dic:
                dic[p[j]].append(j + 1)
            else:
                dic[p[j]] = [j + 1]
    # print(dic)
    ans = dfs(0, dic, indexVal)
    print('Case #%d: %d' % (i + 1, ans))
