import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import Sequential
from tensorflow.python.keras import layers
import numpy as np
import os as filesys
#import commandrun
#import interface
#from commandrun import history
#import time
working_path = filesys.getcwd()
result_stringg = ''
working_path = str(working_path)
print(working_path)
combined_path = working_path + '\\' + 'ai_model.h5'
print(combined_path)
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','-','_','+','=',' ','.',',',';',':',"'",'"','!','?','@','#','$','%','^','&','*','(',')','\\']

if filesys.path.exists(combined_path):
    model = keras.models.load_model(combined_path)
else:
    model = Sequential()
    model.add(layers.Dense(name="1", units='190', activation='relu'))
    model.add(layers.Dense(name="2", units='190', activation='relu'))
    model.add(layers.Dense(name="3", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="4", units='190', activation='relu'))
    model.add(layers.Dense(name="5", units='190', activation='relu'))
    model.add(layers.Dense(name="6", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="7", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="8", units='190', activation='relu'))
    model.add(layers.Dense(name="9", units='190', activation='relu'))
    model.add(layers.Dense(name="10", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="11", units='190', activation='relu'))
    model.add(layers.Dense(name="12", units='190', activation='relu'))
    model.add(layers.Dense(name="13", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="14", units='190', activation='relu'))
    model.add(layers.Dense(name="15", units='190', activation='relu'))
    model.add(layers.Dense(name="16", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="17", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="18", units='190', activation='relu'))
    model.add(layers.Dense(name="19", units='190', activation='relu'))
    model.add(layers.Dense(name="20", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="21", units='190', activation='relu'))
    model.add(layers.Dense(name="22", units='190', activation='relu'))
    model.add(layers.Dense(name="23", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="24", units='190', activation='relu'))
    model.add(layers.Dense(name="25", units='190', activation='relu'))
    model.add(layers.Dense(name="26", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="27", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="28", units='190', activation='relu'))
    model.add(layers.Dense(name="29", units='190', activation='relu'))
    model.add(layers.Dense(name="30", units='210', activation='sigmoid'))
    model.add(layers.Dense(name="31", units=len(characters), activation='softmax'))

    #Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

def run(input_string, character_string):
    encoded_input = [character_string.index(char) for char in input_string]
    encoded_input = np.array(encoded_input)

    prediction = model.predict(encoded_input)
    predicted_index = np.argmax(prediction[0])
    predicted_char = characters[predicted_index]
    return predicted_char

def train(input_string, character_string, epochnum):
    encoded_input = [character_string.index(char) for char in input_string]
    encoded_input = np.array(encoded_input)

    model.fit(encoded_input, encoded_input, epochs=epochnum, verbose=0)

def save():
    model.save(combined_path, True)

def delete():
    while True:
        print("Are you sure?")
        inp = input()
        if inp.upper() == 'Y':
            print("Deleted.")
            filesys.remove(combined_path)
            break
        elif inp.upper() == 'N':
            print("Cancelled.")
            break
        else:
            print("Invalid character, try Y/N.")

def quick_delete():
    #Warning: This is dangerous! Please only call this function in a security loop.
    if filesys.path.exists(combined_path):
        filesys.remove(combined_path)
    #Please. It is very dangerous.

def fancyrun(input, characters, iterations, result_string):
    counter = iterations
    while counter > 0:
        train(input, characters, iterations)
        counter -= 1
        result = run(input, characters)
        result_string = result_string + result
    return result_string