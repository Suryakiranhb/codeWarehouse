n = int(input("Enter the number of array elements: "))
print("Enter array eleents: ")
a = []

for i in range(0,n):
  a.append(int(input()))

find = int(input("Enter the two sum number you want to find: "))

i=0

for i in range(0,n):
  for j in range(i,n):
    if(a[i]+a[j]==find):
      print(a[i])
      print(a[j])
    else:
      continue
