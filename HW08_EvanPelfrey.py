#Exercise 1
def fcopy(file1, file2):
    file1 = open (file1)
    file2 = open (file2, 'w')
    source = file1.read()
    file2.write(source)
    file1.close()
    file2.close()
#Exercise 2
def stats(file):
    file = open (file)
    content = file.read()
    wordList = content.split()
    print("word count: " + str(len(wordList)))
    print("character count: " + str(len(content)))
    file.seek(0)
    lineList = file.readlines()
    print("line count: " + str(len(lineList)))
#Exercise 3 (not done)
def repeatWords(inputFile, outputFile):
    inF = open (inputFile)
    outF = open (outputFile, 'w')
    lineList = inF.readlines()
    d = {}
    for line in lineList:
        line.split()
    for word in lineList:
            if word not in d:
                d[word] = 1
            elif d[word] == 1:
                outF.write(word)
                d[word] += 1
        
            
        
