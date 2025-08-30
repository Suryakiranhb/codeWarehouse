#54. Spiral Matrix

def spiralOrder(matrix):
    # Step 1: Initialization and pointer variable setting
    traversed = []
    #Here, we are just traversing in a spiral order and adding each element reached into a list
    top = 0
    bottom = len(matrix)-1 #2
    left = 0
    right = len(matrix[0])-1 #2
    print("Values rn are ", top,bottom,left,right)

    # Step 2: Traversal using pointer variables
    while top<=bottom and left<=right:
        #traversing from left to right now,
        for i in range(left, right+1):
            traversed.append(matrix[top][i])
        top+=1

        #top to bottom traversal now,
        for i in range(top, bottom+1):
            traversed.append(matrix[i][right])
        right-=1

        #now traversing from the right to the left,
        # just making sure to handle edge case where input is only 1 row:
        if top<=bottom:
            for i in range(right,left-1,-1): #this loop is running in reverse, for obv reasons
                traversed.append(matrix[bottom][i])
            bottom-=1

        #Now traversing from bottom to top
        # same, checking for edge cases
        if left<=right:
            for i in range(bottom,top-1,-1): #this loop is running in reverse, for obv reasons
                traversed.append(matrix[i][left])
            left+=1

    return traversed
def printer(matrix):
    for i in range(0,len(matrix[0])):
        for j in range(0,len(matrix)):
            print(matrix[i][j], end = ' ')
        print()
    print("---------------------------------")

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Original matrix: ")
printer(matrix)
ans = spiralOrder(matrix)
print("The traversal order is: ",ans)



'''
INSIGHTS
Boundary pointers: Always track top, bottom, left, right. These shrink after each traversal.
Traversal order:
Left → Right (across top) → then top += 1
Top → Bottom (down right) → then right -= 1
Right → Left (across bottom) → then bottom -= 1
Bottom → Top (up left) → then left += 1

Edge cases: Always guard with if top <= bottom and if left <= right before traversals #3 and #4 to prevent duplicates when matrix reduces to 1 row/col.

Range detail:
Left→Right: range(left, right+1)
Top→Bottom: range(top, bottom+1) ✅ (easy place to mess up)
Right→Left: range(right, left-1, -1)
Bottom→Top: range(bottom, top-1, -1)

End condition: Loop runs while top <= bottom and left <= right.
Key bug trap: Forgetting the +1 in ranges or missing the boundary checks → causes skipped elements or duplicates.
'''