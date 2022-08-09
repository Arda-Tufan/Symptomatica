import os
import time
import sys
import re
import numpy as np
import itertools
import config
import configparser
import threading
from textblob import TextBlob
import re
from autocorrect import Speller


clear = lambda: os.system('cls')


# Basic Welcome and Introduction messages
print("Hello! Welcome to Symptomatica. This is an app that was created by @Mapperland to make diagnosing disases much easier.")
print("|------!!!!!!------| However this product doesn't guarentee %100 percent accuracy so don't use it for medical purposes. |------!!!!!!------|")



while(True):
 
 anwser = input("You need to enter you're symptoms to the terminal. Try to enter them as honest as possible.  Do you want to begin?   Y/N ")

 #Make the user input all lowercase so even when the user enters 
 
 
 if anwser.lower() == "y":
  print("Please enter your symptoms to the prompt. Please try to enter them correctly!")
  break
 elif anwser.lower() == "n":
  print("Ok then. Happy healthy days!")
  ask_again = False
  exit()
 else:
    print("Invalid anwser! Enter y or Y for the anwser -Yes- and n or N for the anwser -No-!")


ask_questions = True


symptom_list_of_usr = []
  


def Read_Disase(disasename):
        disase_point = 0
        config = configparser.RawConfigParser() #Reads config file and loads config
        config.read('Disase_symptoms.ini')
        details_dict = dict(config.items(disasename))
        for k,v in details_dict.items():
         if v in symptom_list_of_usr:
            disase_point += 1
            

        

        if int(disase_point) > int(len(details_dict))/2:
            print("You might have " + disasename + ".")

            
             
# iterating till the range
while True:
    symptom = input("Enter your'e symptom (Press F to finish entering) : ")
    spell = Speller()
    result = spell(symptom)
    if result != symptom:
     you_rlly_typ_it = input("Did you mean to type " + str(result) + "? ")
     if you_rlly_typ_it == "y":
         symptom = result
         pass   
     elif you_rlly_typ_it == "n":
        print(symptom_list_of_usr)
         
     else:
         print("y as yes and n for no please!")
         continue
    else:
        pass
    

     
    
 
        
       
     
   
#THREADS
   
 #Making the program work 2 functions with same parameters all at the same time

    if (symptom.lower() == "f"):
     Thread1 = threading.Thread(target=Read_Disase("FLU"))
     Thread2 = threading.Thread(target=Read_Disase("FOOD POISONING"))
     Thread3 = threading.Thread(target=Read_Disase("MALARIA"))
     Thread4 = threading.Thread(target=Read_Disase("DIARRHEA"))
     Thread5 = threading.Thread(target=Read_Disase("COVID 19"))
     Thread6 = threading.Thread(target=Read_Disase("MONKEYPOX"))
     Thread7 = threading.Thread(target=Read_Disase("TETANUS"))
     Thread8 = threading.Thread(target=Read_Disase("PNEUMONIA"))
     # Start the thread
     Thread1.start()
     Thread2.start()
     Thread3.start()
     Thread4.start()
     Thread5.start()
     Thread6.start()
     Thread7.start()
     Thread8.start()



     
     # Wait for the threads to finish
     Thread1.join()
     Thread2.join()
     Thread3.join()
     Thread4.join()
     Thread5.join()
     Thread6.join()
     Thread7.join()
     Thread8.join()
     
     
     
     
    else:
     symptom_list_of_usr.append(symptom.lower())
     print(symptom_list_of_usr)                            


