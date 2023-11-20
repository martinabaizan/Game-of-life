import random

#Welcome and board size
print("Welcome to the Game of Life")
print("What size do you want your grid to be?")
size = int(input()) #input size of the raws and columns
board = [[random.randint(0, 1) for y in range(size)] for x in range(size)] #generate a matrix (list if lists) of size*size with random 1s and 0s

def board_print(board,size): #prints a grid with matrix of 1s and 0s changed to "X" and " "
    for x in range(size + 2):
        print("-", end="")
    print("\n", end="")
    for x in range(size):
        print("|", end="")
        for y in range(size):
            if board[x][y] == 1:
                print("X", end="")
            else:
                print(" ", end="")
        print("|\n", end="")
    for x in range(size + 2):
        print("-", end="")
    print("\n", end="")

def right_neighbours(board,size,x,y):
    neighbours = [] #create an empty list in which the number of neighbours of each coordinate (odrdered as reading) will be appended
    for x in range(size):
        for y in range(size -1):
            neighbours.append(board[x][y+1]) #first column has second column as right neighbours, etc.
        neighbours.append(0) #last column has no right neighbours (compute as 0)
    matrix_right_neighbours = [neighbours[x:x + size] for x in range(0, len(neighbours), size)] #create matrix (10 "sublists" inside list neighbours)
    return matrix_right_neighbours

def left_neighbours(board,size,x,y):
    neighbours = []
    for x in range(size):
        neighbours.append(0) #first column has no left neighbours (compute as o)
        for y in range(size -1):
            neighbours.append(board[x][y]) #second column has first column as left neighbours, etc.
    matrix_left_neighbours = [neighbours[x:x + size] for x in range(0, len(neighbours), size)]  # create matrix
    return matrix_left_neighbours

def below_neighbours(board,size,x,y):
    neighbours = []
    for x in range(size - 1):
        for y in range(size):
            neighbours.append(board[x + 1][y])  # first raw has second raw as below neighbours, etc.
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0) #last raw has no below neighbours (compute as 0)
    nei = neighbours + neighbours0
    matrix_below_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_below_neighbours

def top_neighbous(board,size,x,y):
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0) #first raw has no top neighbours (compute as 0)
    neighbours = []
    for x in range(size-1):
        for y in range(size):
            neighbours.append((board[x][y])) #second raw has first raw as top neighbours, etc.
    nei = neighbours0 + neighbours
    matrix_top_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_top_neighbours

def top_right_neighbours(board,size, x, y):
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0)  # first raw has no top neighbours (compute as 0)
    neighbours = []
    for x in range(size-1):
        for y in range(size-1):
            neighbours.append((board[x][y+1]))
        neighbours.append(0) #last column has no right neighbours (compute as 0)
    nei = neighbours0 + neighbours
    matrix_top_right_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_top_right_neighbours

def top_left_neighbours(board,size, x, y):
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0)  # first raw has no top neighbours (compute as 0)
    neighbours = []
    for x in range(size):
        neighbours.append(0)  # first column has no left neighbours (compute as o)
        for y in range(size-1):
            neighbours.append((board[x][y]))
    nei = neighbours0 + neighbours
    matrix_top_left_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_top_left_neighbours

def below_right_neighbours(board,sizex, x, y):
    neighbours = []
    for x in range(size-1):
        for y in range(size-1):
            neighbours.append(board[x+1][y+1])
        neighbours.append(0) #last column has no right neighbours (compute as 0)
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0)  # last raw has no below neighbours (compute as 0)
    nei = neighbours + neighbours0
    matrix_below_right_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_below_right_neighbours

def below_left_neighbours(board,size, x, y):
    neighbours = []
    for x in range(size-1):
        neighbours.append(0)  # first column has no left neighbours (compute as o)
        for y in range(size-1):
            neighbours.append(board[x+1][y])
    neighbours0 = []
    for i in range(size):
        neighbours0.append(0)  # last raw has no below neighbours (compute as 0)
    nei = neighbours + neighbours0
    matrix_below_neighbours = [nei[x:x + size] for x in range(0, len(nei), size)]  # create matrix
    return matrix_below_neighbours

neighbours = [[0 for y in range(size)] for x in range(size)] #create a size*size matrix of 0s.

def board_compute_next_step(board,size):
    next_board = [[0 for y in range(size)] for x in range(size)] #create a size*size matrix of 0s.
    for x in range(size):
        for y in range(size):
            neighbours[x][y] = right_neighbours(board, size, x, y)[x][y] + left_neighbours(board, size, x, y)[x][y] + \
                               top_neighbous(board, size, x, y)[x][y] + below_neighbours(board, size, x, y)[x][y] + \
                               top_right_neighbours(board, size, x, y)[x][y] + \
                               top_left_neighbours(board, size, x, y)[x][y] + \
                               below_right_neighbours(board, size, x, y)[x][y] + \
                               below_left_neighbours(board, size, x, y)[x][y] #add all neighbours matrices and store result into neighbours matrix
            #From neighbours matrix, create next matrix following the rules:
            #Any live cell with fewer than two live neighbours dies, as if by under-population
            if neighbours[x][y] < 2:
                next_board[x][y] = 0
            #Any live cell with two or three live neighbours lives on to the next generation
            if neighbours[x][y] == 2 or neighbours[x][y] == 3:
                next_board[x][y] = 1
            #Any live cell with more than three live neighbours dies, as if by overpopulation
            if neighbours[x][y] > 3:
                next_board[x][y] = 0
            #Any dead cell with exactly three neighbours becomes a live cell, as if by reproduction
            if neighbours[x][y] == 3:
                next_board[x][y] = 1
    return next_board

#Simulate steps and print the board
while True:
    board_print(board, size) #prints board
    print("Continue simulation (y/n) ?")
    answer = input()
    if answer == "n": #if input is "n" break the loop
        break
    else:
        next_board = board_compute_next_step(board, size) #reset board
        board = next_board