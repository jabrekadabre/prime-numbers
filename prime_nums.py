#program works, but is porobably really shitty since im a beginner...

j =0
stev = []
pra=[]
pme = int(input("primes to:"))
pmepol = pme/2
x = 0
ses = 0
while x <= pme:    #creates list of all numbers from 0 to .pme.
	stev.append(x)
	x += 1
	y = 1
while y <= pmepol: #replaces every number that is % by itself
	y += 1
	z = y
	if stev[z] == 0:
		continue
	else:
		while z <= pme:
			z += y
			if z > pme:
				break
			stev[z] = 0


for g in stev:       # prints out the primes...
	if g == 0:
		continue
	else:
		j += 1
		print(g)
print("number of prime nums:", j)