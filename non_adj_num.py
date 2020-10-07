import sys

def largest_non_adj_sum(arr):
	prev, larg = 0, 0

	for amt in arr:
		print("amount: {}; prev: {}; largest: {}".format(amount, previous, largest))
		prev, larg = larg, max(larg, prev+amount)
		print("new_prev: {}; new_larg:{}".format(previous, largest))
	return larg


print(largest_non_adj_sum([2, 4, 6, 8]))
print(largest_non_adj_sum([5, 1, 1, 5]))