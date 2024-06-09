from statistics import *

temperatures = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5, 20.2]
print(f'Registered temperatures: {temperatures}')
print(f'Mean: {mean(temperatures):.2f}')
print(f'Median: {median(temperatures):.2f}')
print(f'Mode: {mode(temperatures):.2f}')
print(sorted(temperatures))
