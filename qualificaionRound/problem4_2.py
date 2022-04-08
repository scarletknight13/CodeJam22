import itertools
vis = []
def dfs(node, dic, indexVal, vis):
    # print(node)
    arr = []
    vis[node] = True
    ans = indexVal[node]
    for i in dic[node]:
        if not vis[i] and i != 0:
            ans = max(dfs(i, dic, indexVal, vis), ans) 
            
    return ans
for i in range(int(input())):
    n = int(input())
    f = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    dic = {}
    s = set(p)
    indexVal = {}
    indexVal[0] = 0
    for j, val in enumerate(f):
        indexVal[j + 1] = val
    for j in range(n):
        if j == 0:
            dic[1] = [0]
        else:
            if j + 1 in dic:
                dic[j + 1].append(p[j])
            else:
                dic[j + 1] = [p[j]]
    # print(dic)
    leaves = [x for x in range(1, n+1) if x not in s]
    ans = 0
    perms = list(itertools.permutations(leaves))
    for j in range(len(perms)):
        vis = [False for x in range(n+1)]
        res = 0
        for k in range(len(perms[j])):
            res += dfs(perms[j][k], dic, indexVal, vis)
        ans = max(res, ans)
    print('Case #%d: %d' % (i + 1, ans))
