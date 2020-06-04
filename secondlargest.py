
""" Find second largest number from the given array of numbers  """
def second_largest(arr):
	max = None
	scnd_max = None

	for nums in arr:
		if max == None:
			max = nums
		elif nums > max:
			scnd_max = max
			max = nums
		elif scnd_max == None:
			scnd_max = nums
		elif nums > scnd_max:
			scnd_max = nums

	return scnd_max



print(second_largest([1,2,3,4,5]))
print(second_largest([7,6,1,4,5]))
print(second_largest([-7,-6,-1,-4,-5]))