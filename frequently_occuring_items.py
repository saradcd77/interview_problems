# Find out the maximum characters occuring in a list or an array?
# Time Complexity -> O(n) -> Has to iterate through one item at a time in an array

def freq_occuring(array):
	max_item = 0
	max_count = 0
	d = {}

	for ch in array:
		if ch not in d:
			d[ch] = 1
		else:
			d[ch] += 1

	for ch in d:
		if d[ch] > max_count:
			max_count = d[ch]
			max_item = ch

	return max_item


print(freq_occuring('aabc'))
print(freq_occuring('aabbbc'))
print(freq_occuring('aabbbccc'))