
def aps(arr,depth):
    if len(arr) <= 0:
        return
    ans = 0
    for i in arr:
        if type(i) is int:
            ans += i
        elif type(i) is list:
            ans += aps(i,depth+1)
    return ans * depth

print(aps([1, 2, [2,3], 6, [[2,3], 1], 7],1))