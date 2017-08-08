print "calculator"
a=int(input("enter the first number"))
a=str (a)
if len(a)>0 :
    b=input("enter the second number")
    b=str(b)
    if len(b)>0 :
        print "Enter 1 For Addition"
        print "Enter 2 For Subtraction"
        print "Enter 3 For Multiplication"
        print "Enter 4 For Division"
        c=int(raw_input("enter the option"))
        if c == 1:
            a=int (a)
            b=int(b)
            d = a+b
            print d
        if c == "2":
            print (a - b)
        if c == "3":
            print (a * b)
        if c == "4":
            print (a / b)
            #this will happen when you will take input you will face concatenation problem and have to typecast again and again
            # this is due to first we are converting int into str den after we r converting into int again?
            #to run len()
            # ok thanks for making me clear
            #no problem
            #you are from which batch
            # 4th year#ok yester dy we have share github link for problem have a look over it and try to solve them ok sure#and create a new file namewith assignment and create py file with date name and daily practiice over there and push it to github we will have a record over you ok from now i will do the same
            #ok anyother issue i will tell u later as i will practice more#OK thanks again and tata