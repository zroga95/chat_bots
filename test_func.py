import os
import glob
from parse_corpus import parse_script_lines, parse_script_characters, parse_dialogue
from comparing_strings import getClosestSentiment, getClosestCharacterSentiment

if __name__ == '__main__':

	character_lines = parse_dialogue('Brazil_script.html')
	submitted_str = input('Type a string to send. Leave empty for default string')

	if submitted_str != '':
		tester = submitted_str
	else:
		tester = "I'm creating some simple chatbots using natural langugage processing and sentiment."
	print('You sent: ' + tester)

chrs_array = []

for chr in character_lines.keys():
	chrs_array.append(" ".join([str(item) + '. ' for item in character_lines[chr]]))

result = getClosestCharacterSentiment(character_lines, submitted_str)

print(result)