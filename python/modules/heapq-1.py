#!/usr/bin/python3

import heapq

# creating an empty heap
heap = []

# inserting elements in the min-heap (minimun element in the root)
# the heappush function assures that the heap property is maintained
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(f'heap created: {heap}')

# extracting and removing the minimun value of the min-heap
min_value = heapq.heappop(heap)
print(f'minimun value of heap: {min_value}')
print(f'new heap: {heap}')
