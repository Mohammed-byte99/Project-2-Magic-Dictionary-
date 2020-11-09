def binarySearch(anArray, item):
    LI = 0
    UI = len(anArray)-1
    while LI <= UI:
        MI = (LI + UI) // 2
 
        if (anArray[MI] < item):
           LI = MI + 1
        elif (anArray[MI] > item):
           UI = MI - 1
        else:
           return MI
  
    return -1