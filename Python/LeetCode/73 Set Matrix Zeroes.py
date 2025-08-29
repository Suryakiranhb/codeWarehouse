# 73. Set Matrix Zeroes
#bruteforce -> traverse the matrix, wherever you find a 0, mark its row and column elements as -1. If yu encounnter a 0 while marking, dont touch it.
def setZeroes(matrix):
    # m and n values calculation
    row_length = len(matrix)
    col_length = len(matrix[0])

    zero_rows = []
    zero_columns = []
    for row in range(0,row_length):
        for col in range(0,col_length):
            print(matrix[row][col])
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_columns.append(col)

    # we now know where zeroes are present, now we need to make that entire row and entire column as zeroes
    print(f"zero rows are: {zero_rows}")
    print(f"zero cols are: {zero_columns}")    

    #now, for zeroing, the thing is if we encounter any zero in any list within the list, it will be fully zeroes cuz of horizontal zeroing
    # for vertical zeroing, we would need to zero on the same position in all the other lists
    for row in range(0,row_length):
        if row in zero_rows:
            for col in range(0,col_length):
                matrix[row][col] = 0
        else:
            for col in range(0,col_length):
                if col in zero_columns:
                    matrix[row][col] = 0
    
    return matrix

'''
Inisght:
we are traversing the matrix and noting down the row and the column position where we found the zeroes.
Then once we have that master key sort of a list, we then traverse the matrix again and replace the entire row if its present in key, and the column value in other rows if that column value is present in key


Better approach:
A better approach to this would be to keep 2 lists, row_list and col_list. We traverse the matrix as usual, in whichever row,col value we find zero at, 
we take note of that in that row_list[row] and col_list[col].
Then after traversal is done, we again traverse the matrix. This time, if we find row and col of matrix[row][col] to be marked in the row_list and col_list, we simply turn them into zero.
This saves us a for loop, because in my code, we are having 2 for loops to replace zeroes (even though it runs on a conditional, still the row_list col_list appproach is better)

Catch:
The thing is, still, these take up memory. Mine takes 2 variables, and the better approach takes 2 lists. So we need to have an optimal solution

Optimal:
so, the optimal solution is nothing but the better approach but instead of using the 2 lists, we do it using the already existing matrix's 0th positions itself. i.e., 
By treating the first row of the matrix as row_list and the first column of the matrix as col_list. But note that matrix[0][0] would have to store the values of both row_list[0]
and col_list[0] values. This is wrong. So, we use a variable called row_0 to store only the value of what would be stored in row_list[0]. 

Now, after we get the row_list and col_list within the matrix itself after traversal is complete, we go ahead and traverse the matrix except the [0][j] and [i][0] places, and 
change into zeroes as per better approach. 
Coming to 0th row and col, we do first the row and then the column so as to not cause any unwanted changes in the 0th row/column as that itself is used to store the zero flags

'''
def setZeroes_usingMatrixItself(matrix):
    m, n = len(matrix), len(matrix[0])
    
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # use first row/col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # zero out cells based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    # handle first col
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
    
    return matrix

'''
Key insight:
Use the first row and first column as "flags" to track which rows/columns should become zero. Keep two booleans to remember if the first row/col themselves must be zeroed.
'''



matrix = [[1,1,1],[1,0,1],[1,1,1]]
ans = setZeroes_usingMatrixItself(matrix)
print(f"The zeroed in matrix would be : ",ans)