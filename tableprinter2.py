#! python3

print("test")


import pyperclip
import sys

table = [["BMW", "BENZ", "AUDI", "VW"],
          ["Lamorghini", "Maserati", "Ferrari", "Ukuleli"],
          ["Toyota", "Suzuki", "Opel", "Nissan"]]


def tablePrint(table):
    colwidths = [0] * len(table)
    #print(colwidths)
    for i in range(len(table)):
        colwidths[i] = len(max(table[i],key = len))

    for i in range(len(table)):
        for x in range(len(table)):
            print(table[x][i].ljust(colwidths[i]))

#was noch zu machen ist:
# - siehe lesezeichen in python
# - jeweils die Spalten bilden und dann deren Breite anpassen


    #print(colwidths)
    #print("Autos".center(23))

tablePrint(table)
