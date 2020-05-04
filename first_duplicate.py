def firstDuplicate(a):
    dups = {}
    for i in a:
        if dups.get(i):
            return i
        else:
            dups[i] = 1
    return -1



print(firstDuplicate([7,4,5,6,4,6,3]))
print(firstDuplicate([2, 1, 3, 5, 3, 2]))
print(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])) # 6 not 4 since another 6 appears before 4