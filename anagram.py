
""" Finds if two given strings are anagram or not (LeetCode Easy Problem) """

def isAnagram(str1, str2):
	dict_str = {}

	for chars in str1:
		if chars not in dict_str:
			dict_str[chars] = 1
		else:
			dict_str[chars] += 1

	for chars in str2:
		if chars not in dict_str:
			dict_str[chars] = 1
		else:
			dict_str[chars] -= 1

	for k,v in dict_str.items():
		if dict_str[k] != 0:
			return False

	return True


print(isAnagram('triangle', 'integral'))
print(isAnagram('listen', 'silent'))
print(isAnagram('hello','ollew'))


