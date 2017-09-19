from globals import friends
from termcolor import colored
def select_friend():
    counter = 1
    #Display All friends
    for friend in friends:
        print str(counter) + ". ",
        friend.displayDetails(),
        print "" #To Remove Extra output none
        counter = counter + 1
    if(counter>1):
        #temporary variable
        temp=True
        #If entered value is greater than no. of elements
        while temp:
            result = int(raw_input("Select from the list : "))
            if(result<counter):
                temp=False
            else:
                print colored("Enter Correct Value",'red')
    else:
        return -1
    return result - 1