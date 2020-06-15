"""AAABBBC --> 3A2B1C """


def string_compr(str):
	d = { }
	output = ''

	for ch in str:
		if ch in d:
			d[ch] += 1
		else:
			d[ch] = 1

	for k, v in d.items():
		output = output+(k + str(v))

	return output

print(string_compr("AAABBBC"))