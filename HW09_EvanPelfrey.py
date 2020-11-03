#Exercise 1
def wordCount(wordList):
    counters = {}
    for word in wordList:
         if word not in counters:
             counters[str(word)] = 1
         else:
            counters[str(word)] += 1
    return(counters)

#Exercise 2
def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d.keys():
            d[word[0]] = [word]
        elif word in d[word[0]]:
            continue
        elif word[0] in d.keys():
            d[word[0]].append(word)
    return d

#Exercise 3 (not done)
def shareALetter(wordList):
    d = {}
    for word in wordList:
        if word not in d:
            d[word] = [word]
    for word in wordList:
        for letter in word:
            if letter in 
