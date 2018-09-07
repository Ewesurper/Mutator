#!/usr/bin/env/python

#Import Libraries
import argparse
import os
from prettytable import PrettyTable

#Define Argparse,
parser = argparse.ArgumentParser()

parser.add_argument('-hf', action='store', dest='hashfile', help='Define the location of the hash dump')
parser.add_argument('-pf', action='store', dest='potfile', help='Define the location of the potfile')
parser.add_argument('-d', action='store', dest='domain', default="*None*", help='List domain of recovered credentials')


args = parser.parse_args()

#Define variables
cracked_dict = {}
row_count = 0
t = PrettyTable(['Row', 'Domain', 'Username', 'Hash', 'Password'])

#Create key pairs
def get_pair(line):
	key, sep, value = line.strip().partition(":")
	return key, value

#Add potfile lines to cracked_dict
f1=open(args.potfile, 'r')
for line in f1:
	cracked_dict[get_pair(line)[0]] = get_pair(line)[1]
f1.close()

#Compare hashfile to cracked_dict
for key, value in cracked_dict.items():
	f2=open(args.hashfile, 'r')
	for line in f2:
		if line.split(':')[2] == key:
			row_count += 1
			t.add_row([row_count, args.domain, line.split(':')[0],  line.split(':')[1] +':'+ line.split(':')[2], value])
f2.close()

#Print Table
print t

