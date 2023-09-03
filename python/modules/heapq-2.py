#!/urs/bin/python3

import heapq

# Creating an empty max-heap (by negating values)
max_heap = []

# Inserting elements into the max-heap (negate values)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)

print(f'heap: {max_heap}')

# Retrieving the maximum element (by negating it back)
max_val = -heapq.heappop(max_heap)

print(max_val)  # Output: 3
