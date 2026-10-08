num=input("Enter number")
reverse=""
for i in num:
    reverse=reverse+i
if num==reverse:
    print("Palindrome number")
else:
    print("Not palindrome")