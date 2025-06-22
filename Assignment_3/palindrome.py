num=int(input("Enter the number you want to check"))
original=num
reverse=0
while num!=0:
      a=num%10
      reverse=reverse*10+a
      num//=10

print("The reverse number is:",reverse)
#to check whether a number is palindrome or not
if original==reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")