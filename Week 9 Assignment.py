#Excercise 1
#Write function that matches a string that has an 'a' followed by anything, ending in 'b'
import re
a = input('Enter a string of letters')
endB = re.compile(r"[a](b)$")
match = re.search(endB, a)
if match:
    print('Great string, your string ends in a b')
else:
    print('It does not end with a b, b-asist is seems')

#Exercise 2
#Write function that matches string if it starts with word
sentence = input("Input a sentence")
deconstructedSentence = re.split(r'\s', sentence)
if not deconstructedSentence[0] == ' ':
    print('Your sentence does not begin with a proper word')
else:
    print('Great sentence')


#Exercise 3
#Write function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

date = input('Enter the date in the yyyy-mm-dd format')
deconstructedDate = re.split(r'\-', date)
length = len(deconstructedDate)
newdate = "-".join(deconstructedDate[length::-1])
print(newdate)


#Exercise 4
#Write function to search for words containing 3 letters in the given string
phrase = input('Enter a concise sentence of your choice')
phrase = re.split(r'\s',phrase)
word = ''
for k in phrase:
    if len(k) == 3:
        word = word +','+ k
    else:
        print('No three lettered words in your sentence')
print(word)


#Exercise5
#Write function to convert camel case string to snake case string
camel = input('Enter a single camel stringed word')
word1 = re.split(r'[A-Z]', camel)
word1[1].lower()
snake = '_'.join(word1)
print(snake)

#Exercise 6
#Write function to find all adverbs in the given string
#'The early bird catches the worm.'
string1 = input('Enter a phrase')
match1 = re.compile(r'(ly)')
adverb = re.search(match1 , string1)
print(adverb)


#Exercise 7
#Write function to remove multiple spaces in the given string
#'Better    late    than    never.'
givenString = 'Better    late    than    never.'
givenString = re.sub(r'\s+',' ',givenString)
print(givenString)

#Exercise 8
#Write function that matches word that does not starts and ends with s in the given string
sWords = input('Enter a concise sentence')
sWordSearch = re.compile(r'(\s\S),(s)$,(S)$')
newWord = re.search(sWordSearch, sWords)
if sWordSearch:
    print(newWord)

#Exercise 9
#Write function to remove leading zeroes from month and day
removingZeros = input('Input the dat in the yyyy-mm-dd format')
re.sub(r'[0]','',removingZeros)
print(removingZeros)

#Exercise 10
#Write function that will find sequence of 4 and more same symbols in given string
findingReps = input('enter a string of letter in no specific chronological order')
count = 0
for findingReps:
    stringsFound = re.findall(r'[a-z]+')
    count = count + 1
    if count >= 4:
        print(f'Letter {stringsFound} has been fount {count} times')
    else:
        print('No frequent letters found')