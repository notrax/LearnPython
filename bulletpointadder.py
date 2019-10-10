#! python3
#bulletpoint adder - in einem wikipedia artikel
#stern am anfang jeder zeile mit text

import pyperclip

text = pyperclip.paste()

#todo: seperate lines and add stars

lines = text.split("\n")
for i in range(len(lines)): #loop durch alle indizes in lines
    lines[i] = "*" + lines[i] #add star to each string in lines list

text = "\n".join(lines)
pyperclip.copy(text)
