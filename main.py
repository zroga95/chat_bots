import os
import glob
from parse_corpus import parse_dialogue
from comparing_strings import getClosestSentiment

if __name__ == '__main__':

	character_lines = parse_dialogue('Brazil_script.html')
	submitted_str = input('Type a string to send. Leave empty for default string')

	if submitted_str != '':
		tester = submitted_str
	else:
		tester = "I'm creating some simple chatbots using natural langugage processing and sentiment."
	print('You sent: ' + tester)

	selected_character = 'TUTTLE'
	print(selected_character + ' replies: ' + getClosestSentiment(character_lines[selected_character], tester))