""" Given a non-empty array of digits representing a non-negative integer, plus one to integer
    The digits are stored such that the most significant digit is at the head of the list,
    and each element in the array contain a single digit. """

# Leet Code Easy Problem

def plusone(digits):
    num = ""
    output = []

    for i in digits:
        num = num + str(i)
    num = int(num)
    num += 1
    num = str(num)
    for i in num:
        output.append(int(i))
    return output


print(plusone([1,2,3]))
print(plusone([9,9]))  
print(plusone([9]))