from tkinter import *     
import os
from random import randint

class Inn():
    def __init__(self) -> None:
        pass

    # def odpowiedzi(self):  
    #     odpowiedz = randint("Co chciałbyś kupić?","Znalazłeś coś ciekawego?","Zainteresowało cię coś?")
    #     self.odpowiedz = odpowiedz

    #     if odpowiedz == 0:
    #         self.odpowiedz = odpowiedz

    #     elif odpowiedz == 1:
    #         self.odpowiedz = odpowiedz
    
    #     else:
    #         self.odpowiedz = odpowiedz


    def inf(self):
        print("---"*30)
        print("Witaj podróżniku. Jak mogę ci pomóc?")
        print("b - Cinnamon Bunny 30g")
        print("c - Crab Apple 15g")
        print("h - Hearts Donut - 20g")
        print("p - Wynajęcie pokoju - 200g")
        print("---"*30)

    def food(self, player):
        
        inp = input("Zainteresowało cię coś?")
        if inp.lower() == "h":
            if player.goold >= 20:
                player.hp += 32
                player.goold -= 20 
                print(f"Zapłacono 20 gold, obecnie masz {player.goold}")
                print(f"Masz {player.hp} hp")
                print(f"Dziękuje za twój zakup.")
            else:
                print("Nie masz wystarczajacej ilosci zlota ") 

        if inp.lower() == "c":
            if player.goold >= 15:
                player.hp += 18         
                player.goold -= 15 
                print(f"Zapłacono 15 gold, obecnie masz {player.goold}")
                print(f"Masz {player.hp} hp")
                print(f"Dziękuje za twój zakup.")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")
        
        if inp.lower() == "b":
            if player.goold >= 30:
                player.hp += randint(45, 50)
                player.goold -= 30 
                print(f"Zapłacono 30 gold, obecnie masz {player.goold}")
                print(f"Masz {player.hp} hp")
                print(f"Dziękuje za twój zakup.")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")

    def sleep(self, player):

        inp = input("Zainteresowało cię coś?")
        if inp.lower() == "p":
            if player.goold >= 200:
                player.hp == player.max_hp
                player.mana == player.max_mana
                player.goold -= 200 
                print(f"Zapłacono 50 gold, obecnie masz {player.goold}")
                print(f"Uleczono {player.max_hp-player.hp} hp i masz {player.max_mana-player.mana} many")
                print(f"Dziękuje za twój zakup.")
            else:
                print("Nie masz wystarczajacej ilosci zlota ")   

    