#Grid traversal 

def grid_traverse(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = '')
        print()

board = [
  ['A','B','C'],
  ['D','E','F'],
  ['G','H','I']
]

#grid_traverse(board)


def word_search(board,word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i):
        if i == len(word):
            return True

        #check for out of bounds or character mismatch
        if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i]:
            return False
        
        temp = board[r][c] 
        board[r][c] = '#'

        #Now to explore all 4 directions:
        #it is cool here see, we are pupulating the variable based on or condition. So we will have the 
        found_target_character = (backtrack(r+1, c, i+1) or #right
                                  backtrack(r, c+1, i+1) or #down
                                  backtrack(r-1, c, i+1) or #left
                                  backtrack(r, c-1, i+1) #upwards 
                                  )
        
        #restoring the original character
        board[r][c] = temp

        return found_target_character
    
    #starting from every cell:
    for row in range(len(word)):
        for col in range(len(board[0])):
            if backtrack(row,col,0):
                return True
                #we return true and just exit out once we find the target
            
    return False

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"

print(word_search(board, word))  # Output: True
