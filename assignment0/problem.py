# Zach Domke
# CIS_315
# 4/8/18

import sys

# adds 2 given numbers
def add(x, y) -> int:
	return x + y

# multiplies 2 given numbers
def multiply(x, y) -> int:
	return x * y

# takes in how many lines are tested and then adds and multiplies that many times
def driver():
	n = int(input())
	for i in range(n):
		inData = input().strip().split()
		x = int(inData[0])
		y = int(inData[1])
		addOut = add(x, y)
		multiplyOut = multiply(x, y)
		print(addOut, multiplyOut)

# allows python3 code to run as python
if __name__ == "__main__":
	driver()
