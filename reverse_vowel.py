""" Swaps the position of the vowel"""

def vowelReverse(str):
	vowels = {'a','e','i','o','u'}

	s = list(str)
	left, right = 0, len(s)-1

	while left < right:
		if (s[left] in vowels) and (s[right] in vowels):
			s[left], s[right] = s[right], s[left]

		else:
			if s[left] in vowels:
				left -= 1

			elif s[right] in vowels:
				right += 1

		left += 1
		right -= 1

	return "".join(s)

			




print(vowelReverse('Hello'))
print(vowelReverse('Hire'))
print(vowelReverse('Harry'))
print(vowelReverse('aeiou'))
