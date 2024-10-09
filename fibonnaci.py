#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def fibonacci(limit):
    fibonacci_numbers = []
	a, b = 0, 1
	while a <limit: 
		fibonacci_numbers.append(a)
		a, b = b, a + b
    return fibonacci_numbers

def writingfile(fibonacci_numbers, filename): 
	try: 
		with open(filename, 'w') as f: 
			for number in fibonacci_numbers: 
				f.write(f"{number}")
		print(f"Wrote out Fibonacci numbers to {filename}")
	except IOError as e: 
		print(f"Error")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers up to limit")
	parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers")
	parser.add_argument("output", help="Output file with Fibonacci numbers")

	args = parser.parse_args()

	fibonacci_numbers = fibonacci(args.limit)

	writingfile(fibonacci_numbers, args.output)