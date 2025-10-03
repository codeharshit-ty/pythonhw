file1 = open("codingal.txt",'r')
file2 = open("codingalupdated.txt",'w')
for line in file1.readlines():
    if (line.startswith('coding')):
        print(line)
        file2.write(line)
file1.close()
file2.close()
