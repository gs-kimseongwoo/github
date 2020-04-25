#!usr/bin/python3

def convert(value):
	integer = int(value,2)
	eight = format(integer,'o')
	sixteen = format(integer,'x')
	print("=>OCT>" + eight)
	print('=>DEC> {}'.format(integer))
	print("=>HEX>"+ sixteen)
