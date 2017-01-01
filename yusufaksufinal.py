data = []
f = open("final.txt", "r")
for line in f.readlines():
    data.append(int(line[11:14])) #Number stars with the 11. columns and ends with 14.
    data.sort()
print data
print [data[x:x+3] for x in xrange(0, len(data), 3)]
