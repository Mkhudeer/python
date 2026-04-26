

# 1 Magic 8-ball

#Write A magic 8-ball, when you ask a question, the program provides a random answer from a list. The code below contains a list of possible answers. Create a magic 8-ball program that asks a question, then gives a random answer.

#answers = [ "It is certain", "It is decidedly so", "Without a \
#doubt", "Yes, definitely", "You may rely on it", "As I see it, \
#yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
#"Reply hazy try again", "Ask again later", "Better not tell you \
#now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
#count on it", "My reply is no", "My sources say no", "Outlook \
 #not so good", "Very doubtful" ]

import random

questions = [
"Will I pass the exam?",
"Will I get a job?",
"Is today my lucky day?",
"Will I travel soon?",
"Will I become rich?"
]

answers = [
"It is certain", "It is decidedly so", "Without a doubt",
"Yes, definitely", "You may rely on it", "As I see it, yes",
"Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later",
"Better not tell you now", "Cannot predict now",
"Concentrate and ask again", "Don't count on it",
"My reply is no", "My sources say no",
"Outlook not so good", "Very doubtful"
]

question = random.choice(questions)

answer = random.choice(answers)

print(" Question:", question)
print(" Answer:", answer)

# 2 FIFO
#A first-in-first-out (FIFO) structure, also called a “queue,” is a list 
# that gets new elements added at the end, while elements from the front are 
# removed and processed. 
# Write a program that processes a queue. In a loop, ask the user for input.
#  If the user just presses the Enter key, the program ends. 
# If the user enters anything else, except for a single question mark (?),
#  the program considers what the user entered a new element and appends it to the queue.
#  If the user enters a single question mark, the program pops the first element from 
# the queue and displays it. 
#You have to take into account that the user might type a question mark even if 
# the queue is empty.
queue = []
queue.append("A")
queue.append("B")
print(queue.pop(0))


#3. Fibonacci
#Write a Fibonacci sequence using Python. 
# A Fibonacci sequence is an infinite series of numbers
#  that are created by adding the last two numbers in the series. 
# A series would start with the numbers 1 and 1 in place,
#  followed by 1 (0+1). 2(1+1), 3(1+2), 5(3+2), etc.. 

#0 1 1 2 3 5 8 13 21 ....

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()


# 4 Counting
def counting_number(sub, text):
    return text.count(sub), text.replace(sub, "")

print(counting_number("an", "banan"))


# 5 Palindrome
def is_palindrome(text):
    return text == text[::-1]


word = input("Enter a word: ")

if is_palindrome(word):
    print("Yes")
else:
    print("No")


# 6 Largest
print(max([10, 20, 4]))
print(max([20, 10, 20, 4, 100]))
