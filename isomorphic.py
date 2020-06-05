"""" Check if given two strings are isomorphic """

def isIsomorphic(str1 ,str2):
    dict1 = {}; dict2 = {}

    for i in range(len(str1)):
        k, t = str1[i], str2[i]

        if k not in dict1:
            dict1[k] = t

        if t not in dict2:
            dict2[t] = k

        if dict1[k] != t or dict2[t] != k:
            return False

    return True

print(isIsomorphic('xxy','aaa'))
print(isIsomorphic('paper','title'))
print(isIsomorphic('foo','baar'))