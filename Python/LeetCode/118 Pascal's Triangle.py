#118 Pascal's Triangle

#binomial coefficient approach / nCr formula approach
# THIS USES:
'''
Quick mental note: Formula
“Each element = previous element * (row_index - col_index + 1) // col_index”
It's a neat shortcut to compute binomial coefficients iteratively without factorials.
'''
def generate(numRows):
    pascals_triangle =[]
    for i in range(numRows):    
        pascal_row = [1]
        ans = 1
        for j in range(1,i+1):
            ans = ans * (i-j+1) // j   # straight up, this is a formula. This calculates nCr without multiplying those huge numbers.
            pascal_row.append(ans)
        pascals_triangle.append(pascal_row)
    
    return pascals_triangle


numRows = 5
answer = generate(numRows)
print(f"The pascal row for numrow {numRows} is {answer}")


'''
Note:

## Pseudo-steps for iterative, easier approach
1. Initialize result as empty list.  
2. For each row `i` from `0` to `numRows-1`:  
   - Start with `[1]`.  
   - Fill middle using `prev_row[j-1] + prev_row[j]`.  
   - End with `[1]`.  
   - Append to result.  

---

## Complexity
- **Time:** O(n²) (since we build triangle row by row).  
- **Space:** O(n²) (storing full triangle).  

---

## Key Insight
- Each row depends only on the **previous row**.  
- Pascal’s Triangle naturally follows **binomial coefficients**.

'''

# Another way:

from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col) #main part
        ans //= col #main part
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
