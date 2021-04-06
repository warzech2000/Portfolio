file= open('file.txt', 'r')
f = file.readlines()
print(f)
newList = []
for line in f:
    newList.append(line.strip())
print(newList)