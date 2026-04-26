# Exercise 1
#Exercise 1: Accessing Tuple Elements
#Create a tuple with the values ("apple", "banana", "cherry", "date").

#Print the first item.
#Print the last item using a negative index.
#Print the second and third items using slicing.

fruits = ("apple", "banana", "cherry", "date")
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

# Exercise 2
#Exercise 2: Tuple Operations
#Create two tuples:
#Combine them into a new tuple.
#Multiply tuple1 by 2 and print the result.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
print(tuple1 * 2)

# Exercise 3
#Exercise 3: Tuple Methods & Unpacking Create a 
# tuple with the values (10, 20, 30, 40, 50).

#Use tuple unpacking to assign the first two values to 
# variables a and b, and the rest to a variable rest.
#Print a, b, and the rest.
#Count how many times 20 appears in the tuple.
#Find the index of 40 in the tuple.

numbers = (10, 20, 30, 40, 50)
a, b, *rest = numbers
print(a, b, rest)
print(numbers.count(20))
print(numbers.index(40))