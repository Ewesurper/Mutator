#!/usr/bin/env python3

#Import Libraries
import argparse
import itertools

#Define Argparse,
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
        'z':['z','Z','2']
}



#Define character list
characterlist = list(args.user_word.lower())
characterlength = len(args.user_word)

# build the list of lists
list_o_possibilities = []
for letter in characterlist:
    list_o_possibilities.append(md[letter])    

for element in itertools.product(*list_o_possibilities):
        print(''.join(element))

'''
#Define Master Dictonary
md = {
        'a':{'a','A','@','4'},
        'b':{'b','B','8'},
        'c':{'c','C','<'},
        'd':{'d','D'},
        'e':{'e','E','3'},
        'f':{'f','F','ph'},
        'g':{'g','G','6','9'},
        'h':{'h','H'},
        'i':{'i','I','1','|','!'},
        'j':{'j','J'},
        'k':{'k','K'},
        'l':{'l','L','|'},
        'm':{'m','M'},
        'n':{'n','N'},
        'o':{'o','O','0','()','[]','{}','<>'},
        'p':{'p','P'},
        'q':{'q','Q'},
        'r':{'r','R'},
        's':{'s','S','z','Z','$','5'},
        't':{'t','T','7'},
        'u':{'u','U'},
        'v':{'v','V'},
        'w':{'w','W'},
        'x':{'x','X'},
        'y':{'y','Y'},
        'z':{'z','Z','2'}
}

if characterlength == 1:
	a = characterlist[0]
	for value0 in md[a]:
		print(value0)
elif characterlength == 2:
	a = characterlist[0]
	b = characterlist[1]
	for value0 in md[a]:
		for value1 in md[b]:
			print(value0+value1)
elif characterlength == 3:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	for value0 in md[a]:
       		for value1 in md[b]:
               		for value2 in md[c]:
                       		print(value0+value1+value2)
elif characterlength == 4:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					print(value0+value1+value2+value3)
elif characterlength == 5:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						print(value0+value1+value2+value3+value4)
elif characterlength == 6:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							print(value0+value1+value2+value3+value4+value5)
elif characterlength == 7:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								print(value0+value1+value2+value3+value4+value5+value6)
elif characterlength == 8:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									print(value0+value1+value2+value3+value4+value5+value6+value7)
elif characterlength == 9:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										print(value0+value1+value2+value3+value4+value5+value6+value7+value8)
elif characterlength == 10:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	j = characterlist[9]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										for value9 in md[j]:
											print(value0+value1+value2+value3+value4+value5+value6+value7+value8+value9)
elif characterlength == 11:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	j = characterlist[9]
	k = characterlist[10]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										for value9 in md[j]:
											for value10 in md[k]:
												print(value0+value1+value2+value3+value4+value5+value6+value7+value8+value9+value10)
elif characterlength == 12:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	j = characterlist[9]
	k = characterlist[10]
	l = characterlist[11]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										for value9 in md[j]:
											for value10 in md[k]:
												for value11 in md[l]:
													print(value0+value1+value2+value3+value4+value5+value6+value7+value8+value9+value10+value11)
elif characterlength == 13:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	j = characterlist[9]
	k = characterlist[10]
	l = characterlist[11]
	m = characterlist[12]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										for value9 in md[j]:
											for value10 in md[k]:
												for value11 in md[l]:
													for value12 in md[m]:
														print(value0+value1+value2+value3+value4+value5+value6+value7+value8+value9+value10+value11+value12)
elif characterlength == 14:
	a = characterlist[0]
	b = characterlist[1]
	c = characterlist[2]
	d = characterlist[3]
	e = characterlist[4]
	f = characterlist[5]
	g = characterlist[6]
	h = characterlist[7]
	i = characterlist[8]
	j = characterlist[9]
	k = characterlist[10]
	l = characterlist[11]
	m = characterlist[12]
	n = characterlist[13]
	for value0 in md[a]:
		for value1 in md[b]:
			for value2 in md[c]:
				for value3 in md[d]:
					for value4 in md[e]:
						for value5 in md[f]:
							for value6 in md[g]:
								for value7 in md[h]:
									for value8 in md[i]:
										for value9 in md[j]:
											for value10 in md[k]:
												for value11 in md[l]:
													for value12 in md[m]:
														for value13 in md[n]:
															print(value0+value1+value2+value3+value4+value5+value6+value7+value8+value9+value10+value11+value12+value13)
else:
	print("I'm sorry, the amount of characters supplied isn't supported yet")
'''
