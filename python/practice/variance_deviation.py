#!/usr/bin/python3

import statistics

group_a = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
group_b = [6, 1, 5, 1, 2, 3, 6, 4, 5, 1]

print(f"group a: {group_a} --> variance: {statistics.pvariance(group_a)}")
print(f"group b: {group_b} --> variance: {statistics.pvariance(group_b)}")

print(f"group a standard deviation: {statistics.pstdev(group_a)}")
print(f"group b standard deviation: {statistics.pstdev(group_b)}")
