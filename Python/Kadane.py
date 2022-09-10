def kadane_pls_hlp(a):
  # ok I am Kadane and I will help you :)
  sum = 0
  biggest_sequence = []
  for i in range(len(a)):
    sum+=a[i]
    if sum<=0:
      sum = 0
      biggest_sequence = []
    else:
      biggest_sequence.append(a[i])
      continue

  flag = 0
  if(len(biggest_sequence)==0) :
    biggest = a[0]
    for i in range(0,len(a)):
      if a[i]>biggest:
        biggest = a[i]
    print(biggest)
    flag = 1

  if(flag !=1 ):
    return(biggest_sequence,sum)
  else:
    return(biggest)
  #there you go! :) 

arr = [1,2,3,-2,5]
kadane_pls_hlp(arr)

# test arrays to give Mr.Kadane :
# [1,2,3,-2,5]
# [1,3,-4,4,3,5,-4,2,3]
# [-1,-2,-3,-4]
