a = ["Surya","Beidou","Ezio","Ajay Ghale","Artyom"]
#can take any custom array, numbers or names as needed
flag = 0
person = input("Enter the person's name: ")
from_here = int(input("Enter where the person wants to sit: "))
from_here-=1
for i in reversed(range(from_here,len(a))):
  if(flag == 0):
    a.append(0)
    flag = 1
  a[i+1] = a[i]
  if i == from_here:
    a[from_here] = person
    print(i)

print(a)
