# Author : Niroshiman

filename = 'words.txt'

# stored all the words from the text file into list
with open(filename) as file_object:

	words = file_object.readlines()
	
# a function that takes every alphabet from a username and puts into a list
def make_words(name):

	name = name.upper()	# conver name to an uppercase string
	list = []	# this is an empty list
	
	for alpha in name:	# take the current alphabet in name...
		list.append(alpha)	# and put it in the list

	return list	# once the list is complete return the list

name = make_words('dharshana')	# returns a list called name
total = 0


# take the current word in the list of words
for word in words:

	
	# eliminating the next line character from end of the word, word is a string FYI
	word = word.replace('\n',"").upper() # convert word to an uppercase string
	word = make_words(word) # converting the word from string to list

	# set current count to length of word
	count = len(word)

	# for the current alphabet in the word from the dictionary...
	for alpha in word:

		# if this current alphabet in word is found in the name list...
		if alpha in name:
			count -= 1	# reduce the count by one
			name.remove(alpha)	# and remove the current alphabet from the name list...

	# check if the count has reached zero...
	# indicating all alphabets in word exists in name
	if count == 0:
		# print(word)	# print that word to double confirm
		total += 1

		if len(word) > 0:
			word = ''.join(word) # convert list to string
			print(word)

	name = make_words('dharshana')

name = ''.join(name)
print('total number of words found in ' + name + ': ' + str(total))



# draft

# word = make_words('boshi')	# returns a list called word
# print(name)
# print(word)
# match_count = len(word)

# # for the current alphabet in the word from the dictionary...
# for alpha in word:

# 	# if this current alphabet in word is found in the name list...
# 	if alpha in name:
# 		print('yes')	# print yes to indicate it exists in the name list...
# 		name.remove(alpha)	# and remove the current alphabet from the name list...
# 		print(name)	# this is the new name list with one of the alphabets removed...
# 	else:
# 		print('no') # print no to indicate it does not exist
# 		print(name)		# nothing to remove from the name list, print it anyways

# print(name)
