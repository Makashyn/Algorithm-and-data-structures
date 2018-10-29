def inclusion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i - 1
		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key


if __name__ == '__main__':
	array = [1, 5, 5, 2, 4, 11, 3]
	inclusion_sort(array)
	print(array)



