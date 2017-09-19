from termcolor import colored
STATUS_MESSAGES = ["Spy mode ON", "Busy, Call If Urgent"]
def add_status():
    tempcheck=True#temporary variable
    wholecheck=True#temporary variable
    while wholecheck:
        default = raw_input("Do you want to select from older status (y/n)? ")
        if default.upper() == "N":
            wholecheck=False
            #Setting new Status Message
            while tempcheck:
                new_status_message = raw_input("What status message do you want to set? ")
                if len(new_status_message)>0:
                    updated_status_message = new_status_message
                    STATUS_MESSAGES.append(updated_status_message)
                    tempcheck=False
                else:
                    print colored("Please enter a valid status ",'red')

        elif default.upper() == "Y":
            wholecheck=False
            while tempcheck:
                item_position = 1
                #selecting from list(Status)
                for message in STATUS_MESSAGES:
                    print str(item_position) +". "+ str(message)
                    item_position = item_position + 1
                message_selection = int(raw_input("Use Number To Select Desired Status\nEnter Choice:  "))
                if len(STATUS_MESSAGES) >= message_selection:
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    tempcheck=False
                else:
                    print colored("Select a proper status",'red')

        else:
            print colored("Wrong choice. Please try again",'red')
    return updated_status_message