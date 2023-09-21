#!/usr/bin/python3


def max_heapify(a, heap_size, i):
	"""
	This function swaps 2 elements in a list to order according to a heap
	"""
	l = 2*i	# left
	r = 2*i + 1	# right
	
	largest = i
	
	if l < heap_size and a[l] > a[i]:
		largest = l
	
	if r < heap_size and a[r] > a[largest]:
		largest = r
	
	if largest != i:
		# swap elements
		a[i], a[largest] = a[largest], a[i]
		max_heapify(a, heap_size, largest)
		
		
def build_max_heap(a):
	heap_size = len(a)
	
	for i in range(heap_size//2, 0, -1):
		max_heapify(a, heap_size, i)
		

def main(a):
	build_max_heap(a)
	print(f"heap: {a[1:]}")


a = [None, 0, 2, 4, 5, 6, 1, 8, 9, 10, 15, 20, 13, 7]
main(a)
