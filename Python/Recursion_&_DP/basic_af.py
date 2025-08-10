# basic af
def binary_search(arr,key):    
    low = 0
    high = len(arr)
    mid = len(arr) // 2
    for i in range(low,mid):
        if i > mid:
            low = mid
            high = len(arr)
            
        
arr = [5,3,7,6,2]
key = 6
arr.sort() 
ans = binary_search(arr,key)
print("poistion of the thing is: ",ans)