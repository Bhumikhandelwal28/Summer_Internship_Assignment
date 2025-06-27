import re
import pandas as pd

df=pd.DataFrame([
    "bhumie@example.com",  # valid
    "janve123@sub.domain.co",  # valid
    "user@.com",  # invalid
    "@gmail.com",  # invalid
    "neji.com",  # invalid
    "hello@world"  # invalid
],columns=['email'])
print(df)
#checking email format
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df['is_valid'] = df['email'].str.match(pattern)
print(df)

#checking mobile number format
number=input("Enter any number")
same=r'^[6-9]\d{9}$'
if re.match(same,number):
    print("The number is valid")
else:
    print("the number is invalid")

#strong password validation
password=input("Enter the password")
r_pass=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.match(r_pass,password):
    print("the password is available")
else:
    print("Create some strong password")
    print('''
The password should contain At least one lowercase letter → [a-z]
At least one uppercase letter → [A-Z]
At least one digit → [0-9]
At least one special character → @ $ ! % * ? & 
Minimum length of 8 characters")''')
# string check
stri=input("enter the string")
#Only Alphabets (with spaces)
res=r'^[A-Za-z ] +$'
# Alphanumeric String (no special characters)
ser=r'^[A-Za-z0-9]+$'
if re.match(res,stri):
    print("The string is valid")
else:
    print("The string is invalid")

#For checking date and time
date=input("Enter the date")
datte=r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$'
if re.match(datte,date):
    print("Valid")
else:
    print("Invalid")

#for Checking IP address Format
IP=input("Enter the IP address:")
ip_format=r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
if re.match(ip_format,IP):
    print("Valid")
else:
    print("Invalid")

#indian pincode format check
pin=input("Enter the pincode")
pin_format=r'^[1-9][0-9]{5}$'
if re.match(pin_format,pin):
    print("Valid")
else:
    print("Invalid")

#url basic format
url=input("Enter the URL")
url_format=r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*\/?$'
if re.match(url_format,url):
    print("Valid")
else:
    print("Invalid")



