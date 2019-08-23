def writeFile(filePath,line):
	file = open(filePath, 'w')
	file.write(line)

writeFile('item.txt','new item')
