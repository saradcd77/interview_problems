"""LeetCode Easy Problem"""
def romanToInt(s:str):
    rom_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    output = 0

    for i in range(len(s)):
        current_char = s[i]
        if i < len(s) - 1:
            next_char = s[i + 1]
            if rom_dict[current_char] < rom_dict[next_char]:
                output -= rom_dict[current_char]
            else:
                output += rom_dict[current_char]
        else:
            output += rom_dict[current_char]
    return output

print(romanToInt('XX'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))