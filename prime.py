""" Building a function to know if the given number is prime or not"""
def is_prime(x):
    for i in range(2, int(x/2)):
        if (x % i) == 0:
            return False
    
    return True

    