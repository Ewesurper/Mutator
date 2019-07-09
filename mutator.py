# -*- coding: utf-8 -*-
#Name: Mutator.py
#Purpose:Create mutations of supplied word(s)
#Last updated: 8 July 2019
#Version: 2.1
#Created by: Ewesurper

##Example Commands:
#python mutator.py -w password
#python mutator.py -w password >> password_mutations.txt
#python mutator.py -d2 -w password
#python muation.py -d2 -w password >> password_mutations_full.txt
#TODO: Add file output functionality
#TODO: Add count functionality -c

#Import Libraries
import argparse
import itertools

#Define Argparse
parser = argparse.ArgumentParser()

parser.add_argument('-w', action='store', dest='user_word', help='Word to mutate')
parser.add_argument('-f', action='store', dest='user_list', help='Wordlist to mutate')
#parser.add_argument('-o', action='store', dest='file_output', help='File to output results')
parser.add_argument('-d2', action='store_true', dest='d2', help='Chose to use the second, more complete, dictionary')

args = parser.parse_args()

#Define Dictionaries
#Words will be mutated based off the dictionary picked
#Dictionary with common replacements
d1 = {
        'a':['a','A','@','4'],
        'b':['b','B','8'],
        'c':['c','C','<','k','K'],
        'd':['d','D'],
        'e':['e','E','3'],
        'f':['f','F','ph'],
        'g':['g','G','6','9'],
        'h':['h','H'],
        'i':['i','I','1','|','!'],
        'j':['j','J'],
        'k':['k','K','c','C'],
        'l':['l','L','|'],
        'm':['m','M'],
        'n':['n','N'],
        'o':['o','O','0'],
        'p':['p','P'],
        'q':['q','Q'],
        'r':['r','R'],
        's':['s','S','z','Z','$','5'],
        't':['t','T','7'],
        'u':['u','U'],
        'v':['v','V'],
        'w':['w','W'],
        'x':['x','X'],
        'y':['y','Y'],
        'z':['z','Z','s','S','2'],
        '0':['0'],
        '1':['1'],
        '2':['2'],
        '3':['3'],
        '4':['4'],
        '5':['5'],
        '6':['6'],
        '7':['7'],
        '8':['8'],
        '9':['9'],
        '0':['0'],
        '!':['!'],
        '@':['@'],
        '#':['#'],
        '$':['$'],
        '%':['%'],
        '^':['^'],
        '&':['&'],
        '*':['*'],
        '(':['('],
        ')':[')'],
        '-':['-'],
        '_':['_'],
        '+':['+'],
        '=':['='],
        '{':['{'],
        '}':['}'],
        '[':['['],
        ']':[']'],
        '|':['|'],
        '\\':['\\'],
        '`':['`'],
        '~':['~'],
        ':':[':'],
        ';':[';'],
        '"':['"'],
        '\'':['\''],
        '<':['<'],
        '>':['>'],
        '?':['?'],
        ',':[','],
        '.':['.'],
        '/':['/'],
        ' ':[' ']
}

#Dictionary with rare and complex replacements
#Pulled off the wiki page. Deleted some that didnt make any sense
#https://simple.wikipedia.org/wiki/Leet
#Some still seem very obscure to me. Maybe I am just not cool enough to understand them. I included them anyway
d2 = {
	'a':['a','A','4','@','/-\\','/_\\','/\\','Д'],
	'b':['b','B','8','|3','13','|8','18','6','|B','|8','lo','|o','j3','ß'],
	'c':['c','C','k','K','<','{','[','(','©','¢'],
	'd':['d','D','|)','|}','|]'],
	'e':['e','E','3','£','₤','€'],
	'f':['f','F','|=','ph','|#'],
	'g':['g','G','6','9'],
	'h':['h','H','4','|-|','[-]','{-}','}-{','}{','|=|','[=]','{=}','/-/','(-)',')-(',':-:','I+I'],
	'i':['i','I','1','|','!','eye'],
	'j':['j','J','_|','_/','_7','_)','_]','_}'],
	'k':['k','K','c','C','|<','1<','l<','|{','l{'],
	'l':['l','L','1','!','|','|_'],
	'm':['m','M','44','|\\/|','^^','/\\/\\','/X\\','[\\/]','[V]','(V)','N\\'],
	'n':['n','N','|\|','/\/','/V','И'],
	'o':['o','O','0','()','[]','{}','<>','Ø','oh'],
	'p':['p','P','|o','|O','|>','|*','|°','|D','/o','[]D','|7'],
	'q':['q','Q','O_','9','(,)','0''kw'],
	'r':['r','R','|2','12','.-','|^','l2','Я','®'],
	's':['s','S','z','Z','5','$','§'],
	't':['t','T','7','+','7`','\'|\'','`|`','~|~','-|-','\'][\''],
	'u':['u','U','|_|','\\_\\','/_/','\\_/','(_)','[_]','{_}'],
	'v':['v','V','\\/'],
	'w':['w','W','uu','UU','\\/\\/','(/\\)','\\^/','|/\\|','\\X/','\\\\','//','vv','VV','\\_|_/','\\\\//\\\\//','Ш','2u','\\V/'],
	'x':['x','X','%','*','><','}{',')(','Ж'],
	'y':['y','Y','`/','¥','\\|/','Ч'],
	'z':['z','Z','s','S','2','5','7_','>_','(/)'],
	'0':['0'],
	'1':['1'],
	'2':['2'],
	'3':['3'],
	'4':['4'],
	'5':['5'],
	'6':['6'],
	'7':['7'],
	'8':['8'],
	'9':['9'],
	'0':['0'],
	'!':['!'],
	'@':['@'],
	'#':['#'],
	'$':['$'],
	'%':['%'],
	'^':['^'],
	'&':['&'],
	'*':['*'],
	'(':['('],
	')':[')'],
	'-':['-'],
	'_':['_'],
	'+':['+'],
	'=':['='],
	'{':['{'],
	'}':['}'],
	'[':['['],
	']':[']'],
	'|':['|'],
	'\\':['\\'],
	'`':['`'],
	'~':['~'],
	':':[':'],
	';':[';'],
	'"':['"'],
	'\'':['\''],
	'<':['<'],
	'>':['>'],
	'?':['?'],
	'?':['?'],
	',':[','],
	'.':['.'],
	'/':['/'],
	' ':[' ']
}

#delcare lists for various storage
wordlist = []
output = []

#populate wordlist with each word that will be mutated based on 
if args.user_list:
    #read in each line of user_list as element in wordlist
    wordlist = [line.rstrip('\n') for line in open(args.user_list)]
if args.user_word:
    #append user_word to wordlist
    wordlist.append(args.user_word)

#iterate through each word in wordlist
for word in wordlist:
    #Clear out old characterlist and list_o_possibilities
    list_o_possibilities = None
    characterlist = None
    #Create list to contain 
    list_o_possibilities = []
    #Explode word into list of characters
    characterlist = list(word.lower())
    #Assemble the list of lists
    if args.d2 == True:
        for character in characterlist:
            list_o_possibilities.append(d2[character])
    else:
        for character in characterlist:
            list_o_possibilities.append(d1[character])
    #store mutations in output
    for element in itertools.product(*list_o_possibilities):
        #print(''.join(element))
        output.append(''.join(element))
#Print the final output
#print(output)
for elem in output:
    print elem
