"""
                            STRING PROGRAMMING

Q1.Write a program to count the number of vowels in a string. 

count=0
s='PythonProgramming'
for x in s:
    if x in ('a','e','i','o','u'):
        print (x)
        count+=1
print ("Total Numbers of Vowels are:",count) 

Q2.Reverse a string without using built-in functions. 

s='PythonProgramming'
s1=()
for x in s:
    for i in range(len(s),0,-1):
        s1=s[i-1]
        print(s1,end=' ')
    break
    

Q3.Check whether a string is a palindrome.

s='malayalam'
s1=s
s2=''
for x in s:
    for i in range(len(s),0,-1):
        s2+=s[i-1]
    print (s2,end=' ')
 
    if (s2==s1):
        print ("Palindrome")
        break
    else:
        print ("Not Palindrome")
        break


Q4.Count uppercase and lowercase letters in a string.

s='PythonProgramming1'
count=0
count1=0
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
         count+=1
    elif s[i]>='a' and s[i]<='z':
         count1+=1

    else:
        print("Digit:",s[i])

print("Uppercase Letter:",count)
print("Lowercase letter:",count1)

Q5.Replace all spaces in a string with _.

s='Python Programming 1'
print(s.replace(' ','_'))

Q6.Find the frequency of each character in a string.

s='PythonProgramming'
s1=''

for x in s:
    if x not in s1:
        print (x,':',s.count(x))
        s1+=x
        
Q7.Remove duplicate characters from a string. 

s='PythonProgramming'
s1=''

for x in s:
    if x not in s1:
        s1+=x
print ("Original Sting:",s)
print ("After Removing Duplicate:",s1)

Q8.Find the first non-repeating character in a string.

st ="amankumar"
for i in st:
    if st.count(i)==1:
        print(i)
        break
else:
    print("No Non Repeating Character")

Q9.Check if two strings are anagrams.

s='listen'
s1='silent'
if sorted(s)==sorted(s1):
    print ("Anagrams")
else:
    print ("Not Anagrams")

Q10.Convert "hello world" → "Hello World" (title case without using .title()).

s='hello world'
words=s.split()
result=''
for w in words:
    result+=w.capitalize()+' '
print (result)    

Q11.Find the longest word in a sentence.

s="Python programming Language is good "
s1=s.split(" ")

longest=s1[0]

for x in s1:
    if len(x) > len(longest):
        longest=x
print ("Longest Word in a Sentence:",longest)    

Q12.Compress a string like "aaabbc" → "a3b2c1".

s='aaabbc'
result=' '

count=1

for x in range (len(s)-1):
    if s[x]==s[x+1]:
        count+=1
    else:
        result+=s[x]+str(count)
        count=1
        
result+=s[-1]+str(count)      
print (result)

Q13.Count words, characters, and digits in a string.

s="Programminglanguage112"

words=len(s.split())

chars=0
digits=0

for x in s:
    if x.isalpha():
         chars+=1
    elif x.isdigit():
        digits+=1

print ("Total Words:",words)
print ("Total Characters:",chars)
print ("Total Digits:",digits)

Q14.Rotate a string left by n positions.

s="AMAN KUMAR"
n=int(input("Enter Position to Rotate:"))

rotated=s[n:]+s[:n]
print (rotated)

Q15.Find all substrings of a given string.

s = "abc"

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])

                            SET PROGRAMMING

Q1.Create a set and add elements dynamically.

s ={1}

for x in range(1,10):
    num=int(input("Enter The Number:"))
    s.add(num)
    print (s)

Q2.Find the union and intersection of two sets.

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}

print("Union:",s1.union(s2))
print ("Intrsection:",s1.intersection(s2))

Q3.Remove duplicate elements from a list using a set.

li=[2,5,67,78,45,23,67,90]
s=set(li)
print(s)

Q4.Check if an element exists in a set.

n=67
s={2,5,67,78,45,23,67,90}

for x in s:
    if n in s:
        print ("Exist")
        break
    else:
        print ("Dont Exist")

Q5.Find the difference between two sets.

s1={2,5,67,78,45,23,67,90}
s2={45,23,90,21,12,46,78}

print("Differeence B/W Both Sets:",s1-s2)

Q6.Find common elements in two lists using sets.

li=[2,5,67,78,45,23,67,90]
li1=[45,23,90,21,12,46,78]

s1=set(li)
s2=set(li1)
print (s1.intersection(s2))

Q7.Check whether one set is a subset of another.

s1 = {1, 2, 3}
s2= {1, 2, 3, 4, 5}

flag = True

for x in s1:
    if x not in s2:
        flag = False
        break

if flag:
    print("s1 is a subset of s2")
else:
    print("s1 is not a subset of s2")

Q8.Find the first non-repeating character in a string.

s="amankumar"

for x in s:
    if s.count(x)==1:
        print (x)
        break
else:
    print ("No Non-Repeating Character")

Q9.Count unique elements in a list using a set.

li=[10,20,22,40,10,30,20]

s=set(li)

li1=list(s)
print (li1)

Q10.Remove all common elements from two sets.

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60, 70}

common=s1.intersection(s2)

s1=s1-common
s2=s2-common

print ("Set 1:"s1)
print ("Set 2:"s2)

Q11.Find missing numbers from 1 to n using sets. 

s={1,2,4,6,7,9}
n=10

all_numbers=set(range(1,n+1))

missing=all_numbers-s

print(missing)

Q12.Check if two lists have any common elements.

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60, 70}

common=s1.intersection(s2)
print(common)

Q13.Convert a set of strings into uppercase. 

s={"Programming"}

upper_set=set()

for x in s :
    upper_set.add(x.upper())

print(upper_set)

Q14.Identify unique vowels in a given string using a set. 

s = ("Programming is Awesome")

vowels=set()

for ch in s.lower():
    if ch in 'aeiou':
        vowels.add(ch)

print ("Unique Vowels:",vowels)

Q15.Find elements that appear only once in a list.

li=[10, 20, 30, 20, 40, 10, 50]

for x in li:
    if li.count(x)==1:
        print(x)


"""































