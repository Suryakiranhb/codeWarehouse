a = []
n = int(input("Enter the length of the array: "))
for i in range(0,n):
  a.append(int(input("Enter the {}th element: ".format(i+1))))

print(a)

lastElement = a[len(a)-1]
for i in reversed(range(0,len(a))):
  if i == 0:
    a[i] = lastElement
  else:
    a[i] = a[i-1]
  

print("The cyclically rotated array is: {}".format(a))
