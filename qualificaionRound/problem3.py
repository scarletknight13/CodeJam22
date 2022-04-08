for i in range(int(input())):
    first, second, third, fourth = int(1e7), int(1e7), int(1e7),int(1e7)
    for j in range(3):
        arr = [int(x) for x in input().split()]
        first = min(arr[0], first)
        second = min(arr[1], second)
        third = min(arr[2], third)
        fourth = min(arr[3], fourth)

    sum = first + second + third + fourth
    print('\nsum; ', sum)
    print("nums: " , first, second, third, fourth)
    over = sum - int(1e6)
    print('over ', over)
    if sum < 1e6:
        print('Case #%d: %s' % (i + 1, 'IMPOSSIBLE'))
    else:
        temp = min(over, first)
        first -= temp
        over -= temp            
        temp = min(over, second)
        second -= temp
        over -= temp 
        temp = min(over,third)
        third -= temp
        over -= temp
        temp = min(over, fourth)
        fourth -= temp
        over -= temp             
        print('Case #%d: %d %d %d %d' % (i + 1, first, second, third, fourth))



