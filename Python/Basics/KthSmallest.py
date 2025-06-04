arr = []
len = int(input("Enter the length of the array: "))
for i in range(0,len):
  arr.append(int(input()))

k = int(input("Enter the value for K. It should be <= the length of the array: "))

for i in range(0,len):
  for j in range(i,len):
    if(arr[i]>arr[j]):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp

print(arr)
print("The Kth smallest element is {}".format(arr[k-1]))
