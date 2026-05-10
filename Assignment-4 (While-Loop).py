"""
Q1.Print numbers from 1 to 10 using a while loop.

a=1
while a<=10:
    print (a)
    a=a+1

Q2.Print even numbers from 1 to 20.

a=1
while a<=20:
    if a%2==0:
        print (a)
    a=a+1

Q3.Print odd numbers from 1 to 20.

a=1
while a<=20:
    if a%2==0:
        a=a+1
        continue
    print (a)
    a=a+1

Q4.Print numbers from 10 to 1 (reverse order)

a=10
while a>=1:
    print (a)
    a=a-1

Q5.Print multiplication table of 5 using while loop.

a=5
while a<=50:
    print (a)
    a=a+5

Q6.Find the sum of first 10 natural numbers using while loop.

a=1
total=0
while a<=10:
    print (a)
    total=total+a
    a=a+1
print ("Sum=",total)

Q7.Find factorial of a number entered by user.

num=int (input("Enter Your Number:"))
factorial=1
while num>0:
    factorial=factorial*num
    num=num-1
print ("factorial of number is :",factorial)    
    
Q8.Count number of digits in a given number.

num=int(input("Enter Your Number:"))
count=0
while num>0:
    rem=num%10
    num=num//10
    count=count+1
print ("The count of Digits in a given Number is:",count)    
5
Q9.Reverse a number using while loop.

num=int(input("Enter Your Number:"))
count=0
while num>0:
    rem=num%10
    count=count*10+rem
    num=num//10
print ("Reverse of a given Number is:",count)    
    
Q10.Check whether a number is palindrome or not using while loop.

num=int(input("Enter Your Number:"))
copy=num
count=0
while num>0:
    rem=num%10
    count=count*10+rem
    num=num//10
print ("Reverse of a given Number is:",count)
if copy==count:
    print ("Palindrome")
else:
    print ("Not Palindrome")

Q11. Print pattern: 
* 
** 
*** 
**** 
*****

i=1
while i<=5:
    print ('*'*i)
    i=i+1

Q12.Print pattern: 
1 
12 
123 
1234 
12345

n=int(input("Enter the range value"))
i=1
while i<n+1:
        j=1
        while j<i+1:
            print(j,end='')    
            j=j+1
        print()
        i=i+1

Q13.Ask user to enter password until correct password is entered.

password='Admin123'
while True:
    n=input("Enter Your Password:")
    
    if password==n:
        print("Correct Password")
        break
    else:
        print ("Try Again")

Q14. Create a number guessing game: 
• Generate a random number (1–10) 
• Keep asking user until they guess correctly

import random
num=random.randint(1,10+1)
i=1
while i<4:
    print (i,'Chance!')
    u=int(input("Guess a Number From 1 to 10:"))
    if num==u:
        print ("You Guess The Right No.")
        print ("That was The Random No.")
        break
    else:
        print ("You Guess Wrong, Try Again")
        i=i+1
if i==4:
    print ("Game Over")
    print ("The Random Number was:",num)

Q15.Keep taking input numbers until user enters 0, then print total sum.

add=0
while True:
    num=int(input("Enter Your Number:"))
    add=add+num
    if num==0:
        print ("Total is:",add)
        break
    print ("The Addition Of Your Numbers is:",add)
    
Q16.Print Fibonacci series up to N terms using while loop.

n=int(input("Enter Your Number:"))
a=0
b=1
i=1
while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1
    print (c)
    
Q17.Check whether a number is Armstrong number.

num=int(input("Enter Your Number:"))
copy=num
add=0
while num>0:
    rem=num%10
    num=num//10
    add=add+rem**3
print (add)
if copy==add:
    print ("It is an Armstrong Number")
else:
    print ("Not Armstrong")

Q18.Print prime numbers between 1 to 50 using while loop

num = 2

while num <= 50:
    i = 2
    is_prime = True

    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime:
        print(num, end=' ')

    num = num + 1

"""


