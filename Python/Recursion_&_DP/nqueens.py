#N-Queens
#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other

def solve_nqueens(n):
    results = []
    board = [["." for _ in range(n)] for _ in range(n)]
    #for i in board:
    #    print(i)

    def backtrack(row, cols, pos_diags,neg_diags):
        if row == n: 
            solution = [''.join(r) for r in board]
            results.append(solution)
            return
        
        for col in range(n):
            if col in cols or (row+col) in pos_diags or (row-col) in neg_diags:
                continue
                
            # If it comes to this part, we know for sure that it doesnt have any queen in the same row, column or diagonal. So, we place the queen.
            board[row][col] = 'Q'
            cols.add(col)
            pos_diags.add(row+col)
            neg_diags.add(row-col)
            
            # Now, to find the rest of the places where we can place the queen (if it can be placed), given that we have placed the queen now in this poistion 
            backtrack(row+1, cols, pos_diags, neg_diags)

            #Remove the queen as you go back after failing to fill queen. (because if you did place queen in all 4 rows, you would append to solution and return)
            board[row][col] = '.'
            cols.remove(col)
            pos_diags.remove(row+col)
            neg_diags.remove(row-col)
    
    backtrack(0, set(), set(), set())
    return results


ans = solve_nqueens(4)
for i in ans:
    print("N Queens placement variation so that they dont attach each other: ")
    print(i)

