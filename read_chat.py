from select_friend import select_friend
from globals import friends
from steganography.steganography import Steganography
from termcolor import colored
import re
def read_chat():
    #function logic
    friend_choice = select_friend()
    #Checking if Friend List is not empty
    if friend_choice!=-1:
        spyobject=friends[friend_choice]
        #Display Spy Details
        print colored(spyobject.Name,'red'), " ", colored(spyobject.Age,'red')
        #Average Words
        spyobject.calcAverageWords()
        #Checking If Chat History Is Not Empty
        if(len(spyobject.chat)>0):
            for chatobject in spyobject.chat:
                tempstr=chatobject.Message
                chatobject.Message=Steganography.decode(chatobject.Message)
                # Display Chat
                chatobject.displayMessage()
                chatobject.Message=tempstr
        else:
            print colored("No Chat History!!!!",'red')
    else:
        print colored("Empty Friend's List!!!!",'red')