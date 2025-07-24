def main():
    f = open("whale.aln")
    lines=f.readlines()
    print(lines)
    final = []
    for i in range(1, len(lines)):
        final += lines[i].rstrip('\n')
    #print(final)




main()