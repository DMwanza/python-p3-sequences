#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    
    # Check if length is 0 or negative
    if length <= 0:
        print("Length should be a positive integer.")
        return
    
    # Add the first two numbers to the sequence
    fibonacci.append(0)
    if length > 1:
        fibonacci.append(1)
    
    # Generate the Fibonacci sequence
    for i in range(2, length):
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)
    
    # Print the Fibonacci sequence
    for number in fibonacci:
        print(number, end=", ")