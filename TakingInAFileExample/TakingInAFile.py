f = open('inputFile.txt', 'r')

#print(f.read())
for l in f:
    PassingScoreFromFile = l.split()
    if PassingScoreFromFile[2] == 'P':
        print(l)

f.close()