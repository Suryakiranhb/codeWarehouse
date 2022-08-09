arr = []
len = int(input(print("Enter array length")))

for i in range(0,len):
  arr.append(int(input()))

low = 0
mid = 0
high = len-1 

while(mid<=high):
  if arr[mid]==0:
    arr[low], arr[mid] = arr[mid],arr[low]
    low+=1
    mid+=1
  elif arr[mid] == 1:
    mid+=1
  else:
    arr[mid], arr[high] = arr[high], arr[mid]
    high = high-1
  
print(arr)


# INITAL METHOD USED: ANOTHER ARRAY AS PLACEHOLDER 
'''
size = int(input(("Enter the array size: ")))
arr = []
print("Enter the array elements: ")
for i in range(0,size):
  arr.append(int(input()))
#print(arr)

arr2 = []
for i in range(0,size):
  if(arr[i]==0):
    arr2.append(arr[i])

for i in range(0,size):
  if(arr[i]==1):
    arr2.append(arr[i])

for i in range(0,size):
  if(arr[i]==2):
    arr2.append(arr[i])

arr1 = arr2
print(arr1)

'''
