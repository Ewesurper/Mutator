# -*- coding: utf-8 -*-
#Name: Mutator.py
#Purpose:Create mutations of supplied word(s)
#Last updated: 7 August 2019
#Version: 2.2
#Created by: Ewesurper

##Example Commands:
#python mutator.py -w password
#python mutator.py -w password -o password_mutations.txt
#python mutator.py -l words.lst 

#Todo-List
#Add count functionality -c

#Import Libraries
import argparse
import itertools
from collections import defaultdict

#Define Argparse
parser = argparse.ArgumentParser()

parser.add_argument('-w', action='store', dest='user_word', help='Word to mutate')
parser.add_argument('-l', action='store', dest='user_list', help='Wordlist to mutate')
parser.add_argument('-o', action='store', dest='user_output', default=' ',help='File to output results')
parser.add_argument('-d', action='store', dest='dict', help='Chose a dictionary to use')

args = parser.parse_args()

#Define Dictionaries
d = defaultdict(list)
with open(args.dict, 'r') as dfile:
    for line in dfile:
        k, v = line.rstrip().split(':')
        d[k].extend(map(str.strip,v.split(',')) if v.strip() else [])
dfile.close()

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

#Iterate through each word in wordlist
for word in wordlist:
    #Clear out old characterlist and list_o_possibilities
    list_o_possibilities = None
    characterlist = None
    #Create list to contain 
    list_o_possibilities = []
    #Explode word into list of characters
    characterlist = list(word.lower())
    #Assemble the list of lists
    for character in characterlist:
        list_o_possibilities.append(d[character])
    #store mutations in output
    for element in itertools.product(*list_o_possibilities):
        #print(''.join(element))
        output.append(''.join(element))

#Output output
if args.user_output == ' ':
    for elem in output:
        print(elem)
else:    
    with open(args.user_output, 'w') as output_file:
        for elem in output:
            output_file.write(elem + '\n')
    output_file.close()
