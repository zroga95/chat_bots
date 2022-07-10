import os
import glob
from parse_corpus import parse_script_lines
from comparing_strings import getClosestSentiment

if __name__ == '__main__':

	character_lines = parse_script_lines('Brazil_script.html', 'TUTTLE')
	submitted_str = input('Type a string to send. Leave empty for default string')

	if submitted_str != '':
		tester = submitted_str
	else:
		tester = "I'm creating some simple chatbots using natural langugage processing and sentiment."
	print('You sent: ' + tester)
	print('Tuttle replies: ' + getClosestSentiment(character_lines, tester))