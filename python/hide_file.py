#!/usr/bin/python3

import ctypes
import sys
import os

atribute = 0x02

try:
	file_name = sys.argv[1]
	system = sys.argv[2]
except:
	print("Usage: ./hide_file.py file [win|lin]")
	sys.exit()
	
def hide_file(file_name, system):
	try:
		if system == "win":
			result = ctypes.windll.kernel32.SetFileAttributesW(file_name, atribute)
		elif system == "lin":
			os.system(f"mv {file_name} .{file_name}")
		else:
			print("chose between windows (win) and linux (lin)")
	except Exception as error:
		print(error)
		
hide_file(file_name, system)

