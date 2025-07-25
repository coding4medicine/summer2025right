def compare(x, y):
    counts = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            counts += 1
            #print(i, x[i], y[i])
    #print(counts)

    return(counts)
list = [
    ["          ", "beluga", "dolphin", "orca", "Zebra Fish", "Cow", "Rat"],
    ["beluga    ", "    ", "    ", "    ", "    ", "    ", "    "],
    ["dolphin   ", "    ", "    ", "    ", "    ", "    ", "    "],
    ["orca      ", "    ", "    ", "    ", "    ", "    ", "    "],
    ["Zebra Fish", "    ", "    ", "    ", "    ", "    ", "    "],
    ["Cow       ", "    ", "    ", "    ", "    ", "    ", "    "],
    ["Rat       ", "    ", "    ", "    ", "    ", "    ", "    "]
]
f=open("/home/spadejac/main-folder/summer2025right/whale proteins/whale.aln")
g = open("/home/spadejac/main-folder/summer2025right/whale proteins/animaux.aln")
lines1=g.readlines() 
lines=f.readlines()
#print(len(lines))
animals=["","","","","",""]
for i in range(0, 3):
        for j in range(10*i+1,10*i+9):
                animals[i] += lines1[j].rstrip('\n')

for i in range(0, 3):
      for j in range(10*i+1,10*i+9):

        animals[i+3] += lines[j].rstrip('\n')
for i in range(1,7):
      for j in range(1,7):
        #    print(len(animals[i-1]))
           list[i][j]= compare(animals[i-1],animals[j-1])
#print("beluga\n",whales[0],"\ndolphin\n",whales[1],"\norca\n",whales[2])
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
# #print(list[7])
# for e in range(len(list)):
#      print(list[e])
# print(animals[3], "\n")
# print(animals[4], "\n")
# print(animals[5], "\n")

