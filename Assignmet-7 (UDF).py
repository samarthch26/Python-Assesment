"""
Q1. Write a function to print "Hello World".

def hello():
    print ("Hello")

hello()    

Q2.Create a function that takes a number and returns its square.

def square(num):
    return num * num

num = int(input("Enter a number: "))
print("Square =", square(num))

Q3.Write a function to check whether a number is even or odd.

def prime(num):
    if num%2==0:
        print ("Prime")
    else:
        print ("Not Prime")

num= int (input("Enter a Number:"))
prime (num)

Q4.Create a function that returns the sum of two numbers.

def add(a,b):
    return a+b
    
print (add(10,20))

Q5.Write a function to find the maximum of three numbers.

def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

print("Maximum number is:", max(n1, n2, n3))

Q6.Create a function that takes a string and returns it in uppercase.

def uppercase(a):
    return a.upper()

a=input("Enter Your String: ")
print ("Uppercase string: ",uppercase(a))

Q7.Write a function to calculate the factorial of a number.

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

num=int (input ("Enter Your Number: "))
print ("Factoria is :",factorial(num))

Q8.Create a function that checks if a number is positive, negative, or zero.  

def pos_neg_zero(num):
    if num>0:
        print ("Positive")
    elif num<0:
        print ("Negative")
    elif num==0:
        print ("Zero")

num=int (input("Enter Your Number: "))
pos_neg_zero(num)

Q9.Write a function to count the number of vowels in a string.

def vowel(a):
    count = 0
    for i in a:
        if i in 'aeiouAEIOU':
            count += 1
    return count

a = input("Enter a string: ")
print("Number of vowels:", vowel(a))

Q10.Create a function that returns the length of a list (without using len()). 

def length_list(li):
    count=0
    for items in li:
        count+=1
    return count

li=[10,20,30,40,50]

print ("Length of List: ",length_list(li))

Q11.Write a function to check whether a number is prime. 

def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num=int(input("Enter a Number:"))
if checkprime(num):
    print ("Prime")
else:
    print ("Not Prime")


Q12.Create a function that returns the reverse of a string. 

def reverse_string(s):
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev


s = input("Enter a string: ")
print("Reversed String:", reverse_string(s))


Q13.Write a function to find the sum of all elements in a list.

def total_sum(li):
    total=0
    for items in li:
        total += items
    return total

li=[10,20,30,40,50]

print ("Sum of all Elemnts:",total_sum(li))


Q14.Create a function that returns the second largest number in a list. 

def second_largest(li):
    li.sort()
    return li[-2]

li=[18,7,24,23,11]
print ("Second Largest Number: ",second_largest(li))


Q15.Write a function to remove duplicates from a list. 

def remove_duplicate(li):
    result=[]
    for item in li:
        if  item not in result:
            result.append(item)
    return result

li=[10,20,30,20,40,10,50,10]
print ("List After Removing Duplicates: ",remove_duplicate(li))


Q16.Create a function that checks if a string is a palindrome. 

def palindrome(s):
    rev=''
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]

    if rev==s:
        return True
    else:
        return False

s=input("Enter A String: ")
if palindrome(s):
    print ("Palindrome")
else:
    print ("Not Palindrome")


Q17.Write a function that takes a list and returns only even numbers.

def even_numbers(li):
    even=[]
    for i in li:
        if i%2==0:
            even.append(i)
    return even

li=[10, 15, 20, 25, 30, 35, 40]
print ("Even Numbers: ",even_numbers(li))
            

Q18.Create a function to count frequency of each element in a list. 

def frequency_count(li):
    freq={}
    for i in li:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

li = [10, 20, 10, 30, 20, 10, 40]

print ("Frequency of Elements: ",frequency_count(li))


Q19.Write a function that merges two lists into one.

def merge_limits(li1,li2):
    return li1+li2

li1=[1,2,3,4]
li2=[5,6,7,8]
print ("Merged List: ",merge_limits(li1,li2))


Q20.Create a function to calculate simple interest. 


def simple_interest(p,r,t):
    si=(p*r*t)/100
    return si

p=int(input("Enter Your Amount: "))
r=int(input("Enter Rate of Interest: "))
t=int(input("Enter Time Period: "))

print("Simple Interest: ",simple_interest(p,r,t))


Q21.Write a function using recursion to find factorial. 

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


Q22.Create a recursive function for Fibonacci series.  

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")


Q23.Write a function that accepts *args and returns their sum. 

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(5, 10, 15))


Q24.Write a function that accepts **kwargs and prints key-value pairs.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Samarth", age=20, course="Python")


Q25.Create a function decorator that prints 
"Function Started" and "Function Ended".

def my_decorator(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper

@my_decorator
def greet():
    print("Hello World")

greet()


Q26.Create a function to generate all substrings of a string. 

def substrings(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])


s = input("Enter a string: ")

substrings(s)


"""




