def parent(i):
	return int(abs(i/2))

def left(i):
	return int(abs(2*i))

def right(i):
	return int(abs(2*i + 1))

def maxHeapify(array, item):
	leftItem = left(item)
	rightItem = right(item)
	print(rightItem, leftItem, len(array))
	if leftItem <= len(array) and array[leftItem] > array[item]:
		largest = leftItem
	else:
		largest = item

	if rightItem < len(array) and array[rightItem] > array[largest]:
		largest = rightItem
	if largest != item: 
		array[item], array[largest] = array[largest], array[item]
		maxHeapify(array, largest)

def BuildMaxHeap(array):
	for i in range(int(len(array) / 2), -1, -1):
		maxHeapify(array, i)

if __name__ == '__main__':
	array = [14,12,19,1,10,4,5,2,3]
	BuildMaxHeap(array)
	print(array)