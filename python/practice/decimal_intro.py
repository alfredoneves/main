#!/usr/bin/python3

from decimal import Decimal	# library to work with high precision like 20 zeros after the point

# example of amount in 10 years with interest of 5%
principal = Decimal('1000.00')
rate = Decimal('0.05')
years = 10

amount = principal * (1 + rate) ** years
print(amount)

print('---' * 10)

# example of restaurant check with tax of 6.25% and bill of $37.45
tax = Decimal('0.0625')
bill = Decimal('37.45')

total = bill * (1 + tax)
print(f'{total:.2f}')
