arr = []
len = int(input("Enter the length of the array: "))
for i in range(0,len):
  arr.append(int(input()))

print(arr)
print("Press 1 for with sorting, 2 for without sorting")
withSort = int(input())


if(withSort == 1):
  for i in range(0,len):
    for j in range(i,len):
      if(arr[i]>arr[j]):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      else:
        continue

  print("Sorted type used")
  print("The sorted array: {}".format(arr))
  print("The minimun number in the array is {}, and the maximum is {}".format(arr[0],arr[len-1]))

else:
  min = arr[0]
  max = arr[0]
  for i in range(0,len):
    if(arr[i]<min):
      min = arr[i]
    else:
      continue
    
  for i in range(0,len):
    if(arr[i]>max):
      max = arr[i]
    else:
      continue

  print("Unsorted type used")
  print("The array is not sorted: {}".format(arr))
  print("The minimum number in the array is {} and the maximum number is {}".format(min,max))
