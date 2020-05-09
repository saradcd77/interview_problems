"""Find the sum of numbers in alphanumeric string"""

def find_numbers(str):
    digits = []
    alpha = []
    sum = 0
    
    for nums in str:
        if nums.isalpha():
            alpha.append(nums)
        else:
            digits.append(nums)
    output = "".join(digits)

    for i in output:
        sum += int(i)
    return sum


print(find_numbers('adfadsfasdf23245'))
print(find_numbers('adasdf22245fadsfasdf23245'))