#WARNING: experimental! use at your own risk.

#Imports (touch at your own risk)#

import ai #Ai functions
from ai import characters as charset #A variable from the ai script describing all avail chars
import re #Searching stuffs
import subprocess #Runs Command Prompt commands
import time #Delays
import string #For randomized passwords
import random #For randomized things
from configparser import ConfigParser
Con1 = ConfigParser()
Con1.read('Settings.ini')
chattraining = Con1.get("SETS", "chattraining")
supertransparent = Con1.get("SETS", "supertransparent")
loopdelay = float(Con1.get("SETS", "loopdelay"))
if chattraining == 'true':
    chattraining = True
elif chattraining == 'false':
    chattraining = False
else:
    print("Chat training's value is invalid")
if supertransparent == 'true':
    supertransparent = True
elif supertransparent == 'false':
    supertransparent = False
else:
    print("Super transparent's value is invalid")

print(chattraining)
print(supertransparent)
print(loopdelay)

#Configuration (Please look at this!)#

#chattraining = True #Is bot training off of chat?

#supertransparent = False #Is the code going to print whatever step it's on?
#It's also only recommended to do this when you're encountering an error, so you can troubleshoot.

#loopdelay = 0.2 #How long it will be until the main function is ran again (Default: 0.2)

#Variables#
global History
global Present
global Finished
global PSave
global PClear
global PQuit
global PASave
global PAClear
global PAQuit
global DNRFlag
History = ''
Present = ''
Finished = ''
Finished = str(Finished) #Don't touch!
Command = r'''findstr "ChatMessages=(Type=Message," "%localappdata%\\BrickRigs\\SavedRemastered\\Config\WindowsNoEditor\\Game.ini"'''
DNRFlag = False

#Password Randomizer#
def RString():
    if supertransparent == True:
        print("Something was randomized!")
    Ch = string.ascii_letters + string.digits + '!@#$%^&*'
    St = ''.join(random.choice(Ch) for _ in range(6))
    return St

PSave = RString()
PClear = RString()
PQuit = RString()
print("Here are your passwords, have fun!")
print(f"Save: {PSave}, Clear: {PClear}, Quit: {PQuit}")


#Main function#
#Warning: Spaghetti#

def Detect(DCommand, DFinished, PSave, PClear, PQuit):
    global DNRFlag
    if supertransparent == True:
        print("Detection ran!")
    Result = subprocess.run(DCommand, shell=True, capture_output=True, text=True)
    LLine = None
    if supertransparent == True:
        print("Detection is running the line-finder!")
    if Result.returncode == 0:
        lines = Result.stdout.splitlines()
        for line in reversed(lines):
            if "ChatMessages=(Type=Message," in line:
                LLine = line
                if supertransparent == True:
                    print("Line-finder has found the last line!")
                break
    Pat = r'''TextOption=INVTEXT\((.*?)\)'''
    Mat = re.search(Pat, LLine)
    if Mat:
        if supertransparent == True:
            print("Detection has successfully grabbed the text, and is processing!")
        DFinished = Mat.group(1) #Grab the text within
        DFinished = DFinished.replace("\\'", "'") #Replace any \' with just ', as MD does this to quotes
        DFinished = DFinished.replace('\\"', '"') #It does it to " too.
        DFinished = DFinished[1:] #Cut off anything before the text starts in the harvested chat
        LQuote = DFinished.rfind('"')
        if LQuote != -1:
            DFinished = DFinished[:LQuote] #Split the last quote off, and anything after it! We're done!
    else:
        print("Sorry, but there was an invalid character in the last chat, or it returned null.")
        DFinished = "Sorry, but there was an invalid character in the last chat, or it returned null."
    #VERY IMPORTANT#
    if DFinished != 'D.N.R':
    #VERY IMPORTANT#
        if supertransparent == True:
            print("Detection has passed the D.N.R, and Prompt is loading!")
        if DFinished.upper().startswith("!PROMPT"):
            if DNRFlag == False:
                PMat = re.search(r"!PROMPT (\d+) (\w+)", DFinished, re.IGNORECASE)
                if PMat:
                    print("Prompt command detected and successful!")
                    Iterations = int(PMat.group(1))
                    Prompt = str(PMat.group(2))
                    print(f"Prompt: {Prompt}, with an iteration number of {Iterations}!")
                    AIOutput = ai.fancyrun(Prompt, charset, Iterations)
                    print(AIOutput)
                    DFinished = 'D.N.R'
                    DNRFlag = True
                    return DFinished
            else:
                return DFinished
                            
        elif DFinished.upper().startswith("!SAVE"):
            if DNRFlag == False:
                if DFinished != 'D.N.R':
                    SMat = re.search(r"!SAVE (.*)", DFinished, re.IGNORECASE)
                    if SMat:
                        SPa = SMat.group(1)
                        if SPa == PSave:
                            print("Save password correct!")
                            DFinished = 'D.N.R'
                            ai.save()
                            PSave = RString()
                            print(f"Your new password for saving is {PSave}!")
                            DNRFlag = True
                            return DFinished
                        else:
                            print("Password incorrect.")
                            DNRFlag = True
                            DFinished = 'D.N.R'
                            return DFinished
                    else:
                        return DFinished
            else:
                return DFinished

        elif DFinished.upper().startswith("!CLEAR"):
            if DNRFlag == False:
                if DFinished != 'D.N.R':
                    CMat = re.search(r"!CLEAR (.*)", DFinished, re.IGNORECASE)
                    if CMat:
                        CPa = CMat.group(1)
                        if CPa == PClear:
                            print("Clear password correct!")
                            DFinished = 'D.N.R'
                            ai.quick_delete()
                            PClear = RString()
                            print(f"Your new password for clearing is {PClear}!")
                            DNRFlag = True
                            return DFinished
                        else:
                            print("Password incorrect.")
                            DFinished = 'D.N.R'
                            DNRFlag = True
                            return DFinished
                    else:
                        return DFinished
            else:
                return DFinished
                
        elif DFinished.upper().startswith("!QUIT"):
            if DNRFlag == False:
                if DFinished != 'D.N.R':
                    QMat = re.search(r"!CLEAR (.*)", DFinished, re.IGNORECASE)
                    if QMat:
                        QPa = QMat.group(1)
                        if QPa == PQuit:
                            print("Exiting..")
                            exit(0)
                        else:
                            print("Password incorrect.")
                            DFinished = 'D.N.R'
                            DNRFlag = True
                            
                            return DFinished
                    else:
                        return DFinished
            else:
                return DFinished
        else:
            DNRFlag = False
            
            return DFinished


#Input Loop#
while True:
    time.sleep(loopdelay)
    if History == '':
        History = Detect(Command, Finished, PSave, PClear, PQuit)
        Finished = History
        if supertransparent == True:
            print("History was empty!")
        print(History)
        if chattraining == True:
            if supertransparent == True:
                print("AI is training!")
            ai.train(History, charset, 50)
    else:
        if supertransparent == True:
            print("History wasn't empty!")
        Present = Detect(Command, Finished, PSave, PClear, PQuit)
        if Present != History:
            if supertransparent == True:
                print("Present didn't match history!")
            History = Present
            Finished = Present
            print(Present)
            if chattraining == True:
                if supertransparent == True:
                    print("AI is training!")
                ai.train(Present, charset, 50)
