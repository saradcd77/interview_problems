"""" Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

def is_char(code):
	return 0 if code > 26 or code < 1 else 1


def message_count(code):
	str_code = str(code)
	if len(str_code) == 1:
		count = 1
	elif len(str_code) == 2:
		count = 1 + is_char(code)
	else:
		count = message_count(int(str_code[1:]))
		if is_char(int(str_code[:2])):
			count += message_count(int(str_codep[2:]))

	return count

assert message_count(11) == 2
assert message_count(1111) == 5
assert message_count(1311) == 4
