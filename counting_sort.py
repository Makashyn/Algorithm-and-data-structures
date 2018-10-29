def counting_sort(base_array, result_array, max_element):
	repetition = [0] * (max_element + 1)
	for i in range(0, len(base_array)):
		repetition[base_array[i]] += 1
	for i in range(1, len(repetition)):
		repetition[i] += repetition[i - 1]
	for i in range(len(base_array) - 1, -1, -1):
		result_array[repetition[base_array[i]] - 1] = base_array[i]
		repetition[base_array[i]] -= 1
	return result_array

if __name__ == '__main__':
	array = [0, 1, 5, 3, 2, 3, 1, 2, 2, 2]

	max = array[0]
	for i in range(1, len(array)):
		if array[i] > max:
			max = array[i]
	print(array)
	print(counting_sort(array,[0] * len(array), max))