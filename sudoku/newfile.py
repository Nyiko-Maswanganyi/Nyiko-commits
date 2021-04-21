# N is the size of the 2D matrix   N*N
N = 9
 
# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):
   
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 

def readPuzzle(fileName = 'soduku.txt'):
	L = []
	with open(fileName) as puzzle:
		S =	puzzle.read()
		S = S.replace("\n","").replace(" ","").split("],[")
		L.append(S)
	game2 = []
	for row in L[0]:
		r2 = row.replace("[","").replace("]","").split(",")
		results = list(map(int, r2))
		game2.append(results)
	
	return(game2)

def playGame(grid):
	
	print("Please enter a string in the form row position, column posistion, value e.g. 3,4,9\n Insert # to end the game:\n")
	value = ""
	
	while(value != "#"):
		value = input("Enter Value:\n")
		values = value.split(",")
		row = int(values[0])
		col = int(values[1])
		num = int(values[2])
		if isSafe(grid, row, col, num):
			grid[row][col] = num
		else:
			print("Invalid move")
		printing(grid)
			
			
	
game = readPuzzle()
print(game)
#solveSuduko(game,0,0)
playGame(game)
print(game)


