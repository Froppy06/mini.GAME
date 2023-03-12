from tkinter import*
import os

class Czarodziejka():
    def __init__(self) -> None:
        pass

    def inf(self):
        print("a - 100g - Fire_ball - 100m - 10/30dps")
        print("b - 900g - Lightning - 100m - 100/300dps")
        print("c - 400g - Heal - 200m - +100hp")
        print("c - 350g - Ice_wall - 200m - +100hp")  

    def wizyta(self, player):

        inp = input("Tak ? ")
        if inp.lower() == "a":
            if player.Fire_ball == False and player.goold >= 100:
                player.goold -= 100
                player.Fire_ball = True
            
            else:
                print("Nie stać cie / już umiesz to zaklęcie")

        if inp.lower() == "b":
            if player.Lightning == False and player.goold >= 900:
                player.goold -= 900
                player.Lightning = True
                print(f"opanowujesz nowe zklecie - {player.Lightning}")
            
            else:
                print("Nie stać cie / już umiesz to zaklęcie")

        if inp.lower() == "c":
            if player.Heal == False and player.goold >= 400:
                player.goold -= 400
                player.Heal = True
                print(f"opanowujesz nowe zklecie - {player.Heal}")

            else:
                print("Nie stać cie / już umiesz to zaklęcie")  
                  
        if inp.lower() == "d":
            if player.Ice_wall == False and player.goold >= 350:
                player.goold -= 350
                player.Ice_wall = True
                print(f"opanowujesz nowe zklecie - {player.Ice_wall}")    
            else:
                print("Nie stać cie / już umiesz to zaklęcie")