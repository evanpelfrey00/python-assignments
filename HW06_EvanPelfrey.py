#Exercise 1
def twoWords(length, firstLetter):
    returnList = []
    word = input('A ' + str(length) + '-letter word, please: ')
    if len(word) != length:
        while len(word) != length:
            word = input('A ' + str(length) + '-letter word, please: ')
            if len(word) == length:
                break
    returnList.append(word)
    word = input('A letter that starts with ' + firstLetter + ', please')
    if word[0] != firstLetter:
        while word[0] != firstLetter:
            word = input('A letter that starts with ' + firstLetter + ', please')
            if word[0] == firstLetter:
                break
    returnList.append(word)
    return(returnList)
print(twoWords(4, 'b'))
#Exercise 2
def twoWordsV2(length, firstLetter):
    returnList = []
    word = input('A ' + str(length) + '-letter word, please: ')
    while len(word) != length:
        word = input('A ' + str(length) + '-letter word, please: ')
    returnList.append(word)
    word = ('A letter that starts with ' + firstLetter + ', please')
    while word[0] != firstLetter:
        word = input('A letter that starts with ' + firstLetter + ', please')
    returnList.append(word)
    return(returnList)
print(twoWordsV2(4, 'b'))
#Exercise 3
def geometric(lst):
    common = lst[-1] / lst[-2]
    x = 0
    y = True
    for i in range(len(lst)-1):
        if lst[x] * common == lst[x+1]:
            x = x + 1
            continue
        else:
            y = False
    return(y)
print(geometric([2, 4, 8, 16, 32, 64, 128, 256]))
print(geometric([2, 4, 6, 8]))
#Exercise 4
def Mystery(num):
    count = 0
    while num >1:
        num = num // 2
        count += 1
    return(count)
print(Mystery(4))
print(Mystery(11))
print(Mystery(25))
#Exercise 5
def enterNewPassword():
    digits = "0123456789"
    digit = False
    password = (input("Password"))
    while len(password) < 8 or len(password) > 15 or digit == False:
        digit = False
        for i in password:
            if i in digits:
                digit = True
                break
        if digit == False:
            print("Password must contain at least one digit")
        if len(password) < 8 or len(password) > 15:
            print("Password must be between 8 and 15 characters")
        if digit == True and (len(password) >= 8 and len(password) <=15):
            break
        password = (input("Password"))
    print("Success")
enterNewPassword()
