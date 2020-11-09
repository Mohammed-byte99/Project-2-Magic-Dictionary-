import binary_function


def First_Selection(dictionary):
    print("Length of array:", len(dictionary))


def Second_Selection(dictionary):
    cool = input("Word: ")
    index = binary_function.binarySearch(dictionary, cool)
    if (index == -1):
        print("Shame. Your word is so dumb, that it isnt in the dictionary.")
    else:
        print("Hey, Your word ", cool, " is in the dictionary!")


def Third_Selection(dictionary):
    cool = input("Word: ")
    index = binary_function.binarySearch(dictionary, cool)
    if (index == -1):
        print("Error. Word is not in Dictionary.")
    else:
        print("Your word ", cool, " is at position ",
              index, " in the dictionary!")


def Fourth_Selection(dictionary):
    cool = int(input("Position: "))
    print(dictionary[cool])


def Fifth_Selection(dictionary):
    check = input("Letter: ")
    cool = []
    for i in range(len(dictionary)):
        if (dictionary[i])[0] == check.lower():
            cool.append(dictionary[i])
    # print result
    print("The list of matching first letters are: " + str(cool))


def Sixth_Selection(dictionary):
    check = input("Letter: ")
    count = 0
    for i in range(len(dictionary)):
        if (dictionary[i])[0] == check.lower():
            count += 1
    # print result
    print("There are ",  str(count), "elements with the same matching first letter")


def Seventh_Selection(dictionary):
    number = int(input("How Many Letters : "))
    if (number == 1):
        count = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) == 1:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 1 letter")
    elif (number == 2):
        count = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) == 2:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 2 letters")
    elif (number == 3):
        count = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) == 3:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 3 letters")
    elif (number == 4):
        count = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) == 4:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 4 letters")
    elif (number == 5):
        count = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) == 5:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 5 letters")
    elif (number >= 6):
        count = 0
        for i in range(len(dictionary)):
            if (dictionary[i]) >= 6:
                count += 1
        # print result
        print("There are ",  str(count), " words which have 6 letters or more")

def Eigth_Selection(dictionary):
    cool = input("Word: ")
    dictionary2 = ""
    index = 0
    for word in dictionary:
        if index % 2 == 1:
            dictionary2 += " " + cool + " "
        else:
            dictionary2 += word 

        index += 1

    print(dictionary2 [0:44])
    print(dictionary2 [11234: 11294])

def Ninth_Selection(dictionary):
    cool = input("Word: ")
    index = binary_function.binarySearch(dictionary, cool)
    if (index == -1):
        print("Error. Word is not in Dictionary.")
    else:
        print ("Before: ", dictionary[0:10])
        dictionary.remove(cool)
        print("Your word", cool, " was deleted at position ", index, " in the dictionary!")
        print("After: ", dictionary[0:10])
    

    

      