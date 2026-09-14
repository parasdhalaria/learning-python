# today we are going to make calculator using the python language

num1 = int(input("ENTER THE FIRST NUMBER"))
num2 = int(input("enter the second number"))

operator = input("enter the operator(+,-,/,*)")

if operator=="+":
   print(num1 + num2)

elif operator=="-":
    print(num1 - num2)

elif operator =="*":
   print(num1 * num2)

elif operator =="/":
   print (num1 / num2)

else:
    print("invailed operator")
    



