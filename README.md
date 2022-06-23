# 忍び寄る ~ Shinobiyoru ~ 忍び寄る

Shinobiyoru is a windows keylogger which is written in python. Shinobiyoru can log user key strokes, log tab switches, screenshot the user activity and email logged data in .txt format aswell as captured screenshots in .png format.

This program also can delete files after they have created them and change file viewing preferences to allow for a more inconspicuous logging approach.

Logging verbosity is currently only an option in the raw code, there is no command line feature able to set certain key values at the moment. In the future I will create a command line program that can create custom keyloggers i will refine it to meet the needs of many different emails and smtp servers as well as set custom settings.

! currently only configured to send via ms outlook. ! 
if another mail service is to be used SMTP server and port must be updated.

Reccomended Usage.

- Meant to be converted to a .exe file and placed in windows start or renamed and hidden in system32, starting dependienciess need to be created for persistence... Powershell  exclusion path for the program should also be implimented.

- Alternatively .pyw extension to hide the program when running (python3 needs to be installed on the PC in this instance)

