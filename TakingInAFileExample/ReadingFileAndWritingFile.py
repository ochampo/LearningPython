f = open('inputFile.txt', 'r')
passFile = open('PassFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
f.close()
passFile.close()