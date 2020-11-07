def underpop(array,row,col):
    '''
    Rule: less than two live neighbours -> underpoluation (death)
    
    check all surrounding cells
    if sum of neighbours < 2
    return true (underpopulation)
    else (n>2)
    return false (not underpopulation)
    '''

    if checkNeighbours(array,row,col) < 2:
        return True
    else:
        return False


def overpop(array,row,col):
    '''
    Rule: more than three live neighbours -> overpopulation
    
    check all surrounding cells
    if sum of neighbours > 3
    return true (overpopulation)
    else (n<3)
    return false (not overpopulation)
    '''
    # TODO: fix failed test

    if checkNeighbours(array,row,col)>3:
        return True
    else:
        return False


def repro(array,row,col):
    '''
    Rule: exactly three live neighbours -> reproduction

    check all surrounding cells
    if sum of neighbours is 3
    return true (reproduction)
    else (!= 3)
    return false (no reproduction)
    '''
    if checkNeighbours(array,row,col) == 3:
        return True
    else:
        return False

# def remainAlive(array,row,col):
#     '''
#     May not need this? This is no change. yeah i guess this is covered by the other 3
#     '''
    

def checkNeighbours(array,row,col):
    '''
    
    '''
    neighbours = 0
    for m in range(-1,2):
        newRow = row + m
        for n in range(-1,2):
            newCol = col + n
            if newRow<len(array) and newRow>0 and newCol<len(array[0]) and newCol >0 and (m == 0 and n == 0): #yuck
                if array[newRow][newCol] == 1:
                    neighbours+=1
    return neighbours


def play(inputArray):
    '''
    
    '''
    for row in range(len(inputArray)):
        for col in range(len(inputArray)):
            if overpop(inputArray,row,col) or underpop(inputArray,row,col):
                inputArray[row][col] = 0
            elif repro(inputArray,row,col):
                inputArray[row][col]= 1


def print_cell(input_array):
    for i in input_array:
        for e in i:
            print(e, end=' ')
        print('')



if __name__ == '__main__':
    inputArray = [[0,0,0,0],[1,1,0,0],[0,0,1,0]]
    #maybe multiple iterations (hongmei agrees, let's not run it forever :D)
    for iter in range(1, 5):
        play(inputArray)
    
    print_cell(inputArray)
    play(inputArray)
    for x in inputArray:
       print(x)