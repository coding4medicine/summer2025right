def compare(x, y):
    counts = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            counts += 1
            print(i, x[i], y[i])
    print(counts)

    return counts

f = open("whale.aln")
g = open("animaux.aln")
lines1=g.readlines() 
lines=f.readlines()
others=["","",""]
whales=["","",""]
for i in range(0, 3):
        for j in range(10*i+1,10*i+9):
                others[i] += lines1[j].rstrip('\n')

for i in range(0, 3):
	for j in range(10*i+1,10*i+9):
		whales[i] += lines[j].rstrip('\n')
#print("beluga\n",whales[0],"\ndolphin\n",whales[1],"\norca\n",whales[2])
print("beluga vs dolphin")
compare(whales[0], whales[1])
print("dolphin vs orca")
compare(whales[1],whales[2])
print("orca vs beluga")
compare(whales[2],whales[0])
