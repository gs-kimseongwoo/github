#!/usr/bin/python3
import my_pkg.conversion
import my_pkg.diagram

def checking(array):
	print(array[1])

while True:
	menu=int(input("Select menu: 1)conversion 2)union/intersection 3)exit?"))
	if menu == 1:
		number = input("input binary number : ")
		my_pkg.conversion.convert(number)
	if menu == 2:
		args1 = eval(input("1st list"))
		args2 =	eval(input("2st list")) 
		my_pkg.diagram.union(args1,args2)
		my_pkg.diagram.intersection(args1,args2)
	if menu ==3:
		print("exit the program...")	
		break
