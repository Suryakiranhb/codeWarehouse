def recursion_print(n):
    if n>0:
        print(n)
        recursion_print(n-1)
    else:
        return

def recursion_print_backtracking(name, num):
    if num>0:
        recursion_print_backtracking(name,num-1)
        print(name)
        return
    
def n_to_1(n):
    if n>0:
        print(n)
        n-=1
        n_to_1(n)
    return

def sum_of_n_numbers(num): #This function itself returns the sum of N numbers
    value = 0
    if num==0:
        return 0
    else:
        return num + sum_of_n_numbers(num-1) #return part is where all the magic happens here in sum. We are backtracking with the adds

def sum_of_numbers_parameterized(n,sum):
    if n<1:
        print(sum)
        return
    else:
        n-=1
        print("n and sum rn: ",n,sum)
        sum_of_numbers_parameterized(n,sum+n) #this gets called s_o_n_p(4,5) -> sonp(3,9) -> sonp(2,12) -> sonp(1,14) -> sonp(0,15) then fails on if condition so returns n

def sum_recursion_parameterized_2(n,sum): #this one works fine
    if n<1:
        print("Sum of n recursion: ",sum)
        return
    print("n and sum rn: ",n-1,sum+n)
    sum_recursion_parameterized_2(n-1,sum+n) #we are decrementing i to hit the base case, along with that we are adding to the sum variable, each of the number we go on decrementing till we hit 0, and exit out of the base condition

def factorial(num):
    if num==0:
        return 1
    else:
        print("num :",num )
        return num * factorial(num-1)  
        #CALLS fact(4) -> fact(3) -> fact(2) -> fact(1) -> base case execution, so returns 1
        # 1 * 120 <- 2*60 <- 3*20 <- 4*5  <- 5*1 RETURNS

def factorial_2(num):
    if num == 0:
        return 1
    else:
        return num * factorial_2(num-1)
    
def factorial_custom(fact, num):
    if num == 0:
        print("Factorial is: ", fact)
        return
    else:
        print("Value in fact and num are: ",fact,num)
        factorial_custom(fact*num,num-1) #note that in fact, it has to be entered as 1 since if we multiply initially with 0, we'll keep on getting zero upon each increment and mutiplication cycle

def rec_rev_array(n,arr):
    #n is the number of items in the array, you gotta iterate till 0 and each time, reversing the array
    #BUT, since we are exchanging elements of the array, i only gotta iterate till len(array)/2 since by the time we reach the midpoint of the array, all elements will be mirror exchanged
    if n==int(len(arr)/2):
        print("length of array/2 value upon exit: ",len(arr)/2)
        print("exiting when n's value got: ",n)
        print("Reversed array: ",arr)
        return
    else:
        temp = arr[n-1]
        arr[n-1] = arr[len(arr) - n]
        arr[len(arr)-n] = temp
        print("n value and the len(arr)-1 value is: ",n,len(arr)-1)
        print("We are passing this array into next iteration: ",arr)
        n-=1
        rec_rev_array(n,arr)

def rec_palin_check(string,n):
    def recursive_palindrome_check(string,n):
        print("String and n value passed in the recursion call: ",string, n)
        reversed_string = "placeholder"
        if n == int(len(string)/2): 
            #this will go until n/2 times and capture the reversed string in the reversed string variable, but in the next function call of recursion, 
            #that variabe is overwritten again. how do I make this persistent? Need to think
            print("Reversed string: ",string)
            #reversed_string = string
            return string
        else:
            string = list(string)
            temp = string[n-1]
            print("LENTGHG ",len(string)-1)
            string[n-1] = string[len(string)-n]
            string[len(string)-n] = temp
            n-=1
            print("String and n value passed in the recursion call: ",string, n)
            recursive_palindrome_check(string,n)
            return string #this will return the reversed array outside to the function calling the recursive function. 
    original_string = string
    reversed_string = recursive_palindrome_check(string,n)
    print("reversed_string variable contains: ",reversed_string)
    reversed_string = ''.join(reversed_string)
    if original_string == reversed_string:
        print("Yes. The string ",string," is a palindrome")
    else:
        print(string," is not a palindrome")
        
def fibonacci(n):
    #so basically, the next number will be the sum of the prevous number and the previous one before that. n = (n-1)+(n-2) basically
    fib = []
    fib.append(0)
    fib.append(1)
    print(fib)
    while(fib[len(fib)-1]<n):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    print("The fibonacci numbers till ",n," is: ",fib)
    #THIS IS SO EASY WITH A WHILE LOOP WTF

def fibo_rec(n):
    arr = []
    arr.append(0)
    arr.append(1)
    def fib(n,arr):
        if arr[len(arr)-1]>=n:
            return arr
        else:
            arr.append(arr[len(arr)-1] + arr[len(arr)-2])
            actual_arr = fib(n,arr)
            return actual_arr
    final_arr = fib(5,arr)
    print("arr finally contains: ",final_arr)
    return final_arr
    #okay damn! this worked in the first try. Very nice.

def fibo_multi_rec(n):
    # multiple-function calls would be used in implementing the Fibonacci series where any Nth Fibonacci number can be written as a 
    # sum of (N-1)th and (N-2)th Fibonacci numbers. So, the function result would look like this:
    # Fibonacci(N) = Fibonacci(N-1) + Fibonacci(N-2)
    # Results from both the function calls would be summed and returned to the main function call. This will only return the N th fibo number, not the whole array till n.
    if n<=1:
        return n
    else:
        last = fibo_multi_rec(n-1)
        second_last = fibo_multi_rec(n-2)
    return last + second_last



###### R E C U R S I V E  C O D E  D R I V E R ##########
#recursion_print(5)
#recursion_print_backtracking('Kiran',5)
#n_to_1(5)
#sum_of_numbers_parameterized(5,0)
#print(sum_of_n_numbers(5))
#print("TYPE 2 ACTUAL")
#sum_recursion_parameterized_2(3,0)
#print(factorial_2(5))
#factorial_custom(1,5)
#rec_rev_array(4, [1,2,3,4])
#rec_rev_array(5, [1,2,3,4,5])
#rec_palin_check('MALAYALAM',9)
#fibonacci(5)
#fibo_rec(5)
print("Nth fibo number is: ",fibo_multi_rec(4))



#----------- RECURSION REVISION ---------------

#traversing an array with recursion
def traverse_rec(arr,num):
    #GOING UP OPERATIONS
    if num < len(arr):
        arr[num]+=1
    else:    
        return
    print("going up, the array num  ",num, " is: ",arr[num])
    num+=1
    traverse_rec(arr,num)

    #COMING BACK DOWN OPERATIONS
    if num == 3:
        arr[num]+=20
        print("THE FATED ADDITION!")
    else:
        print("Num while coming down rn is : ",num, ". Hence nothing will happen")
    #it exits out of here when num finally +=1s and reaches 5
    return arr
    

arr = [1,2,3,4,5]
caught_arr = traverse_rec(arr,0)
print("The array we got back is: ",caught_arr)