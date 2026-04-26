#Algorithm Problems


#Write a program that will add all the values between 200 and 2700 (inclusively) 
# that are divisible by 3 or 5, but not both 3 and 5.
#  For this algorithm, write the pseudocode before your Python code.

# Pseudocode:

# 1- Initialize a variable total with value 0
# 2- Loop from 200 to 2700 (inclusive)
# 3- For each number:
#    If it is divisible by 3 OR 5
#    BUT NOT both
#    Add it to total
# 4- Print the result

total = 0

for i in range(200, 2701):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        total += i

print("Result:", total)






#Define a function rFib(num) that takes a positive integer as input. 
# Returns the Nth Fibonacci number, with n=1 representing the start of the sequence.
#  Solve this recursively.
#  For this algorithm, write the pseudocode before your Python code.

# Pseudocode:
# 1- Define a function rFib(n)
# 2- If n == 1, return 0
# 3- If n == 2, return 1
# 4- Otherwise:
#    Return rFib(n-1) + rFib(n-2)
# 5- Call the function and print the result

def rFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return rFib(n - 1) + rFib(n - 2)

print("Fib:", rFib(6))




#Write a function that finds and returns the longest word from a given string. 
# longest_word("The quick brown fox jumped over the lazy dog").
#  For this algorithm, write the pseudocode before your Python code.

# Pseudocode:
# 1- Take a sentence as input
# 2- Split the sentence into words
# 3- Initialize a variable longest as empty string
# 4- Loop through each word:
#    If the length of the word is greater than longest
#    Update longest
# 5- Return the longest word


def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print("Longest word:", longest_word("The quick brown fox jumped over the lazy dog"))

#Declare a function is_palindrome(str) that takes a string as input.
#  Return true if the given string is a palindrome. Otherwise, return false.
#  A palindrome is a word or sentence that's spelled the same way both forward and
#  backward, ignoring punctuation, case, and spacing. For this algorithm, 
# build the complete T diagram for the word ‘kayak’.

def is_palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

print("Is palindrome:", is_palindrome("kayak"))

# T diagram for 'kayak':

#| Step      | Variable   | Value   |
#| --------- | ---------- | ------- |
#| Input     | s          | "kayak" |
#| Lowercase | s          | "kayak" |
#| Cleaned   | s          | "kayak" |
#| Reversed  | s[::-1]    | "kayak" |
#| Result    | comparison | True    |




#Declare a function remove_negative(arr) that takes an array as input.
#  Given an array X, for example [1,-2,4,1], remove the negative numbers,
#  so that the output becomes: [1,4,1]. For this algorithm, 
# build the complete T diagram for the array [1,-2,3].

def remove_negative(arr):
    result = []

    for num in arr:
        if num >= 0:
            result.append(num)

    return result

print("Filtered:", remove_negative([1, -2, 3]))

# T diagram for [1, -2, 3]:

#| Step  | num | result |
#| ----- | --- | ------ |
#| Start | -   | []     |
#| 1     | 1   | [1]    |
#| 2     | -2  | [1]    |
#| 3     | 3   | [1, 3] |
#| Final | -   | [1, 3] |

