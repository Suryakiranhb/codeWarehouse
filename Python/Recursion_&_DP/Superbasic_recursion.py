def fun(i,n,string):
  if(i>n):
    return
  else:
    print(string)
    fun(i+1,n,string)

string = input()
times = int(input("How many times do you wanna print your name?"))
fun(1,times,string)
