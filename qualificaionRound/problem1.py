for i in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    counter = 1
    for j in range(n):
        if counter <= arr[j]:
            counter += 1
    
    print("Case #%d: %d" % (i + 1, counter - 1))