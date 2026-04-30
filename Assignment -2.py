"""
Q1.Write a Python program to check if a number is positive.

num = float(input("Enter a Number:"))
if num>0:
     print("The Number is Positive")

Q2.Print "Eligible to vote" if age is 18 or above. 

age=float(input("Enter your Age:"))
if age>=18:
    print ("Eligible to Vote")

Q3.Check if a number is divisible by 7.


num= float(input("Enter a Number:"))
if num%7==0:
    print ("It is Divisible")

Q4. Print "Pass" if marks are greater than 40.

marks=float(input("Enter Your Marks:"))
if marks>40:
    print ("Pass")

Q5.Check if a number is greater than 100.

num=float(input("Enter Your Number:"))
if num>100:
    print ("It is Greater Number")

Q6.Display a message if temperature exceeds 45°C.

temp= float(input("Enter the Temperature:"))
if temp>45:
    print ("Temperature High")

Q7.Check if a string length is more than 8 characters.

a=input("enter:")
if len(a)>8:
    print ("length is more than limit")

Q8. Print "Logged In" if password matches "admin123".

text=input("Enter:")
if text=='admin123':
    print ("Logged In")

Q9.Check if a number is a multiple of 10.

num=float(input("Enter Your Number:"))
if num%10==0:
    print ("It is a Multiple of 10")
    
Q10.Print a warning if balance is below minimum limit.

num=float(input("Enter the Balance:"))
limit=5000
if num<limit:
    print ("WARNING Balance Low")

Q11. Check whether a number is even or odd.

num=int(input("Enter Your Number:"))
if num%2==0:
    print ("Number is even")
else:
    print ("Number is odd")

Q12. Find the largest of two numbers.

a=float (input("Enter Your Number:"))
b=float (input("Enter Your Number:"))
if a>b:
    print ("The largest Number is:",a)
else:
    print ("The largest Number is:",b)

Q13.Check whether a person is eligible for driving license.

num=int(input("Enter Your Age:"))
if num>=18:
    print ("Eligible for Driving License")
else:
    print ("Not Eligible for Driving License")

Q14.Print "Pass" or "Fail" based on marks. 

marks=float(input("Enter you Marks:"))
if marks>=33:
    print ("PASS")
else:
    print ("FAIL")

Q15.Check whether a number is positive or negative. 
    
a=float(input("Enter Your Number:"))
if a>=0:
    print ("POSITIVE")
else:
    print ("NEGATIVE")

Q16.Check whether a character is a vowel or consonant.

ch= input("Enter a Alphabet=")
if ch in "aeiouAEIOU":
    print ("It is a Vowel")
else:
    print ("It is a Costant")
    
Q17.Check if a year is leap or not.




Q18.Print "Valid Password" or "Invalid Password".

a=input("Enter Your Password :")
if a=="admin123":
    print ("Valid Password")
else:
    print ("Invalid Password")
    
Q19.Determine whether salary is taxable or not.

salary=input("Enter Your Monthly Salary:")
if salary>="60000":
    print ("Taxable")
else:
    print ("Not Taxable")

Q20.Check whether a number is greater than 50 or not.

a=int(input("Enter Your Number:"))
if a>50:
    print ("It is Greater")
else:
    print ("It is not Greater")

Q21.Find the largest of three numbers.

a=int(input("Enter the Number:"))
b=int(input("Enter the Number:"))
c=int(input("Enter the Number:"))
if a>=b and a>=c:
    print ("The Largest Number is",a)
else:
    if b>=a and b>=c:
         print ("The Largest Number is",b)
    else:
         print ("The Largest Number is",c)

Q22.Check whether a number is positive, negative, or zero. 

a=float(input("Enter Your number :"))
if a>0:
    print ("Positive")
else:
    if a<0:
        print ("Negative")
    else:
        print ("Zero")

Q23.. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60

marks= float(input("Enter Your Marks:"))
if marks>=90:
    print ("A Grade")
else:
    if marks>=75:
        print ("B Grade")
    else:
        if marks>=60:
            print ("C Grade")
        else:
            print ("FAIL")

Q24.Check whether a triangle is equilateral, isosceles, or scalene.

a=float(input("Enter The Value of Side A:"))
b=float(input("Enter The Value of Side B:"))
c=float(input("Enter The Value of Side c:"))    
if a==b==c:
        print ("Equilateral")
else:
    if a==b or b==c or a==c:
        print ("Isosceles")
    else:
        print ("Scalene")

Q25. Check whether a character is uppercase, lowercase, digit, or special character.

ch =input ("Enter a Character :")
ch1= ord(ch)
if ch1>=65 and ch1<=90:
    print ("Uppercase",ch)
else:
    if ch1>=97 and ch1<=122:
        print ("Lowercase",ch)
    else:
        if ch.isdigit():
            print ("Digit")
        else:
            print ("Special Character")\

Q26.Calculate electricity bill using slab-wise rates            

service=250
unit=int(input("Enter unit consumption:"))
if unit<=100:
    bill=unit*5
else:
    if unit<=200:
        bill=unit*7
    else:
        bill=unit*10
bill=bill+service
print("Bill:",bill)

Q27.. Validate login using username and password. 

username=input("Enter Your Username:")
password=input("Enter Your Password:")
user="Admin"
passcode="Admin123"
if user!=user:
        print ("The username Is Not Found")
else:
    if password!=passcode:
        print ("Password is Incorrect")
    else:
        print ("Logged Inn")

Q28.Check student result using marks of 3 subjects.

marks1=float(input("Enter you 1st Subject Marks:"))
marks2=float(input("Enter you 2nd Subject Marks:"))
marks3=float(input("Enter you 3rd Subject Marks:"))
total=(marks1+marks2+marks3)
print ("TotalMarks:",total)
if total>=40:
    print ("Passsed")
else:
    print ("Failed")

Q29.Find the second largest number among three numbers.

a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
if (a>b and a>c):
    if (b>c):
        print ("The Second Largest Number is",b)
    else:
        print ("The Second Largest Number is",c)
else:
   if (b>a and b>c):
     if (a>c):
         print ("The Second Largest number is",a)
     else:
         print ("The Second Largest Number is",c)
        
Q30.Check loan eligibility using age, salary, and credit score. 

age=int(input("Enter Your AGE:"))
income=float(input("Enter Your INCOME:"))
creditscore=int(input("Enter Your CREDIT SCORE:"))
if (age>=18 and age<=70):
    if (creditscore>=650 and income>=40000):
        print ("Eligible for Loan")
    else:
        if creditscore<650:
            print ("Not eligible, Credit Score Does Not Fullfill The Requirements")
        else:
            if income<40000:
                print ("Not eligible, Income Does Not Fullfill The Requirements")
else:
    print ("Not Eligible, Age Does Not Fullfill The Requirements")

Q31.Print day name using day number (1–7).

days=int(input("Enter Days Number:"))
if days==1:
    print("Monday")
elif days==2:
    print("Tuesday")
elif days==3:
    print ("Wednesday")
elif days==4:
    print ("Thursday")
elif days==5:
    print ("Friday")
elif days==6:
    print ("Saturday")
elif days==7:
    print ("Sunday")
else:
    print ("Something Went Wrong")

Q32.Print month name using month number.     

months=int(input("Enter Months Number:"))
if months==1:
    print ("January")
elif months==2:
    print ("February")
elif months==3:
    print ("March")
elif months==4:
    print ("April")
elif months==5:
    print ("May")
elif months==6:
    print("June")
elif months==7:
    print ("July")
elif months==8:
    print ("August")
elif months==9:
    print ("September")
elif months==10:
    print ("October")
elif months==11:
    print ("November")
elif months==12:
    print ("December")
else:
    print ("Something Went Wrong")

Q33.Display grade based on percentage.

a=int(input("Enter Your Percentage:"))
if a>=90 and a<=100:
    print ("A Grade")
elif a>=80 and a<=89:
    print ("B Grade")
elif a>=60 and a<=79:
    print ("C Grade")
elif a>=40 and a<=59:
    print ("D Grade")
else:
    print ("Failed")

Q34.Display bonus percentage based on experience years.

years=float(input("Enter Your Years of Experience:"))
if years<1:
    print ("Not Eligible For Bonus")
elif (years>=1 and years<2):
    print ("5% Bonus")
elif (years>=2 and years<3):
    print ("10% Bonus")
elif (years>=3 and years<5):
    print ("13% Bonus")
elif (years>=5 and years<10):
    print ("!7% Bonus")
elif years>=10:
    print ("25% Bonus")
    
Q35.Identify traffic signal meaning. 

trafficsignal=input("Enter Traffic Signal Meaning:")
if trafficsignal=="Red" or trafficsignal=="RED" or trafficsignal=="red":
    print ("STOP")
elif trafficsignal=="Yellow" or trafficsignal=="YELLOW" or trafficsignal=="yellow":
    print ("SLOW DOWN AND STOP")
elif trafficsignal=="Green" or trafficsignal=="GREEN" or trafficsignal=="green":
    print ("GO")
else:
    print ("Invalid Signal")

Q36.Categorize temperature as Cold / Warm / Hot.

temp=float(input("Enter the Temperature:"))
if temp<=13:
    print ("COLD")
elif temp>13 and temp<=32:
    print ("WARM")
elif temp>32:
    print ("HOT")

Q37.Categorize employee based on salary range.

salary=int(input("Enter Your Salary:"))
if salary<=30000:
    print ("Associative Engineer")
elif salary>30000 and salary<50000:
    print ("Software Engineer")
elif salary>50000 and salary<80000:
    print ("Senior Software Engineer")
else:
    print ("Manager")

Q38.Print discount percentage based on purchase amount.

amount=float(input("Enter Purchase Amount:"))
if amount<=2000:
    print ("No Discount Applied")
elif amount>2000 and amount<=5000:
    print ("8% Discount Applied")
elif amount>5000 and amount<=15000:
    print ("15% Discount Applied")
elif amount>15000:
    print ("20% Discount Applied")
    
Q39.Identify number type: single-digit / double-digit / multi-digit. 

num=int(input("Enter Your Number:"))
if num>=0 and num<=9:
    print ("Single-Digit")
elif num>=10 and num<=99:
    print ("Double-Digit")
elif num>=100 and num<=999:
    print ("Triple-Digit")
else:
    print ("Multi-Digit")

Q40.Assign performance rating: Poor / Average / Good / Excellent.

performance=input("Enter Your Performance Value:")
if performance=='Outstanding':
    print ("Excellent , Rating= 9-10")
elif performance=='Very Satisfactory':
    print ("Good , Rating= 6-8")
elif performance=='Satisfactory':
    print ("Average , Rating= 4-5")
elif performance=='Unsatisfactory':
    print ("Poor , Rating= Below 4")

Q41.Check whether a number is divisible by 5 and 11.

num=int(input("Enter Your Number:"))
a=5
b=11
if num % a ==0 and num % b ==0:
    print ("yes, It is Divisible")
else:
    print ("Not Divisible")

Q42.. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700

Age=int(input("Enter Your Age:"))
Salary=int(input("Enter Your Salary:"))
Creditscore=int(input("Enter Your Credit score:"))
if Age>=21 and Salary>=25000 and Creditscore>=700:
print ("Eligible For Loan")
else:
    print ("Not Eligible")

Q43.Validate login using username AND password.

name=input("Enter Your Username:")
passcode=input("Enter Your Password:")
username='Samarthchaudhary'
password='Samarth123'
if name==username and passcode==password:
    print ("Logged Inn")
elif name==username:
        print ("Usename is Incorrect")
elif passcode==password:
    print ("Password is Incorrect")
elif name!=username and passcode!=password:
    print ("Both Username And Password Are Wrong")

Q44.Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50   

marks1=float(input("Enter 1st Subject Marks:"))
marks2=float(input("Enter 2nd Subject Marks:"))
marks3=float(input("Enter 3rd Subject Marks:"))
average=(marks1+marks2+marks3)/3
if average>=50 and marks1>=40 and marks2>=40 and marks3>=40:
    print ("PASS")
elif average<50:
    print ("NOT PASS IN AVERAGE")
elif marks1<40:
    print ("Not PASS IN 1st SUBJECT")
elif marks2<40:
    print ("NOT PASS IN 2nd SUBJECT")
elif marks3<40:
    print ("NOT PASS IN 3rd SUBJECT")

Q45.Check if a number lies between 10 and 100.

num=int(input("Enter Your Number:"))
if num>10 and num<100:
    print (num,"Lies B/W 10 To 100")
elif num<=10:
    print (num,"is Less Then 10")
elif num>=100:
    print (num,"is More Then 100")

Q46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

a=float(input("Enter Your Attendance%="))
attendance=75
if a>=75:
    print ("Eligible For Exam")
else:
    b=input("Medical Certificate Available (Yes/No):")
    if b=='Yes':
       print ("ELIGIBLE FOR EXAM")
    else:
        print ("NOT ELIGIBLE FOR EXAM")

Q47.Validate a date using conditions.

date=int(input("Enter Date:"))
month=int(input("Enter Month No.:"))
year=int(input("Enter Year:"))
if date>0 and date<32 and month>0 and month<13:
    print ("valid Date")
else:
    print ("Invalid Date")

Q48.Check whether an email format is valid.

email=input("Enter Your Email=")
if '@' in email and '.' in email:
    print ("Valid Email")
else:
    print ("Invalid Email")

Q49.Determine insurance eligibility using age, health status, and income.

age=int(input("Enter Your Age:"))
healthstatus=input("Enter Your Health Status Ok/Not Ok:")
income=int(input("Enter Your Income:"))
if age>=18 and age<=70:
    if healthstatus=='Ok' and income>=20000:
        print ("Eligible For Insurance")
    elif healthstatus=='Not Ok' and inome>=20000:
        print ("Not Eligible, Health Status Does Not Match The Criteria")
    elif healthstatus=='Ok' and income<20000:
        print ("Not Eligible, Income Does Not Match The Criteria")
else:
    print ("Not Eligible, Age Does Not Match The Criteria")

Q50.Check leap year using complete leap year logic.

year=int(input("Enter Year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print (year,"It is a Leap Year")
else:
    print (year,"It is not a Leap Year")

Q51.Write a Python program to calculate income tax using slabs.

income=float(input("Enter Your Income:"))
tax=0
if income<=250000:
    tax=0
elif income<=500000:
    tax=(income - 250000)*0.10
elif income<=1000000:
    tax=(250000*0.10)+(income-500000)*0.20
else:
    tax=(250000*0.10)+(500000*0.20)+(income-1000000)*0.30
    
print ("The Tax Value on Income",income,"is",tax)

Q52. Create an ATM withdrawal program with balance checks.

balance=40000
print("--ATM MENU--")
print("1.Check Balance")
print("2.Withdrawl Amount")
print("3.Deposit Balance")

choice=int(input("Enter Your Choice:"))
if choice==1:
    print ("Your Balance Is",balance)
elif choice==2:
    amount=float(input("Enter Amount To be Withdrawl:"))
    if amount<=0:
        print ("Invalid Amount Entered")
    elif amount>balance:
        print ("Invalid Amount Entered")
    else:
        balance=balance-amount
        print ("Amount Withdrawled")
        print ("Current Balance is",balance)
elif choice==3:
    amount=float(input("Enter Amount To be Deposit:"))
    if amount<=0:
        print ("Invalid Amount Entered")
    else:
        balance=balance+amount
        print ("Amount Deposited")
        print ("Current Balance",balance)
else:
    print ("Invalid Choice")

Q53.Check promotion eligibility using experience and performance.

exp=float(input("Enter Your Experience:"))
if exp<3:
    print ("Not Eligible for Promotion")
elif exp>=3:
    perf=input("Enter Your Performance Rating:")
    if perf=='Satisfactory':
      print ("Not Eligible for Promotion")
    elif perf=='Good':
      print ("Not Eligible for Promotion")
    elif perf=='Great':
      print ("Eligible For Promotion")
    elif perf=='Outstanding':
      print ("Eligible For Promotion")
else:
    print ("Not Eligible For Promotion")

Q54.Implement a grading system using nested if–else.

marks=float(input("Enter Your Marks:"))
if marks>=90 and marks<101:
    print ("Grade A,",marks)
elif marks>=80 and marks>90:
    print ("Grade B,",marks)
elif marks>=65 and marks>80:
    print ("Grade C,",marks)
elif marks>=40 and marks>65:
    print ("Grade D,",marks)
elif marks<40:
    print ("Fail,",marks)

Q55.Validate strong password using multiple conditions.

password=input("Enter Your Password:")
specialchar="@#$%&"
if len(password)<8:
     print ("Weak Password ❌ (Minimum 8 characters required)")
elif password.islower() or password.isupper():
     print ("Weak Password ❌ (Must Contain Mix of Upper and Lower Case)")
elif password.isalpha():
     print ("Weak Password ❌ (Must Contain at least One Digit and Special Character)")
elif password.isalnum():
    print ("Weak Password ❌ (Must Contain at least One Special Character)")
else:
    print ("Strong Password ✔")

Q56.Calculate delivery charges based on location and order amount.

amount=int(input("Enter Your Product Amount: "))
location=input("Enter Your Location(Local/Outstation):")

delcharges=0
               
if amount>=2000:
    delcharges=0
    print("No Delivery Charges")
elif location=='Local':
    delcharges=50
    print ("The Delivery Charges Will be:",delcharges)
elif location =='Outstation':
    delcharges=100
    print ("The Delivery Charges Will be:",delcharges)
else:
    print ("Invalid Location Entered")
    delcharges=0
    
total=amount+delcharges
print ("The Total Amount To be Paid is:",total)

Q57.Determine online exam qualification.

name=input("Enter Your Name:")
marks=int(input("Enter Your Marks:"))
if marks>=60 and marks<=100:
    print ("Qualified")
elif marks>=40 and marks<60:
    print ("Not Qualified")
elif marks<40:
    print ("Fail")
else:
    print ("Wrong Marks Entered")

Q58.Create movie ticket pricing logic based on age & show time

age=int(input("Enter Your Age:"))
showtime=input("Enter Show Time (Morning/Evening):")
ticketprice=200
if age<=12:
    ticketprice=ticketprice*0.5
elif age>=60:
    ticketprice=ticketprice*0.7
if showtime=='Morning':
    ticketprice=ticketprice-50
elif showtime=='Evening':
    ticketprice=ticketprice
else:
    print ("Invalid Showtime Entered")
print ("Total Ticket Price Is:",ticketprice)

Q59.Determine bank account type based on balance.

balance=float(input("Enter Balance in Your Account:"))
if balance<0:
    print ("Invalid Balance")
elif balance<=10000:
    print ("Basic Balance")
elif balance<=50000:
    print ("Saving Account")
elif balance<=200000:
    print ("Premium Account")
else:
    print ("VIP Account")

Q60. Create a menu-driven program using if–elif–else.

print("--MENU--")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=int(input("Enter Your Choice(1 to 4):"))

if choice>=1 and choice<=4:
    a=float(input("Enter Your 1st Number:"))
    b=float(input("Enter Your 2nd Number:"))
    
    if choice==1:
       print ("Result:",a+b)

    elif choice==2:
       print ("Result:",a-b)

    elif choice==3:
       print ("Result:",a*b)

    elif choice==4:
         if b==0:
            print ("Cannot Divide by ZERO")
         else:
            print ("Result:",a/b)
else:
    print ("Invalid Choice")

"""







 






