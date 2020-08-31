def get_product(array):
	cum_product = 1
	rt_prod_array = array()

	for num in array:
		cum_product *= num
		rt_prod_array.append(cum_product)

	cum_product = 1
	left_prod_array = []

	for num in array[::-1]:
		cum_product *= num
		left_prod_array.append(cum_product)

	left_prod_array = left_prod_array[::-1]

	output_array = []
	for i in range(len(array)):
		num = None
		if i == 0:
			num = left_prod_array[i+1]
		elif i == len(array) - 1:
			num = rt_prod_array[i-1]
		else:
			num = rt_prod_array[i-1] * left_prod_array[i+1]
		output_array.append(num)


	return output_array

print(get_product([1,2,3,4,5]))
