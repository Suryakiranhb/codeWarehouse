a = [1,3,4,2,2]
'''
n = int(input("Enter n value "))
print("Array values enter madi: ")
for i in range (0,n):
   a.append(int(input()))
'''
flag = 0
for i in range(0,len(a)):
  for j in range(i,len(a)):
    if(a[i] == a[j] and i!=j):
      print("Found repeat of {} at pos {}".format(a[i], j))
      flag = 1
      break
    else:
      continue

if flag == 0:
  print("No match found, all elements")
