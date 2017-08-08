print "Let's get started"
spy_name = raw_input("what is your name ?")
if len(spy_name)>0:
    print "VALID NAME"
spy_salutation = raw_input("What should we call you? Mr. or Ms. : ")
# concatination of salutation and name.
spy_name = spy_salutation + "" + spy_name
print "welcome "+ spy_name + " Glad to have you back with us."
