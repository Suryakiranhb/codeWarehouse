def solveSudoku(board):
    # To check if we can actually place the number or not, first by checking the horizontal and vertical line of the board,
    # Then checking the 3x3 board of where we want to place the number 
    def is_valid(r, c, char):
        #this scope, is limited to that 3x3 board, and the horizontal and vertical lines coming out from that 3x3 board
        for i in range(9):
            # Now checking vertical and horizontal lines
            if board[r][i] == char or board[i][c] == char:
                return False
            #Now checking the whole 3x3 board
            if board[3*(r//3) + i//3] [3*(c//3) + i%3] == char:
                return False
        return True
    
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # Now we are sure that here, we can start placing as it is '.'
                    for char in '123456789':
                        if is_valid(r,c,char):
                            board[r][c] = char
                            # Recursion happens from here. The board gets updated per recursion
                            if backtrack():
                                return True
                            # In case we are unable to place, we remove the number while backtracking
                            board[r][c] = '.'
                    return False
        return True
    
    backtrack()


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)

# Print the solved board
for row in board:
    print(row)

                            