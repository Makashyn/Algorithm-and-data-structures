# search min and max elements in array 
# comlexity is 3n/2



def search(array):
	min = array[0] if array[0] < array[1] else array[1]
	max = array[0] if array[0] > array[1] else array[0]
	for i in range(2, len(array), 2):
		if array[i + 1] >= array[i]:
			if array[i + 1] > max:
				max = array[i + 1]
			if array[i] < min:
				min = array[i]
		else:
			if array[i] > max:
				max = array[i]
			if array[i + 1] < min:
				min = array[i + 1]	


	return min, max 

if __name__ == '__main__':
	array = [3 ,1, 0, 10, 5, 4,2,5,-31,100]
	min, max = search(array)
	print(min, max) 