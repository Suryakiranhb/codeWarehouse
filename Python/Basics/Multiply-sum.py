a = int(input())
b = int(input())

def calc(a,b):
  c = a*b
  if(c<=100):
    return c
  else:
    return a+b

calc(a,b)
