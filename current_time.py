"""
This module tell us the current time.
"""
import datetime
time  = datetime.datetime.now().time()
if __name__ == "__main__":
    print (time)
else:
    print("Since this module is imported to another module I wont print it")
    
