""" Find maximum occurence of particular string of urls from a given text file. 
The function reads off a given text file with strings of url and parses the first 25 characters
to include the full url from including both https and .com at the end """


def findCommonText(file):
	char_count = {}
	max_char = 0
	max_count = 0

	with open(file, 'r') as stream:
		for line in stream:
			str = line[0:25]

			if str not in char_count:
				char_count[str] = 1
			else:
				char_count[str] += 1

		for ch in char_count:
			if char_count[ch] > max_count:
				max_char = ch

		return max_char


print(findCommonText('urls.text'))