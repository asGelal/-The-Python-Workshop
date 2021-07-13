"""
Creating the Fibonacci_iterative function that returns the nth value in the Fibonacci sequnce
"""
global fiboNumPre, fiboNumRec,fiboNumNew
def fibonacci_iterative(x):
    fiboNumPre = 0
    fiboNumRec = 1
    for i in range(2,x):
        fiboNumNew = fiboNumPre + fiboNumRec 
        fiboNumPre = fiboNumRec
        fiboNumRec = fiboNumNew
    return fiboNumNew

        
        