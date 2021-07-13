"""
Calculating Factorial with Iteration 
"""
def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i + 1 
    return result

""" 
Calculating Factorial with recursion
"""
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
        
