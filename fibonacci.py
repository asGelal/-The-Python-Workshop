"""Fibonacci using recursive"""
prev = 0
rec  = 1
def fibonacci_recursive(x):
    global prev , rec
    current = prev + rec
    prev = rec
    rec = current
    if x-1 <= 2:
        #print (current)
        return current
        
    
    else:
        #print(x-1 ,'>>',current)
        
        return fibonacci_recursive(x-1) 
#print (f"{prev} and {rec}")   
fibo = fibonacci_recursive(7)
print (f"{prev} and {rec} and {current}") 

print(f"{fibo}")
