###### python3
#schöne tabelle erstellen, aus irgendeiner Liste von Listen

import pyperclip

tabelle = [["BMW", "BENZ", "AUDI", "VW"],
          ["Lamorghini", "Maserati", "Ferrari", "Ukuleli"],
          ["Toyota", "Suzuki", "Opel", "Nissan"]]


def printTable():
    for i in range(len(tabelle) +1 ):
        print("")
        for x in range(len(tabelle)):
                print("".join(tabelle[x][i]),end="\t")
    print("\n")

printTable()


#
# #! /usr/bin/env/python3
# import pyperclip
#
# tabelle = [["BMW", "BENZ", "AUDI", "VW"],
#           ["Lamorghini", "Maserati", "Ferrari", "Ukuleli"],
#           ["Toyota", "Suzuki", "Opel", "Nissan"]]
#
#
# def printTable(tabelle):
#     colwidths = [0] * len(tabelle)
#     print("Autos".center(colwidths,"-"))
#
#
# printTable()
