#!/bin/python3

def fizzBuzz(n):
	for i in range(1, n+1):
		if i % 3 == 0:
			print("Tiga", end="")
		if i % 5 == 0:
			print("Lima", end="")
		if i % 3 != 0 and i % 5 != 0:
			print(i, end="")
		print()

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
