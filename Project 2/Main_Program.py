import re
import time
import selection_Function

def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()
    return re.findall(r"[\w']+", textData)

# Load data files into global variables
dictionary = loadWordsFromFile("data-files/dictionary.txt")

# Main Menu
loop = True
while loop:
    # Print Main Menu
    print("Magic Dictionary")
    print("1: Find How Many Words Are In The Dictionary")
    print("2: Is Your Word In the Dictionary?")    
    print("3: What Position Is Your Word At?")
    print("4: What Word Is at Your Position?")
    print("5: What are the Words that Start With the Letter You Give?")
    print("6: How many Words are that Start with the Letter You Give?")
    print("7. How many Words have more that have (User Input)____ letters?")
    print("8. Change every 2nd element with a user inputted word (Only will Print a couple elements due to list size)")
    print("9: Delete any word in the array (Try [aal] to see if the word is gone)")
    print("10: Exit")
    selection = input("Enter menu selection (1-1000): ")

    # Process selection
    if (selection == "1"):
        selection_Function.First_Selection(dictionary)
    elif (selection == "2"):
        selection_Function.Second_Selection(dictionary) 
    elif (selection == "3"):
        selection_Function.Third_Selection(dictionary)
    elif (selection == "4"):
        selection_Function.Fourth_Selection(dictionary)
    elif (selection == "5"):
        selection_Function.Fifth_Selection(dictionary)
    elif (selection == "6"):
        selection_Function.Sixth_Selection(dictionary)
    elif (selection == "7"):
        selection_Function.Seventh_Selection(dictionary)
    elif (selection == "8"):
        selection_Function.Eigth_Selection(dictionary)
    elif (selection == "9"):
        selection_Function.Ninth_Selection(dictionary)
    elif (selection == "10"):
        loop = False
# end while loop
print("Goodbye")
