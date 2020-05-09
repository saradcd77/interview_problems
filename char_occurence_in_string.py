"""Find the number of characters in given string from user's input"""

given_string = input("Please enter the string: ")

def char_count(given_string):
    char_dict = {}

    for char in given_string:
        char_dict[char] = char_dict.get(char,0)+1

    for k,v in char_dict.items():
        print("{} occurs {} times".format(k,v))

char_count(given_string)





