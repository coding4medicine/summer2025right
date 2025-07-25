def compare(x, y):
    counts = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            counts += 1
            print(i, x[i], y[i])
    print(counts)

    return counts
list = [
    ["", "beluga", "dolphin", "orca", "Zebra Fish", "Cow", "Rat"],
    ["beluga", "", "", "", "", "", ""],
    ["orca", "", "", "", "", "", ""],
    ["Zebra Fish", "", "", "", "", "", ""],
    ["Cow", "", "", "", "", "", ""],
    ["Rat", "", "", "", "", "", ""]
]
f=open("whale.aln")
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
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
#print(list[6])
#print(list[7])


