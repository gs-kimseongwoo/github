#!/usr/bin/python3

n=int(input("how many numbers do you want to input"))

a = []
number = 0
while number < n:
	variable=(int)(input("input the number"))
	a.append(variable)
	number = number+1
sum = 0
for plus in a:
	sum = sum+plus
print(sum/len(a))
