from select_friend import select_friend
from globals import friends
from termcolor import colored
from steganography.steganography import Steganography
import re
def read_message():
    #function logic
    friend_choice = select_friend()
    #Checking if Friend List is not empty
    if friend_choice!=(-1):
        pattern='^[A-Za-z][0-9A-Za-z\s]*\.jpg$'
        a=True #temporary variable
        #Average Words
        friends[friend_choice].calcAverageWords()
        #prepare the  message
        while a:
                output_image = raw_input("Provide the name of the image to be decrypted: ")
                if(re.match(pattern,output_image)!=None):
                    a=False
                else:
                    print colored("Enter Again!!!!",'red')
        try:
            #Decrypt the message
            text = Steganography.decode(output_image)
            print "Message:",text
        except TypeError:
            #Blank Image Case i.e. No Decrypted Message in Image
            print colored("Image does not have any message!!!!",'red')
        except IOError:
            print colored("Image Does Not Exists!!!!", 'red')
    else:
        print colored("Empty Friend's List!!!!",'red')