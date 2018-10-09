#Import Libraries
import argparse

#Define Argparse,
parser = argparse.ArgumentParser()

parser.add_argument('-l', action='store', dest='userlist', help='Define the wordlist you wish to combinate')

args = parser.parse_args()

# create matching lists from the contents of the wordlist file
list1 = list2 = open(args.userlist).readlines()

for line1 in list1:
	for line2 in list2:
		print(line1.strip()+line2.strip())
