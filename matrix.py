mainLoop = True #establish main loop
def greeting():
    print('This program solves for the determinant of an NxN matrix')
    
def FirstRowInput():
    keepInputting = True

    rowOne = []
    while keepInputting is True:
        answer = input('Would you like to input a value to the first row of the matrix? (y/n): ' )
        if answer != "y" :
            keepInputting = False
            print()
        else :
            n1= float(input('What value would you like to add? : '))
            rowOne.append(n1)
        print(rowOne)
        print()
    return rowOne

def rowInput(n):

    rowJ = []
    k = 0
    for k in range(0,n):
        nJ= float(input('What value would you like to add? : '))
        rowJ.append(nJ)
        print(rowJ)
    return rowJ
def determinant(n, jRows):
    if #sry didnt finish v1 :(
        
    

jRows = []
while mainLoop == True:
    RowOne = FirstRowInput()
    jRows.append(RowOne)
    print(jRows[0])
    n = len(RowOne) #decides number of rows
    
    j = 0
    for j in range(0,n-1):
        print()
        rowJ = rowInput(n)
        print()
        jRows.append(rowJ)
        k = 0
        j = j+1
    print('Matrix: ')
    for k in range(0,n-1):
        print(jRows[k])
        k+1
    print(jRows[n-1])

# i switched to a different approach bc this one kinda sucked, i realized
#it was gonna be incredibly tedious using the matrix I set up, or atleast
#i think it would be, 
