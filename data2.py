with open("data.txt", "r") as f:
    for line in f.readlines():
        newline = line.rstrip().split(',')
        with open("data2.txt", "a") as f2:
            f2.write(newline[2]+','+newline[1]+','+newline[0]+'\n')
