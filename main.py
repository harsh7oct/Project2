#import statement
from spy_details import spy_name,spy_salutation,spy_rating,spy_age


print "Let's get started"
spy_name = raw_input("what is your name ?")
if len(spy_name) > 0:
    spy_salutation = raw_input("What should we call you? Mr. or Ms. : ")
    # concatination of salutation and name.
    spy_name = spy_salutation + "" + spy_name
    print "welcome " + spy_name + " Glad to have you back with us."
    print "ALRIGHT" + spy_name +" I WOULD LIKE TO KNOW MORE ABOUT YOU"
    spy_age = 0
    spy_age = int(raw_input("enter the age of the spy"))
    print type(spy_age)
    spy_rating = 0.0
    spy_rating = float(raw_input("enter the rating of the spy"))
    print type(spy_rating)
else :
    print "not valid"



