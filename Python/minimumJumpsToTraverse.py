a = [1, 4, 3, 2, 6, 7]
'''
n = int(input("Enter n value "))
print("Array values enter madi: ")
for i in range (0,n):
   a.append(int(input()))
'''

jump = 0   
for i in range(0, len(a)):
  if i+a[i]<=len(a):
    i = i+a[i]
    jump+=1
  if i+a[i]>len(a):
    #jump+=1
    break
  else:
    jump+=1
#print(a)
print(jump)
