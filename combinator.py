#!/usr/bin/env python3

#Import Libraries
import argparse

#Define Argparse,
parser = argparse.ArgumentParser()

parser.add_argument('-l', action='store', dest='userlist', help='Define the wordlist you wish to combinate')

args = parser.parse_args()

list1 = []
list2 = []

f = open(args.userlist, 'r')
for word in f:
	list1.append(word)
	list2.append(word)
for line1 in list1:
	for line2 in list2:
		print(line1.strip()+line2.strip())
