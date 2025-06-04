a_len = int(input("Enter the length of array 1 dimension"))
a = []
for i in range(0, a_len):
    cols = []
    jagged_len = int(input("Enter the jagged array {}'s length: ".format(i)))
    for j in range(0,jagged_len):
        cols.append(int(input()))
    print(cols)    
    a.append(cols)


print(a)
