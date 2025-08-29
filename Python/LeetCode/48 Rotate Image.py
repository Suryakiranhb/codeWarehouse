#48. Rotate Matrix by 90 degrees
def rotate(matrix):
    # transpose the matrix and then mirror all the rows and you will be left with a 90 degree rotated matrix
    def printer():
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):
                print(matrix[i][j], end = ' ')
            print()
        print("---------------------------------")
    
    # Original matrix:
    print("Original matrix: ")
    printer()

    # We just swap all the elements across the diagonal axis to transpose. These are the diagonal elements here:
    for diag in range(0,len(matrix)):
        print("diagonal elements: ",matrix[diag][diag])
    
    # Step 1: Transpose
    n = len(matrix)
    for i in range(0,n):
        for j in range(i+1, n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    print("Transpose is complete: ")
    printer()

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
    print("Matrix is now reversed and it should now be flipped 90 degrees: ")
    printer()

    
    


matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = rotate(matrix)

"""
INSIGHT:
Q: How do you rotate an n x n matrix 90° clockwise in place?
A:Transpose → swap matrix[i][j] with matrix[j][i] for all i < j.
Reverse each row → gives the final rotated matrix.
Time = O(n²)
Space = O(1)
Trick: Transpose aligns rows to columns, reversing rows finishes the rotation.
"""