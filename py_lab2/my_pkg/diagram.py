#!usr/bin/python3


def union(args1,args2):
	un = []	
	un.extend(args1)	
	print(un)
	for numbers2 in range(len(args2)):
		count = 0
		for numbers in range(len(args1)):
			if args2[numbers2] == args1[numbers]:
				count+=1
		if count == 0:
			un.append(args2[numbers2])
	print("union",end = '')
	print(un)

def intersection(args1,args2):
	inter = []
	for numbers in range(len(args1)):
		for numbers2 in range(len(args2)):
			if args1[numbers] == args2[numbers2]:
				inter.append(args1[numbers])
	print("intersection",end = '')
	print(inter)
