"""
Implementing the linear search algorithm in Python using a list of numbers
"""
l = [5,8,1,3,2,6,9,0,1]
search_for = 9
result = -1

for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break
print (search_for ,'is in ',i+1,'th positon')
