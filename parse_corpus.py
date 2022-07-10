from nltk.tokenize import sent_tokenize, word_tokenize
import re

def parse_script_lines(path, character_name):
    counter = 0
    character_lines = []
    with open(path, 'r') as f:
        lines =  f.readlines()
        for i in range(0, len(lines)):
            if character_name.upper() +'\n' in lines[i].upper():
                temp = ''
                for x in range(1,20):
                    if lines[x + i].strip() != '':
                        temp += lines[x+i].strip() + ' '
                    else:
                        break
                #print(str(temp))
                if (len(str(temp)) > 10) & (len(str(temp)) < 500):
                    character_lines.append(str(temp))
                #print("\n', '\n'" in temp)
                #print([lines[x + i] for x in range(1,20)])
                counter = counter +1
            #breaking when non-specific issues
            if counter > 10000:
                break
    return character_lines
    