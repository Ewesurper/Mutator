#!/usr/bin/env python3

#Import Libraries
import argparse
import itertools

#Define Argparse
parser = argparse.ArgumentParser()

parser.add_argument('-w', action='store', dest='user_word', help='word to mutate')
parser.add_argument('-o', action='store', dest='user_output', help='output to a file')

args = parser.parse_args()

#Define Master Dictonary
md = {
        'a':['a','A','@','4'],
        'b':['b','B','8'],
        'c':['c','C','<'],
        'd':['d','D'],
        'e':['e','E','3'],
        'f':['f','F','ph'],
        'g':['g','G','6','9'],
        'h':['h','H'],
        'i':['i','I','1','|','!'],
        'j':['j','J'],
        'k':['k','K'],
        'l':['l','L','|'],
        'm':['m','M'],
        'n':['n','N'],
        'o':['o','O','0','()','[]','{}','<>'],
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
        'z':['z','Z','2'],
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
        '0':['0']
}

# create character list from user supplied word
characterlist = list(args.user_word.lower())

# assemble the list of lists
list_o_possibilities = []
for character in characterlist:
    list_o_possibilities.append(md[character])

for element in itertools.product(*list_o_possibilities):
        print(''.join(element))
