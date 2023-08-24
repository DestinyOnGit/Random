import subprocess
import re
import time
import ai
import os
import sys
import string
import random
from ai import characters as charset

training_protocals = True

print("Initialized Imports")
def generate_random_string():
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    random_string = ''.join(random.choice(characters) for _ in range(6))
    return random_string
print("Initialized Password Generators")
global c_history
global c_current
c_history = ''
c_current = ''
result_stringg = ''
global enable_loop
enable_loop = True
global password_quita
global password_savea
global password_cleara
global pattern_quit
global pattern_save
global pattern_clear
password_quita = generate_random_string()
password_savea = generate_random_string()
password_cleara = generate_random_string()
pattern_quit = '!quit (.*)'
pattern_save = '!save (.*)'
pattern_clear = '!clear (.*)'

command = '''findstr "ChatMessages=(Type=Message," "C:\\Users\\windows server 2003\\AppData\\Local\\BrickRigs\\SavedRemastered\\Config\\WindowsNoEditor\\Game.ini"'''
print("Initialized Starting Variables")

print("Your passwords are:")
print("Quit:", password_quita)
print("Save:", password_savea)
print("Clear:", password_cleara)
print("Have fun!")

#the jewel
global finished
finished = ' '

def findchat(command_run, history, current):
    #print("Findchat has been ran")
    password_clear = password_cleara
    password_save = password_savea
    password_quit = password_quita
    result = subprocess.run(command_run, shell=True, capture_output=True, text=True)
    last_line = None
    #print("Findchat is running the last-line finder")
    if result.returncode == 0:
        lines = result.stdout.splitlines()
        for line in reversed(lines):
            if 'ChatMessages=(Type=Message,' in line:
                last_line = line
                break
    
    #last_line = last_line.replace('TextOption=INVTEXT("', "TextOption=INVTEXT(AA")
    #last_line = last_line.replace('''")''', "AA)")
    #last_line = last_line.replace('"', "'")
    #print("Findchat stopped running the last-line finder")
    if finished != 'D.N.R':
        pattern = "TextOption=INVTEXT\(([^()]+)\)"
        match = re.search(pattern, last_line)
        if match:
            finished = match.group(1)
            finished = finished.replace("\\'", "'")
            finished = finished.replace('\\"', '"')
            finished = finished[1:]
            lastquote = finished.rfind('"')
            if lastquote != -1:
                finished = finished[:lastquote]
        else:
            print("D'oh fiddlesticks. What now?!..")
            finished = "D'oh fiddlesticks. What now?!.."
            #print("Findchat managed to figure out what 'finished' was")
        #print("It is now checking if finished starts with !PROMPT")
        if finished.upper().startswith('!PROMPT'):
            match2 = re.search('''!PROMPT (\d+) (.*)''', finished, re.IGNORECASE)
            if match2:
                if match2 != None:
                    if finished != 'D.N.R':
                        #print("It did, and:")
                        print("Prompt requested.")
                        outputchars = match2.group(1)
                        prompttext =  match2.group(2)
                        outputchars = int(outputchars)
                        print("How many chars on output:", outputchars)
                        print("Prompted text:", prompttext)
                        ai_output = ai.fancyrun(prompttext, charset, outputchars, result_stringg)
                        print(ai_output)
                        finished = 'D.N.R'
                        return finished
                    else:
                        print("It returned Null, shit.")
                else:
                    print("That's an error and a half.")
        elif finished.upper().startswith('!SAVE'):
            savefind = re.search(pattern_save, finished, re.IGNORECASE)
            if savefind:
                if finished != 'D.N.R':
                    savepass = savefind.group(1)
                    if savepass == password_savea:
                        print("Save password was entered correctly.")
                        ai.save()
                        password_savea = generate_random_string()
                        print("Your new save password is:", password_savea)
                        finished = 'D.N.R'
                        return finished
                    else:
                        print("Better luck next time.")
                        finished = 'D.N.R'
                        return finished
            else:
                print("Damn it.. Fix that, enjinr.")
        elif finished.upper().startswith('!CLEAR'):
            clearfind = re.search(pattern_clear, finished, re.IGNORECASE)
            if clearfind:
                if finished != 'D.N.R':
                    clearpass = clearfind.group(1)
                    if clearpass == password_cleara:
                        print("Clear password was entered correctly.")
                        ai.quick_delete()
                        password_cleara = generate_random_string()
                        print("Your new clear password is:", password_cleara)
                        finished = 'D.N.R'
                        return finished
                    else:
                        print("Better luck next time.")
                        finished = 'D.N.R'
                        return finished
            else:
                print("Damn it.. Fix that, enjinr.")
        elif finished.upper().startswith('!QUIT'):
            quitfind = re.search(pattern_quit, finished, re.IGNORECASE)
            if quitfind:
                if finished != 'D.N.R':
                    quitpass = quitfind.group(1)
                    if quitpass == password_quit:
                        print("Quit password was entered correctly.")
                        exit(0)
                    else:
                        print("Better luck next time.")
                        finished = 'D.N.R'
                        return finished
            else:
                print("Damn it.. Fix that, enjinr.")
        else:
            return finished
    





            

while enable_loop:
    time.sleep(0.1)
    if enable_loop == True:
        if c_history == '':
            c_history = findchat(command, c_history, c_current)
            print(c_history)
            if training_protocals == True:
                ai.train(c_history, charset, 10)
                #print("train_debug")
        else:
            c_current = findchat(command, c_history, c_current)
            if c_current != c_history:  
                c_history = c_current
                print(c_current)
                if training_protocals == True:
                    ai.train(c_current, charset, 10)
                    #print("train_debug")
            