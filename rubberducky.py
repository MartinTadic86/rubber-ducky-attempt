from keyboard import press_and_release, write
from time import sleep

command =["echo tvoje mama"]

press_and_release("left windows + R")
sleep(0.5)
write("cmd")
press_and_release("enter")
sleep(0.5)

for cmd in command:
    write(cmd)
    press_and_release (enter)