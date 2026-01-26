# we will use dictionaries to store the sum data, per index. If any sum value already exists previously in the dictionary, 
# it would mean that until that point, the sum is zero. We will then retrieve the first place where that same sum value was found,
# and then calculate the elements between that and the current element. We keep a max variable we update to have it store the maximum
# length. By the end of traversing the array, we will be left with the maximum size giving sum 0 
import sys
def longestSum0(arr):
    sumLogDict = {} #initializing dict
    sumVal = 0 #stores the sum values
    sumLogDict[0] = -1 #making sure that the value before the list starts is zero
    maxLen = 0 # stores the max length where sum is zero
    for i in range(0,len(arr)):
        #print(sumLogDict)
        sumVal += arr[i]
        if sumVal not in sumLogDict:    
            sumLogDict[sumVal] = i
        else:
            # we now know that the sumVal is present in the dict. Now to extract its value and check the length
            position = sumLogDict.get(sumVal)
            len_diff = i - position
            if len_diff > maxLen:
                maxLen = len_diff

    print("dict" ,sumLogDict)
    print("MaxLen now contains: ",maxLen)
    return maxLen
            
arr = [9, -3, 3, -1, 6, -5]
ans = longestSum0(arr)

''' 
What im doing:
I use a prefix sum and a hashmap to store the first occurrence of each sum.
If the same sum appears again, the elements between them sum to zero.
I track the maximum distance between such indices.
'''