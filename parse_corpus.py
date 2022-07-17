from nltk.tokenize import sent_tokenize, word_tokenize
import re

def parse_script_characters(path):
    counter = {}
    characters = {}
    with open(path, 'r') as f:
        lines =  f.readlines()
        for i in range(0, len(lines)):
            if lines[i].strip() in counter:
                counter[lines[i].strip()] = counter[lines[i].strip()] + 1
            else:
                counter[lines[i].strip()] = 1

    for i in counter:
        if((len(i) > 0) & (counter[i] > 1) & (i.upper() == i) 
                & (i != '\n') & ('INT.' not in i)
                & ('EXT.' not in i) & ('CUT TO' not in i)):
            characters[i] = counter[i]

    return characters

def parse_script_lines(path, character_name):
    counter = 0
    character_lines = []
    if '\n' not in character_name:
        character_name += '\n'

    with open(path, 'r') as f:
        lines =  f.readlines()
        for i in range(0, len(lines)):
            if character_name.upper() in lines[i].upper():
                temp = ''
                for x in range(1,20):
                    if lines[x + i].strip() != '':
                        temp += lines[x+i].strip() + ' '
                    else:
                        break
                #print(str(temp))
                joined_str = str(temp)
                if (len(joined_str) > 10) & (len(joined_str) < 500):
                    #remove anything in parenthesis
                    character_lines.append(re.sub("\(.*?\)","",joined_str))
                #print("\n', '\n'" in temp)
                #print([lines[x + i] for x in range(1,20)])
                counter = counter + 1
            #breaking when non-specific issues
            if counter > 10000:
                break
    return character_lines
    
def parse_dialogue(path):

    repeat_characters = parse_script_characters(path)

    dialogue_dict = {}

    for i in repeat_characters:
        lines = parse_script_lines(path, i)
        if len(lines) > 0:
            dialogue_dict[i.split('\n')[0]] = lines

    return dialogue_dict

