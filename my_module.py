"""Ex.34 Writing and Ececuting Our First Script 
   Creatingthe my_module.py
    This script computes the sum of factorial of the list of numbers.
"""
import math
def compute(numbers):
    return([math.factorial(n) for n in numbers])