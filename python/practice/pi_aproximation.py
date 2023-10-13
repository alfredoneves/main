#!/usr/bin/python3

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
pi = 0
denominator = 1

for i in range(10794):
    if i % 2 == 0:
        pi += 4 / denominator
    else:
        pi -= 4 / denominator
    denominator += 2

    print(f'{i}) π = {pi}')
