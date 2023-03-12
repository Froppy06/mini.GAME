from tkinter import *  
from playerNPC import Player   
import os

class Sprzedawca():
    def __init__(self) -> None:
        pass

    def services(self):
        print("---"*30)
        print("Witaj wedrowcze!!! Jak moge ci pomoc?")
        print("s - Sky Mantle - 85 gold")
        print("b - Brave Ax - 450 gold")
        print("s - Miecz のよる - 150 gold")
        print("o - Okaryna - 75 gold")
        print("m - Mandolina - 125 gold")
        print("w - Wooden arrows(10) - 25 gold")
        print("c - Copper arrows(10) - 75 gold")
        print("i - Silver arrows(10) - 125 gold")
        print("---"*30)

    def zbroja(self, player):

        inp = input("Co chcesz? ")
        if inp.lower() == "s":
            if player.goold >= 85:
                player.armor += 6
                player.goold -= 85 
                print(f"Zapłacono 85 zlota, obecnie masz {player.goold}")
                print(f"{player.name} zdobył  i ma teraz {player.armor} obrony")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")

    def bron(self, player):

        inp = input("Tak ? ")
        if inp.lower() == "b":
            if player.goold >= 450:
                player.attack += 16
                player.goold -= 450 
                print(f"Zapłacono 450 zlota, obecnie masz {player.goold}")
                print(f"{player.name} zdobył Brave Ax")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")  
        
        if inp.lower() == "s":
            if player.goold >= 150:
                player.attack += 9
                player.goold -= 150 
                print(f"Zapłacono 150 zlota, obecnie masz {player.goold}")
                print(f"{player.name} zdobył miecz のよる")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")   

        if inp.lower() == "o":
            if player.goold >= 75:
                player.attack += 5
                player.goold -= 75 
                print(f"Zapłacono 75 zlota, obecnie masz {player.goold}")
                print(f"{player.name} zdobył Okaryna")
            else:
                print("Nie masz wystarczajacej ilosci zlota ") 

        if inp.lower() == "m":
            if player.goold >= 125:
                player.attack += 10
                player.goold -= 125 
                print(f"Zapłacono 125 zlota, obecnie masz {player.goold}")
                print(f"{player.name} zdobył Mandolina")
            else:
                print("Nie masz wystarczajacej ilosci zlota ") 


        if inp.lower() == "w":
            if player.goold >= 25:
                player.arrow_wood = 10
                player.goold -= 25
                print(f"Zapłacono 25 zlota, obecnie masz {player.goold} gold")
                print(f"{player.name} zdobył Wooden arrows")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")
        if inp.lower() == "c":
            if player.goold >= 75:
                player.arrow_copper = 10
                player.goold -= 75 
                print(f"Zapłacono 75 zlota, obecnie masz {player.goold} gold")
                print(f"{player.name} zdobył Copper arrows")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")
        if inp.lower() == "s":
            if player.goold >= 125:
                player.arrow_steal = 10
                player.goold -= 125 
                print(f"Zapłacono 125 zlota, obecnie masz {player.goold} gold")
                print(f"{player.name} zdobył Silver arrows")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")
                
                