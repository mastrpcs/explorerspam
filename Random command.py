# this code will be available on my github! https://github.com/mastrpcs/explorerspam

# get the imports
import random
import os
import time

# needed variables
commands = ["explorer.exe"] # if you wanna be a absolute troll (opens up hella explorers)

# main program
os.system("color 2") #optional (sets console to green text)
while True:
    randomcmd = random.choice(commands)
    print("Random command : {randomcmd}")
    print(os.system(randomcmd))