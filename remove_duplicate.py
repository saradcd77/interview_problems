def removeDuplicate(nums: int):
	i = 0
	for num in nums:
		if num != nums[i]:
		i += 1
        nums[i] = num
    return i + 1