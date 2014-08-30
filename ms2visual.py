#!/usr/bin/env python3
import math
import sys

def error(str, exitcode=1):
	print(sys.argv[0] + ": error: " + str, file=sys.stderr)
	exit(exitcode)

def mod_figure_width(n):
	width=1
	# if the number is negative, 1 should be added to width for the '-' sign
	if n<0:
		width+=1

	n=abs(n)

	while n>=10:
		n/=10
		width+=1

	return width

def main():
	while True:
		try:
			s=input()
		except EOFError:
			break

		s=[int(i) for i in s.split()]
		if math.modf(math.sqrt(len(s)))[0]!=0:
			error("invalid length of input line: " + str(len(s)))
		Ceilings=len(s)
		X=int(math.sqrt(Ceilings))

		width=max(mod_figure_width(max(s)), mod_figure_width(min(s)))

		print(("+" + "-"*width)*X + "+")
		for i in range(Ceilings):
			print("|%*d"%(width, s[i]), end='')
			if i%X==X-1:
				print("|\n" + ("+" + "-"*width)*X + "+")
		print("-"*12)

if __name__=='__main__':
	main()
