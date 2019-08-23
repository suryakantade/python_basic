def openFile(filePath):
	file = open(filePath,'r')
	print('opening items in file /s'.format(filePath))
	for line in file:
		print(line)
	file.close()
openFile('item.txt')
