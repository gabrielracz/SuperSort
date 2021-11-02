#!/usr/bin/env python3

import math
from SimpleGraphics import *
import random
import time

setAutoUpdate(False)

def selectionSort(alist):
    n = len(alist)
    for x in range(n):
        unsortedIndex = x   #Unsorted section index (sort 1 number per pass)
        low = x
        for i in range(x+1, n):     #Find lowest value after unsorted index
            if alist[i]< alist[low]:
                low = i
            draw(alist,low,i)
        if low != x:    #Swap the lowest value with the unsorted index value
            alist[low], alist[unsortedIndex] = alist[unsortedIndex], alist[low]
            draw(alist,unsortedIndex,low,True)
            continue
    draw(alist)
    return alist



def bubbleSort(alist):
    swapped = True
    n = len(alist)
    while swapped == True:
        swapped = False
        for i in range(1, n):
            if alist[i-1] > alist[i]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
                swapped = True
                draw(alist,i-1,i,True)
                continue
            draw(alist,i-1,i)
        n -= 1
        draw(alist)
    return alist
    
def combSort(alist):
    shrink = 1.3
    gap = len(alist)
    sort = False
    
    while sort == False: 
        gap = int(gap/shrink)
        if gap > 1:
            sort = False
        elif gap < 1:
            gap = 1
            sort = True
        
        i = 0
        while gap + i <= len(alist)-1:
            if alist[i + gap] < alist[i]:
                alist[gap + i],alist[i] = alist[i], alist[gap + i]
                draw(alist,i,gap+i, True)
                sort = False
                i += 1
                continue
            draw(alist,i,gap+i)
            i += 1
    draw(alist)
    return alist
    
def quicksort(alist):
    quicksorthelper(alist,0, len(alist) - 1)
    draw(alist)
    return alist
    
def quicksorthelper(alist, lo, hi):
    if lo < hi:
        p = partition(alist,lo,hi)
        quicksorthelper(alist,lo, p)
        quicksorthelper(alist,p+1, hi)
    return alist    

def partition(alist, low, high):
    #pivotOptions = [alist[low],alist[low//high], alist[high]]
    #pivot = median(pivotOptions)
    pivot = alist[random.randint(low,high)]
    i = low - 1
    j = high + 1
    while True:
        i+= 1
        j -= 1
        while alist[i] < pivot:
            i += 1
            draw(alist,i,j)
        while alist[j] > pivot: 
            j -= 1
            draw(alist,i, j)
        if i >= j:
            return j
        draw(alist,i,j,True)
        alist[i],alist[j] = alist[j],alist[i]

def median(pivotOptions):
    pivotOptions.sort()
    return pivotOptions[1]

def draw(alist, target1=None, target2=None, found = False, pivot = None):
    global sleeptime, listsize
    clear()
    time.sleep(sleeptime)
    for i in range(len(alist)):
        setColor(255,255,255)
        setOutline(255,255,255)
        if i == target1 or i == target2:
            if found == True:
                setColor(0,225,80)
                setOutline(0,225,80)
            else:
                setColor(250,0,50)
                setOutline(250,0,50)
        if target1 == None:
            setColor(255,255,255)
            setOutline(255,255,255)
            rect(i*(800/listsize), 600, (800/listsize), alist[i]*-(600/listsize))
        rect(i*(800/listsize), 600, (800/listsize), alist[i]*-(600/listsize))
    update()
    return
    
def shuffle(alist):
    shuffled = []
    while len(alist) > 0:
        index = random.randint(0, len(alist) - 1)
        shuffled.append(alist.pop(index))
    return shuffled

def createlist():
    global listsize
    alist = []
    for i in range(listsize):
        alist.append(i+1)
    alist = shuffle(alist)
    return alist
    

background(0,0,0)
choice = ""
sleeptime = 0
listsize = 175
print("\nWhat would you like to see? (q to quit, l for list size, t for time delay)\n 1. Selection Sort\n 2. Bubble Sort\n 3. Comb Sort\n 4. Quicksort")
while choice != "q":
    alist = createlist()
    draw(alist)
    choice = input("")
    start = time.time()
    if choice == "1":
        selectionSort(alist)
    if choice == "2":
        bubbleSort(alist)
    if choice == "3":
        combSort(alist)
    if choice == "4":
        quicksort(alist)
    if choice == "l":
        listsize = int(input("List size: "))
        continue
    if choice == "t":
        sleeptime = float(input("Time delay (in seconds): "))
        continue
    if choice == "q":
        close()
        quit()
    end = time.time()
    elapsed = end - start
    print("{:.3f}".format(elapsed) + " seconds")
    time.sleep(1)
    
































