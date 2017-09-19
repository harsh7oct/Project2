# global variables and constants.
from termcolor import colored
from steganography.steganography import Steganography
#Red Color=> Error, Green Color=>Success Message
# current status message is initialized to None.
current_status_message = None

# list to store status messages.
STATUS_MESSAGES = ["Spy mode ON", "Busy, Call If Urgent"]

# lists to store users friends information.
friends = []

#Spy Class
class Spy:
    def __init__(self,salutation,name,age,rating,isonline):
        #Assigning Values
        self.Name=salutation+"."+name
        self.Age=age
        self.Rating=rating
        self.SpyOnline=isonline
        self.chat=[]
    def displayDetails(self):
        print self.Name," ",self.Age
    def calcAverageWords(self):
        #Average Words Spoken
        avg=0
        if len(self.chat)!=0:
            for i in self.chat:
                avg=avg+len(Steganography.decode(i.Message))
            avg=avg/(len(self.chat))
        print "Average Words Spoken: ",avg

#Chat class
class Chat:
    def __init__(self,msgImage,timestamp):
        #Assigning Values
        self.Message=msgImage
        self.Timestamp=timestamp
    def displayMessage(self):
        print colored(self.Timestamp,'blue'),"\nMessage: ",self.Message,"\n"