#!/usr/bin/env python3
from sys import stdin

def handleValue(x, y, i):
	if i % x == 0 and i % y == 0:
		return "FizzBuzz"
	elif i % x == 0:
		return "Fizz"
	elif i % y == 0:
		return "Buzz"
	else:
		return str(i)


if __name__ == '__main__':
	x, y, n = map(int, stdin.readline().strip().split(" "))
	for i in range(1, n+1):
		print(handleValue(x, y, i))