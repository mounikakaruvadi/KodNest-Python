# Check the number is positive or negative
number=int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Negative")

# Check person eligible to donate blood
age=int(input("Enter the age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Check the temperature is hot or cold
temperature=int(input("Enter the temperature: "))
if temperature > 30:
    print("Hot Day")
else:
    print("Cold")

# check student attendance at leat 75%
attendence=int(input("Enter the number of days: "))
if attendence >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Check whether the number is even or odd
number=int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")   

# Check the person eligible for driving license
age=int(input("Enter the age: "))
if age <= 18:
    print("Not eligible")
elif age >= 60:
    print("Not eligible")
else:
    print("Eligible")  

# Check the year is leap or not 
days=int(input("Enter the number of days: "))
if days==366:
    print("Leap")
else:
    print("Not Leap")

# Compare two numbers print greatest number
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
if num1 > num2:
    print(num1)
else:
    print(num2)

# Assign grades based on marks
marks=int(input("Enter the marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Fail")    

# Categorize electricity usage
units=int(input("Enter the number of units: "))
if units >= 500:
    print("High")
elif units >= 300:
    print("Medium")
elif units >= 100:
    print("Low")
else:
    print("Very Low")             

# Scholarship Eligibility
marks=int(input("Enter the marks"))
income=int(input("Enter the income: "))
if marks < 85:
    print("Not eligible")
elif income > 300000:
    print("Not eligible") 
else:
    print("Eligible")

# User login
username=str(input("Enter the username: "))
password=str(input("Enter the password: "))
if username!= "admin":
    print("Invalid username") 
elif password!= "mouni":       
    print("Invalid password")
else:
    print("Login successful")

# Display weekdays using numbers
day=int(input("Enter the number"))
if day== 1:
    print("Monday")
elif day== 2:
    print("Tuesday")
elif day== 3:
    print("Wednesday")
elif day== 4:
    print("Thursday")
elif day== 5:
    print("Friday")
elif day== 6:
    print("Saturday")
elif day== 7:
    print("Sunday")
else:
    print("Invalid day")     

# Display season based on month
month=str(input("Enter the month: "))
match month:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8 | 9:
        print("Rainy")
    case 10 | 11:
        print("Spring")
    case _:
        print("Invalid month")     

# print number from 1 to 20
for i in range(1,21):
    print(i)  

              
