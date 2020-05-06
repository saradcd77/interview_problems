""" Given a list of numbers and a number k, return whether any two numbers from the list 
add up to k."""

def isSum(given_list, k):
    seen_nums = set()
    
    for num in given_list:
    	if k - num in seen_nums:
    		return True
    	seen_nums.add(num)
    
    return False

print(isSum([1,2,3,4],5))
print(isSum([1,2,3,4],8))