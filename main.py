# import statements.
from spy_details import spy
from start_chat import start_chat
from globals import Spy
from termcolor import colored
import re

print "Let's get started!!!"
whole=True
#whole variable to iterate if value is not Y/N
while whole:
    question = "Do you want to continue as " + spy.Name + "(Y/N) ? "
    existing = raw_input(question)

    # validating users input
    if existing.upper() == "Y":
        # default user
        whole=False
        start_chat(spy.Name, spy.Age, spy.Rating, spy.SpyOnline)

    elif existing.upper() == "N":
        # new user code here
        whole=False
        wholecheck=True#temporary variable
        while(wholecheck):
            tempcheck=True#temporary variable
            # Validation Using Regex
            patternsalutation='^Mr|Ms$'
            patternname='^[A-Za-z][A-Za-z\s]+$'
            patternage='^[0-9]+$'
            patternrating='^[0-9]+\.[0-9]$'
            # Validating Each Values Using Regular Expression
            while tempcheck:
                salutation = raw_input("Mr. or Ms.? : ")
                if (re.match(patternsalutation, salutation) != None):
                    tempcheck = False
                else:
                    print colored("Enter Again!!!!",'red')
            tempcheck=True
            while tempcheck:
                spy.Name=raw_input("Enter Name: ")
                if(re.match(patternname,spy.Name)!=None):
                    tempcheck=False
                else:
                    print colored("Enter Again!!!!",'red')
            # concatenation.
            spy.Name = salutation + "."+spy.Name
            tempcheck=True
            while tempcheck:
                 spy.Age = raw_input("Age?")
                 if (re.match(patternage, spy.Age) != None):
                     tempcheck = False
                     spy.Age=int(spy.Age)
                 else:
                     print colored("Enter Again!!!!", 'red')
            tempcheck=True
            while tempcheck:
                spy.Rating = raw_input("Spy rating?")
                if (re.match(patternrating, spy.Rating) != None):
                    tempcheck = False
                    spy.Rating=float(spy.Rating)
                else:
                    print colored("Enter Again!!!!",'red')
            # Checking If Spy is eligible
            if spy.Rating <= 5.0 and spy.Age > 12 and spy.Age < 50:
                start_chat(spy.Name,spy.Age,spy.Rating,spy.SpyOnline)
                wholecheck=False
            else:
                print colored("Invalid Entry!!!!Start From Scratch.",'red')
    else:
        print colored("Wrong choice. Try again",'red')