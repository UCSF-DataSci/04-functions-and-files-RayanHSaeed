#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
import argparse
from fibonnaci import fibonacci

def is_prime(n):
    #Check if a number is prime.
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_fibonacci(limit):
    # Generate Fibonacci numbers up to the limit
    fibonacci_numbers = fibonacci(limit)
    
	#Find the largest prime Fibonacci number less than the limit:
    return max((num for num in fibonacci(limit) if is_prime(num)), default=None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number below a limit.")
    parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers")
    
    args = parser.parse_args()

    # Find the largest prime Fibonacci number
    result = largest_prime_fibonacci(args.limit)
    
    if result:
        print(f"The largest prime Fibonacci number less than {args.limit} is {result}.")
    else:
        print(f"There is no prime Fibonacci number less than {args.limit}.")