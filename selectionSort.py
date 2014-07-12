__author__ = 'pwalker'
#!/usr/bin/python

#Selection Sort
#@param list: A list of unsorted integers
def selectionsort2( list ):
    for i in range( len(list)):
        tny = i; #store current
        for j in range(i+1, len(list)): #check one ahead

            if list[j] < list[tny]:
                tny = j #store smallest spot

        swap(list, tny, i)#Swap spots

    #display final list
    for h in range(len(list)):
        print h, ":", list[h]

#Swap
#@param A: list
#@param x: first # to swap
#@param y: second # to swap
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

#########################
#End of Member Functions#
#########################

#Execute Application
myList = [3, 1, 6, 9, 2, 10, 4]
selectionsort2(myList)
