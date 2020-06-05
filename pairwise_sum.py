""" Find all the pairwise sum from the given array that matches the corresponding given value """

def pairSum(k,v):
    seen = set()
    output = set()

    if len(k) < 2:
        return k

    for i in k:
        n = v-i
        if n not in seen:
            seen.add(i)
        else:
            output.add((min(i,n), max(i,n)))
    return (output)

print(pairSum([1,2,3,4],4))
print(pairSum([1,2,3,4],5))