"""
                             LIST-QUESTIONS
                             
Q1.Write a Python program to create a list of integers and print its elements.

li=[23,34,45,56,67]
print (li)

Q2.Write a program to find the sum and average of all elements in a list.

li=[23,34,45,56,67]
print (sum (li))
print (sum (li)/5)

Q3.Write a program to find the largest and smallest element in a list.

li=[23,34,45,56,67,46,37]
print (max (li))
print (min (li))

Q4.Write a Python program to count the number of elements in a list without using len().

li=[23,34,45,56,67,46,37]   
print (len(li))

Q5.Write a program to reverse a list without using built-in functions. 

li=[23,34,45,56,67,46,37]
li.reverse()
print (li)

Q6.Write a program to check if an element exists in a list.

li=[23,34,45,56,67,36,25]
y=int(input("Enter a Element:"))
found=False
for x in li:
    if y==x:
        found=True
        break
if found:
    print ("Found",y)
else:
    print ("Not Found",y)

Q7.Write a Python program to remove duplicate elements from a list.

li=[23,34,45,56,67,34,23]
new_li=[]
for x in li:
    if x not in new_li:
        new_li.append(x)
print ("Original List",li)
print ("List after Removing Duplicates",new_li)

Q8.Write a program to sort a list in ascending and descending order.

li=[23,34,45,56,67,34,23]
li.sort()
print (li)
li.sort(reverse=True)
print (li)

Q9.Write a program to merge two lists and remove duplicates.

li=[23,34,45,56,67,34,23]
li2=[49,38,45,50,67,31]
li.extend(li2)
print (li)
found=0
new_li=[]
for x in li:
    if x not in new_li:
        new_li.append(x)
print ("List after Merge and removing Duplicates:",new_li)        

Q10.Write a program to find common elements between two lists.

li=[23,34,45,56,67,34,23]
li2=[49,38,45,50,67,31]

common=[]

for x in li:
    if x in li2:
        common.append(x)
print ("Common Number in both the Lists",common)

Q11. Write a program to split a list into even and odd numbers.

li=[23,24,45,56,67,34,80]
even=[]
odd=[]
for x in li:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print ("Even Number List",even)
print ("Odd Number List",odd)

Q12.Write a program to rotate a list by n positions.

li=[23,24,45,56,67,34,80]
n=int(input("No. of Right Rotation:"))
if n<len(li):
    r=li[n:]+li[:n]
    print(r)
else:
    print ("Wrong No. Entered")

Q13.Write a Python program to find the second largest number in a list.

li=[23,24,45,56,67,34,80]
li.sort(reverse=True)
print ("The Second Largest Number in a List is:",li[1:2])

Q14.Write a program to flatten a nested list.

li = [23, [24, 45], 56, [67, 34, 80]]
f_li = []
for x in li:
    if isinstance(x, list):
        for item in x:
            f_li.append(item)
    else:
        f_li.append(x)

print("Flatten list:", f_li)

Q15.Write a program to count frequency of each element in a list.

li=[21,10,90,87,99,98,34,12,34,90,90]
li.sort(reverse=True)
print(li)
for x in set(li):
    count = li.count(x)
    print(x, "->", count)

Q16.Write a program to replace all negative numbers with zero in a list.

li=[21,-10,90,87,99,98,34,-12,34,-90,90]
li2=[x for x in li if x>=0]
print ("Updated List:",li2)

Q17.Write a program to remove all occurrences of a given element from a list.

li=[23,24,45,56,67,34,80]
print(li)
n=int(input("Enter The Number U Want to Delete:"))
for x in li:
    if n in li:
        li.remove(n)
print (li)

Q18.Write a program to check if a list is a palindrome.

li=[1,2,3,4,3,2,1]
if li==li[::-1]:
    print ("Palindrome")
else:
    print ("Not Palindrome")

Q19.Write a Python program to find missing numbers in a given list of consecutive integers.

li=[1,2,4,5,7,9]

for x in range(len(li)-1):
    for i in range(li[x]+1,li[x+1]):
        li.append(i)
li.sort()
print ("Updated List:",li)
       
Q20.Write a program to perform element-wise addition of two lists.

li=[34,67,89,23,78,'abcd']
li1=[67,88,99,12,56,'54']
result=[]

for x in range(len(li)):
    result.append(li[x]+li1[x])
print ("Result:",result)    
    
Q21.Write a Python program to find the longest increasing subsequence in a list.

li = [10, 22, 9, 33, 21, 50, 57, 41, 60]
    
longest=[]
current=[li[0]]
for x in range(1,len(li)):
    if li[x]>li[x-1]:
        current.append(li[x])
    else:
        if len(current)>len(longest):
            longest=current
        current=[li[x]]
if len(current)>len(longest):
    longest=current
print ("The Longest Increasing Subsequence:",longest)            

Q22.Write a program to group elements based on frequency

li=[ 1, 2, 2, 3, 3, 3, 4, 4]
freq={}
for x in li:
    freq[x]=li.count(x)

group={}

for key in freq:
    value= freq[key]

    if value not in group:
        group[value]=[]
        
    group[value].append(key)
print (group)        

                          TUPLE-QUESTIONS

Q23.Write a Python program to create a tuple and print its elements.
                        
t=(23,34,45,56,67)
print (t)

Q24.Write a program to find the length of a tuple.

t=(23,34,45,56,67)
print (len(t))

Q25.Write a program to find the maximum and minimum element in a tuple.

t=(23,34,45,56,67)
print ("Maximum",max(t))
print ("Minimum",min(t))

Q26.Write a program to convert a tuple into a list.

t=(23,34,45,56,67)
li=list(t)
print (li)

Q27.Write a program to check if an element exists in a tuple.

t=(34,78,98,99,100,67,75,72)
n=int(input("Enter Your Number:"))
for x in range(len(t)):
    if t[x]==n:
        print ("Found")
        break
else:
    print ("Not Found")

Q28.Write a program to count occurrences of an element in a tuple.   

t=(34,78,98,99,100,98,67,98,75,72)
n=int(input("Enter Your Number:"))
count=0
for x in range(len(t)):
    if t[x]==n:
        print ("Found")
        count+=1
print (count)

Q29.Write a program to slice a tuple and display the result.

t=(34,78,98,99,100,67,75,72)
print(t)
print(t[2:7])


Q30.Write a program to find repeated elements in a tuple.

t=(34,78,98,99,100,98,67,98,75,72,78)
count=0
for x in range(len(t)):
    if(t.count(t[x]))>1:
        print(t[x])

Q31.Write a program to merge two tuples.

t=(34,78,98,99,100,98,67,98,75,72)
t2=(67,88,12,'abcd',87,10)

t3=t+t2
print(t3)

Q32.Write a program to unpack elements of a tuple into variables.

t=(34,78,98,99,100,98,67,98,75,72)
ch='a'
for x in t:
    print(ch,x)
    ch=chr(ord(ch)+1)

Q33.Write a Python program to sort a tuple.

t=(34,78,98,99,100,98,67,98,75,72)
li=list(t)
li.sort()
print(li)
t1=tuple(li)
print(t1)

Q34.Write a program to convert a list of tuples into a dictionary.

li = [('a', 34),('b', 56),('c', 67),('d', 89)]

d=dict(li)
print (d)

Q35.Write a program to find the index of an element in a tuple.

t=(34,78,98,99,100,98,67,98,75,72)
for x in range(len(t)):
    print (t.index(t[x]),"Index of",(t[x]))

Q36. Write a program to remove an element from a tuple (without directly modifying it).

t=(34,78,98,99,100,98,67,98,75,72)
li=list(t)
li.remove(78)

t1=tuple(li)
print ("The Original Tuple is:",t)
print ("The Modified Tuple is:",t1)

Q37.Write a program to find common elements between two tuples.

t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 60, 70)
common=[]

for x in t1:
    if x in t2:
        common.append(x)
print (tuple(common))

Q38.Write a Python program to check if a tuple is a palindrome.

t=(1, 2, 3, 4 , 3, 2, 1)

if t==t[::-1]:
    print ("Palindrome")
else:
    print ("not Palidrome)

Q39.Write a program to find the element with maximum frequency in a tuple.

t = (10, 20, 30, 20, 40, 20, 50, 30)

max_freq=0
freq_element=None

for x in t:
    freq=t.count(x)
    if freq>max_freq:
        
        max_freq=freq
        
        freq_element=x

print("Element:",freq_element )
print("Frequency:", max_freq)

Q40.Write a program to create a nested tuple and access its elements.

t=((34,78,98,99,100),(98,67,98,75,98,72))
for x in range(len(t)):
    for i in range(len(t[x])):
        print(t[x][i])

        
"""












