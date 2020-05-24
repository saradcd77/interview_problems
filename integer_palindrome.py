
# Leetcode Easy problem
# Note: Palindrome is a condition when given integer reads same forward and backward

""" Find whether an integer is a palindrome or not """
def isPalindrome(x):
    output = ""

    for i in str(x):
        output = i + output

    if output == str(x):
        return True
    else:
        return False

print(isPalindrome(121))
print(isPalindrome(321))
print(isPalindrome(-121))
print(isPalindrome(10))