# Author : Niroshiman
# Descri : Code that generates anagram from any word. 
# Instru : 1) Set type_word to personally desired word  
#        : 2) Set valid_word_length to desired number

# A function that takes every alphabet from a username and puts into a list
def make_words(name):

	name = name.upper()	# convert name to an uppercase string
	name_alpha_list = []	# this is an empty list
	
	for alpha in name:	# take the current alphabet in name
		name_alpha_list.append(alpha)	# and put it in the list

	return name_alpha_list	# once the list has all alphabets from name, return it


# Set the file name as the name of the English dictionary in use.
filename = 'words.txt'

# Set desired word which will be used to generate anagram
type_word =  'insertword'
name = make_words(type_word)	# returns a list called name
total = 0	# number of anagrams generated 
valid_word_length = 0 # set desired word length of a generated anagram

# Stored all the words from the text file into a list.
with open(filename) as file_object:
	words = file_object.readlines()
	

# Take the current word in the list of words
for word in words:

	name = make_words(type_word)
	
	# Eliminating the next line character from end of the word, word is a string 
	word = word.replace('\n',"").upper() # convert word to an uppercase string
	word = make_words(word) # converting the word from string to list

	# Set count to length of current word
	count = len(word)

	# For the current alphabet in the word from the dictionary...
	for alpha in word:

		# if this current alphabet in word is found in the name list...
		if alpha in name:
			count -= 1	# reduce the count by one
			name.remove(alpha)	# and remove the current alphabet from the name list...

	# check if the count has reached zero...
	# indicating all alphabets in word exists in name
	if count == 0:

		total += 1

		if len(word) > valid_word_length:
			word = ''.join(word) # convert list to string
			print(word)	# print the word


name = ''.join(name) # convert list to string
print('total number of words found in ' + name + ': ' + str(total))
