#!/usr/bin/env python3
import math
import sys

while True:
	try:
		s=input()
	except EOFError:
		break

	s=[int(i) for i in s.split()]
	if math.modf(math.sqrt(len(s)))[0]!=0:
		print("error: invalid length of input line", file=sys.stderr)
		exit(1)
	Ceilings=len(s)
	X=int(math.sqrt(Ceilings))

	width=1
	ma=max(s)
	mi=min(s)
	i=max(ma, abs(mi))
	if i==abs(mi) and mi<0:
		width+=1
	while i>=10:
		i/=10
		width+=1

	print(("+" + "-"*width)*X + "+")
	for i in range(Ceilings):
		print("|%*d"%(width, s[i]), end='')
		if i%X==X-1:
			print("|")
			print(("+" + "-"*width)*X + "+")
	print("-"*12)
