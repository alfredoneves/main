#!/usr/bin/python3


def slope(start, end):
	"""
		Calculates the slope of a line(describes it's direction and steepness)
		Exp: slope((1,1), (4,5)) = 1.33
	"""
	
	delta_x = start[0] - end[0]
	delta_y = start[1] - end[1]
	return delta_y / delta_x
	
	
print(slope((1,1), (4,5)))
