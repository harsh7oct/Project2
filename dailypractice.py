print "CALCULATOR"
print "Enter 1 For Addition"
print "Enter 2 For Subtraction"
print "Enter 3 For Multiplication"
print "Enter 4 For Division"
choice = raw_input("Enter Your Choice")
number1 = input("Enter the first number")
number2 = input("Enter the second number")
if choice=="1":
    print (number1 + number2)
if choice=="2":
    print (number1 - number2)
if choice=="3":
    print (number1 * number2)
if choice=="4":
    print (number1 / number2)
