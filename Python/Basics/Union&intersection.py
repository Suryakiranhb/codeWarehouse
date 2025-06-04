a = [1,2,3]
b = [5,4,3,2,1]
c = []
#c is used for intersection list, and a is used for union list since,
#elements of b are appended to it anyway

for i in range(0,len(b)):
  a.append(b[i])

for i in range(0,len(a)):
  for j in range(i,len(a)-1):
    if a[i]==a[j+1]:
      c.append(a[j+1])
      #in the above line, a[i] could have been appended to c[] tuu since both are the same
      del a[j+1]
    else:
      continue

#del a[1]
print("Union is: {} and the intersection is {}".format(a,c))
