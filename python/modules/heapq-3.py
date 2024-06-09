#!/usr/bin/python3

import heapq

# creating an empty heap
heap = []

# inserting elements in the min-heap (minimun element in the root)
# the heappush function assures that the heap property is maintained
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
heapq.heappush(heap, 7)

print(f'heap created: {heap}')
