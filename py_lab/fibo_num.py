#!/usr/bin/python3
n=(int)(input("fibonacci number?"))
fibonachi = [1,1]
number = 1
while number<(n-1):
	number = number+1
	a = fibonachi[number-1] + fibonachi[number-2]
	fibonachi.append(a)
print(fibonachi)
print("F", n," = ",  fibonachi[-1],sep='')
