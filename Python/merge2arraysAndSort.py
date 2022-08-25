a = [-7,12,17,29,41,56,79]
b = [-9,-3,0,5,19]

for i in range(0,len(b)):
  a.append(b[i])

for i in range(len(a)):
  for j in range(i,len(a)):
    if a[i] > a[j]:
      temp = a[i]
      a[i] = a[j]
      a[j] = temp

print(a)
