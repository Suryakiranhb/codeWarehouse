size = int(input("Enter the size of the array: "))
print("Enter the elements: ")
arr = []

for i in range(0,size):
  arr.append(int(input()))

pos = 0
for i in range(0,size):
  if arr[i]<0:
    arr[i], arr[pos] = arr[pos], arr[i]
    pos+=1
  else:
    continue 

print(arr)
