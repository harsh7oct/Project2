#import statement
from spy_details import spy
from start_chat import start_chat



print "Let\'s get started"
question = "Do you continue as mr. "+spy['salutation']+" "+spy['name']+ ' (y/n) '
existing=raw_input(question)
#check validating user input
if (existing.upper()=='Y'):
    spy['name']=spy['salutation']+" "+spy['name']
    start_chat(spy['name'],spy['rating'],spy['is_online']);

elif (existing=='N' or existing=='n'):
    #new users code
    spy['name'] = raw_input("What is your name ?")
    if len(spy['name']) > 0:
        if spy['name'].isalpha():
            print "ALRIGHT" + spy['name'] + " I WOULD LIKE TO KNOW better before to proceed further.."
            spy['salutation'] = raw_input("What should we call you? Mr. or Ms. : ")
            # concatination of salutation and name.
            spy['name'] = spy['salutation'] + "" + spy['name']
            print "welcome " + spy['name'] + " Glad to have you back with us."
            spy['age'] = 0
            spy['rating'] = 0.0
            spy['online'] = False
            print type(spy['age'])
            spy['age'] = int(raw_input("enter the age of the spy"))
            if (type(spy['age']) == int ):
                print 'valid age'
            if spy['age'] > 15 and spy['age'] < 50:
                spy['rating'] = bool(raw_input("enter the rating"))
                print  type(spy['rating'])
            else:
                "not valid age"
        else:
            print "invalid name"
    else:
        print "not valid in"
else :
    print "wrong choice try again"



