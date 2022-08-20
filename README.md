# Symptomatica
This is a simple python bot to read all of your symptoms that you inputted and diagnose you a disase that relates to your'e symptoms. It runs many threads so your'e computer might think it is a trojan virus (Its not bro trust me) and it is not 100% accurate so DON'T USE IT FOR MEDICAL PURPOSES


if yu want to add an disase just do theese steps:

1- Go to .ini file and format your'e disase like this

[YOUR'E DISASE NAME]

youresymptom = YOOUR'E DISASE SYMPTOM
.
.
.
.




2- Then just head to the #Threads part of the code at the bottom and type theese lines:

Threadbla = threading.Thread(target=Read_Disase("YOUR'E DISASE NAME THAT YOU PUT IN .INI FILE GOES HERE")

Threadbla.start()

Threadbla.join()

Made by @Mors_Atra
