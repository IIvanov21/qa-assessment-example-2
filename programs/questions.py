	# <QUESTION 1>

	# Given a word and a string of characters, return the word with all of the given characters
	# replaced with underscores

	# This should be case sensitive

	# <EXAMPLES>

	# one("hello world", "aeiou") → "h_ll_ w_rld"
	# one("didgeridoo", "do") → "_i_geri___"
	# one("punctation, or something?", " ,?") → "punctuation__or_something_"
import string

def one(word, chars):
	for i in chars:
		if i in word:
			word=word.replace(i,"_")
	return word

	# <QUESTION 2>

	# Given an integer - representing total seconds - return a tuple of integers (of length 4) representing 
	# days, hours, minutes, and seconds

	# <EXAMPLES>

	# two(270) → (0, 0, 4, 30)
	# two(3600) → (0, 1, 0, 0)
	# two(86400) → (1, 0, 0, 0)

	# <HINT>

	# There are 86,400 seconds in a day, and 3600 seconds in an hour

def two(total_seconds):
	days = int((total_seconds % (86400*30))/86400)
	hours = int((total_seconds % 86400) / 3600)
	minutes = int((total_seconds % 3600) / 60)
	seconds = int((total_seconds % 60))
	calendar=(days,hours,minutes,seconds)
	return calendar

	# <QUESTION 3>

	# Given a dictionary mapping keys to values, return a new dictionary mapping the values
	# to their corresponding keys

	# <EXAMPLES>

	# three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracias':'thank you'}
	# three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

	# <HINT>

	# Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
	dictionary={val:key for key,val in dictionary.items()}
	return dictionary

	# <QUESTION 4>

	# Given an integer, return the largest of the numbers this integer is divisible by
	# excluding itself

	# This should also work for negative numbers

	# <EXAMPLES>

	# four(10) → 5
	# four(24) → 12
	# four(7) → 1
	# four(-10) → 5

def four(number):
	if number % 2 == 0:
		return abs(int(number/2))
	elif number % 3 == 0:
		return abs(int(number/3))
	else:
		return abs(int(number/number))

	# <QUESTION 5>

	# Given a string of characters, return the character with the lowest ASCII value

	# <EXAMPLES>

	# five('abcdef') → 'a'
	# four('LoremIpsum') → 'I'
	# four('hello world!') → ' '

def five(chars):
		return min(chars)


	# <QUESTION 6>

	# Given a paragraph of text and an integer, break the paragraph into "pages" (a list of strings), where the
	# length of each page is less than the given integer

	# Don't break words up across pages!

	# <EXAMPLES>

	# six('hello world, how are you?', 12) → ['hello world,', 'how are you?']
	# six('hello world, how are you?', 6) → ['hello', 'world,', 'how', 'are', 'you?']
	# six('hello world, how are you?', 20) → ['hello world, how are', 'you?']
	
def six(paragraph, limit):
	words = paragraph.split()
	pages = []
	
	current_page = ''
	for word in words:

		new_text = f'{current_page} {word}'.lstrip()

		if len(new_text) > limit and current_page != '':
			pages.append(current_page)
			current_page = word
		else:
			current_page = new_text

	pages.append(current_page)

	return pages
	

print(six('hello world, how are you?', 12))
print(six('hello world, how are you?', 6))
print(six('hello world, how are you?', 20))