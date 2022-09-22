def fun(i,n):
  if(i>n):
    return
  else:
    print()
    fun(i+1,n)
  
start = int(input("Strarting from? "))
end = int(input("ending at? (base condition) "))
fun(start,end)
