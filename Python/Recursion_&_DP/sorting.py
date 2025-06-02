############## S O R T I N G ##############
def selection_sort(arr):
    # traverse through the list, get the least number, and then swap that number with the first element. 
    # Move on to the second element in the list and continue comparing it with the rest of the elements, and swap that with the second element.
    # Continue doing this until you reach the end of the list, at which point, youll end up with a sorted list
    print("len(arr)-1 th element: ",arr[len(arr)-1])
    print("len(arr) gives: ",len(arr))
    for i in range(0,len(arr)): 
        # note that in python, the range function's second parameter is not inclusive in range(0,len(arr)). 
        # I.e, you dont need to write len(arr)-1. if there are 6 elements in the array, the range function will run till 0 to 5 here as len(arr) will give 6, 
        # and hence everything before that is taken. 6 is not included.
        least_value = i
        for j in range(i,len(arr)):
            #finding minimum:
            if arr[j]<arr[least_value]:
                least_value = j
        print("The the least element in array after ",i,"th sorting run: ",least_value)
        #now we swap least element with the element in ith position
        temp = arr[i]
        arr[i] = arr[least_value]
        arr[least_value] = temp
        print("Arr after swap on run ",i, " is ", arr)
        # now, we have the least valued element after i, stored in least_value variable. swap its element with arr[i]
    print("Final sorted array: ",arr)
    return

def bubble_sort(arr):
    # here, we will compare 2 elements like, 0 and 1 then 1 and 2 and so on, if they are not in ascending,descending order, we swap them and go to next position and do the same
    # we continue to do this till n-1 times and at the end, the array will be sorted
    print("reachjed")
    j = len(arr)-1
    # len(arr)-1 is important here because if it gets to the last element, what will it compare to? There wont be any next element to compare and swap. 
    # So in bubble sort, we traverse till one short of the usual last index
    while(j>0):
        print("j value: ",j)
        for i in range(0,j): 
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            else:
                continue
            print("Array after the ",i,'th iteration of sorting: ',arr)
        j-=1
    print("Final sorted array: ",arr)
    
def insertion_sort(arr):
    # here we will go ffrom left to right, and for each iteration, we take the element and swap it with somewhere it should be present in in the left section. We are preparing our sorted array as we traverse
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            counter = j
            while(counter>0):
                if arr[counter]>arr[j]:
                    counter-=1
                else:
                    print("arr(counter) that needs swapping its -1 is ",arr[counter])
                    temp = arr[counter+1]
                    arr[counter+1] = arr[j]
                    arr[j] = temp
                    counter-=1
        print("Arr after ",i,"th iteration: ",arr)
    print("Final sorted arr: ",arr)

def insertion_sort2(arr):
    for i in range(0,len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    print("Final sorted array: ",arr)

def merge_sort(arr):
    low = 0
    high = len(arr)
    # arr passed is currently [9, 4, 7, 6, 3, 1, 5]
    def mergesort(arr,low,high):
        print("low and high values passed: ",low,high)
        if low>=high:
            return
        mid = int((low+high)/2)
        mergesort(arr,low,mid)
        print("baCK FROM RECURSION, THE ARRAY NOW IS: ",arr)
        mergesort(arr,mid+1,high)
        print("merge is passedthese values (arr,low,mid,high) :",arr,low,mid,high)
        merge(arr,low,mid,high)
    
    def merge(arr,low,mid,high):
        print("merging olage arr currently: ",arr)
        temp = []
        left = low
        right = mid+1
        # now, this function is where all the magic happens, whatever is there in mergesort itll all come back here
        # we have two halves of the list, low...mid and mid+1...high
        while(left<=mid and right<=high):
            # we are now traversing both halves of the list, appending to temp the lowest of the 2 numbers present in the position pointed in the list
            print("left and right values: ",left,right)
            if(arr[left]<=arr[right]):
                temp.append(arr[left])
                #since we have now added left half's element to the temp array, we move the pointer to the next element in the list to again compare and add to temp
                left+=1 
            else:
                temp.append(arr[right])
                #same with right in case right was smaller instead of left
                right+=1
            
            # now lets say we run out of elements in either of the two halves of the arrays. We dont need to compare anymore since the halves by themselves are sorted
            # we just add whats remaining in the array having elements remaining to the temp array

            #copying left out elements from the left half in case there are any:
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        
        #copying left out elements from the right half in case there are any:
        while(right<=high):
            temp.append(arr[right])
            right+=1
            
            # Now we need to place this sorted temp array back into the main array (This is still a recursion call so we need to add it back to main array until the array is whole again)
        for i in range(low,high):
            arr[i] = temp[i-low]
        
    mergesort(arr,low,high)
    print("Sorted array: ",arr)
    return


def merge_sort_custom(arr):
    low = 0
    mid = int((low+len(arr))/2)
    high = len(arr)
    print("low, mid and high values are: ",low,mid,high)
    #now lets split the array into 2 halves recursively
    def splitter(arr,low,high):
        if low>=high:
            print("ending recursion when low and high are",low,high," respectively")
            print("arr is currently: ",arr)
            return
        mid = int((low+high)/2)
        print("Mid value: ",mid)
        splitter(arr,low,mid)
        print("After first set of recursion for 1st part of array, we have arr, low and mid as: ",arr,low,mid)
        splitter(arr,mid+1,high)
        print("After second set of recursion for 1st part of array, we have arr, low and mid as: ",arr,low,mid)
    
    def merger(arr,low,mid,high):
        temp = [] #initialize an empty array
        left = low
        right = mid+1

        #while(left<=mid and right<=high):

    splitter(arr,low,high)


def recursion_sort(arr):
    print()

############## D R I V E R S ##############
arr = [13,46,24,52,20,9]
arr2 = [9,4,7,6,3,1,5]
merge_sort_arr = [38, 27, 43, 10] 
#selection_sort(arr)
#bubble_sort(arr)
#insertion_sort2(arr)
#merge_sort_custom(merge_sort_arr) #need to come back to it later
merge_sort(merge_sort_arr)

recursion_sort(arr)