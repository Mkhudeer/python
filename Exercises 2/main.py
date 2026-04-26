# Question 1
# 1- Write a program that checks if a number is positive, negative, or zero.
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Question 2
# 2- Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)


# Question 3
 # 3- Use a while loop to print numbers from 10 down to 1
i = 10
while i >= 1:
    print(i)
    i -= 1


# Question 4
# 4- Write a program that prints all even numbers from 1 to 20 using range().
for i in range(2, 21, 2):
    print(i)


# Question 5
# 5- Ask the user for a number. 
#If it’s greater than 100, print "Big number!", otherwise print "Small number!".
number = int(input("Enter a number: "))

if number > 100:
    print("Big number!")
else:
    print("Small number!")