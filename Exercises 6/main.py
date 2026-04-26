# Exercise 1: List → Dictionary

#1. Building Dictionaries from a List
#The code below contains a list of words. 
# Build a dictionary that contains all these words as keys, 
# and their quantities as values. Print the words with their quantities.

wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

wordlist = [
"apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"
]

word_count = {}

for word in wordlist:
    word_count[word] = word_count.get(word, 0) + 1

print("Exercise 1 result:")
print(word_count)


# Exercise 2: String → Dictionary

#2. Building Dictionaries from a String
#The code block below contains a string that is a list of words, separated by commas. 
# Build a dictionary that contains all these words as keys, 
# and how often they occur as values. Then print the words with their quantities.

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

words = text.split(",")

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nExercise 2 result:")
print(word_count)


# Exercise 3: Translation

#3. Translating
#The code block below contains a very small dictionary that contains the translations of English words to Dutch. Write a program that uses this dictionary to create a word-for-word translation of the given sentence. A word for which you cannot find a translation, you can leave “as is.” The dictionary is supposed to be used case-insensitively, but your translation may consist of all lower case words. It is nice if you leave punctuation in the translation, but if you take it out, that is acceptable (as leaving punctuation in is quite a bit of work, and does not really have anything to do with dictionaries – besides, leaving punctuation in is much easier to do once you have learned about regular expressions).

#english_dutch = { "last":"laatst", "week":"week", "the":"de",
#"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
#"zaag", "first":"eerst", "performance":"optreden", "of":"van",
#"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
#"one":"een", "world":"wereld", "leading":"leidend", "modern":
#"modern", "composer":"componist", "composers":"componisten",
#"two":"twee", "shed":"schuur", "sheds":"schuren" }

#sentence = "Last week The Royal Festival Hall saw the first \
#performance of a new symphony by one of the world's leading \
#modern composers, Arthur \"Two-Sheds\" Jackson." 

import string

english_dutch = {
"last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":"zaag",
"first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend",
"modern":"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren"
}

sentence = "Last week The Royal Festival Hall saw the first performance of a new symphony by one of the world's leading modern composers Arthur \"Two-Sheds\" Jackson."

words = sentence.lower().split()

translated = []

for word in words:
    clean_word = word.strip(string.punctuation)
    
    translated_word = english_dutch.get(clean_word, clean_word)
    
    translated.append(translated_word)

print("\nExercise 3 result:")
print(" ".join(translated))