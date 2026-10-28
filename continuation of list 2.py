Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#PYTHON LIST
#SORT()
numbers = [40,10,30,20]
numbers.sort()
print(numbers)
[10, 20, 30, 40]

numbers = [40,10,30,20,50,70,60,80]
numbers.sort()
print(numbers)
[10, 20, 30, 40, 50, 60, 70, 80]

#REVERSE()
fruits = ['apple','mango','banana','grapes']
fruits.reverse()
>>> print(fruits)
['grapes', 'banana', 'mango', 'apple']
>>> numbers = [40,10,30,20,50,70,60,80]
>>> numbers.reverse()
>>> print(numbers)
[80, 60, 70, 50, 20, 30, 10, 40]
>>> 
>>> #COPY()
>>> fruits = ['apple','mango','banana','grapes']
>>> fruits.copy()
['apple', 'mango', 'banana', 'grapes']
>>> print(fruits)
['apple', 'mango', 'banana', 'grapes']
>>> numbers = [40,10,30,20,50,70,60,80]
>>> numbers.copy()
[40, 10, 30, 20, 50, 70, 60, 80]
>>> 
>>> #EXTEND()
>>> fruits = ['apple','mango','banana','grapes']
>>> more_fruits = ['litchi', 'dragon']
>>> fruits.extend(more_fruits)
>>> print(fruits)
['apple', 'mango', 'banana', 'grapes', 'litchi', 'dragon']
>>> numbers = [40,10,30,20]
>>> add = [100,200]
>>> numbers.extend(add)
>>> print(numbers)
[40, 10, 30, 20, 100, 200]
