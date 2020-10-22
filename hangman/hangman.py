from random import randint
from os.path import join, dirname

#files---
assets = join(dirname(__file__), "assets")
#--------

#functions---
def get_lexicon():
	current_word = ""
	list_lexicon = []

	with open(join(assets, "words.txt"))as w:
		lexicon = w.read()
	for i in lexicon:
		if(i != "\n"):
			current_word += i
		else:
			list_lexicon.append(current_word)
			current_word = ""
		
	return list_lexicon	

def find_pos(letter, word): ### get positions of letters in word
	last_pos = 0
	positions = []
	last_pos = word.find(letter)
	while(last_pos != -1): ### word.find() returns -1 if there is no such symbol
		positions.append(last_pos)
		last_pos = word.find(letter, last_pos + 1)
	return positions	

def print_progress(word, positions): ### function prints gaps filled with right letters that have been already guessed
	for i, letter in zip(range(len(get_lexicon())), word):
		if i in positions:
			print(letter, end=" ")
		else:
			print("_", end=" ")	
#------------

#variables---
word = get_lexicon()[randint(0, len(get_lexicon()) - 1)] ### hidden word
letters_count = 0 ### how many words in hidden word
positions = [] ### indexes of guessed words
guessed_letters = [] ### list of guessed_letters
mistakes_count = 1 ### how many mistakes player made
gallows = None ### the gallows texture
#------------

#phrases---
phrases = {
	"letters" : "Letters in word:",
	"guess" : "Guess the letter:",
	"input_error" : "You entered too many symbols. Try again",
	"repeating_symbol" : "You've entered that symbol before",
	"correct" : "Correct! The letter position is",
	"incorrect" : "Incorrect!",
	"loss" : "I'm trying to be gracious, I'm SOOOO sorry, you're dead. Bye. The hidden word was:",
	"win" : "Congratulations on your victory. The hidden word was:"
}
#----------

#the game progress---
with open(join(assets, "0.txt")) as f: ### print gallows w/o body
	gallows = f.read()
print(gallows)

for i in word: ### count the letters in hidden word
	letters_count += 1
print(phrases["letters"], letters_count)

while(mistakes_count < 7): ### main game cycle
	print(phrases["guess"])
	letter = input()

	if len(letter) != 1: ### check if only one symbol inputed
		print(phrases["input_error"])
		letter = ""
		continue

	if letter in guessed_letters:
		print(phrases["repeating_symbol"])
		continue

	guessed_letters.append(letter) 		
	
	if letter in word:
		positions.extend(find_pos(letter, word))
		print(phrases["correct"], find_pos(letter, word))
	else:
		print(phrases["incorrect"])
		with open(join(assets, "{}.txt").format(mistakes_count)) as f2:
			gallows = f2.read()
		print(gallows)
		mistakes_count += 1

	if len(positions) == len(word): ### check if the word is fully guessed
		break

	print("")
	print_progress(word, positions)

print("")	
if mistakes_count == 7:
	print(phrases["loss"], word)
else:
	print(phrases["win"], word)		
#---------------