from select_friend import select_friend
from steganography.steganography import Steganography
from globals import friends,Chat
from termcolor import colored
from datetime import datetime
import re
def send_message():
    #function logic
    friend_choice = select_friend()
    #checking If Friend's List Is not Empty
    if friend_choice!=-1:
        pattern='^[A-Za-z][0-9A-Za-z\s]*\.jpg$'#Regex for correct name pattern for image
        patternsave='^SOS|SAVE ME|IN DANGER|HELP$'
        a=True#Temporary Variable
        #prepare the  message
        while a:
            original_image = raw_input("Provide the name of the image to hide the message: ")
            if(re.match(pattern,original_image)!=None):
                a=False
            else:
                print colored("Enter Again!!!!",'red')
        a=True
        while a:
            output_image = raw_input("Provide the name of the output image : ")
            if (re.match(pattern, output_image) != None):
                a = False
        text = raw_input("Enter your message here: ")
        if(len(text)>100):
            #remove friend he/she types more 100 words
            print colored("Large Message Input!!!!",'red')
            print colored("You are no more a Spy!!!!",'red')
            friends.remove(friends[friend_choice])
        else:
            #Handling Exception If Image Does Not Exist
            try:
                # Encrypt the message
                Steganography.encode(original_image,output_image,text)
                chatobject=Chat(output_image,datetime.now())
                friends[friend_choice].chat.append(chatobject)
                #Successful message
                print colored("Your message encrpyted successfully",'green')
                # Handling Situation For SOS|Danger
                if (re.match(patternsave, text.upper()) != None):
                    print colored("I got your location!!!!I'll be there soon!",'green')
            except IOError:
                print colored("Image %s Does Not Exist!!!!" %(original_image),'red')
    else:
        print colored("Empty Friend's List!!!!",'red')