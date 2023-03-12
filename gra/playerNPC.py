from random import randint
from basicMinionNPC import BasicMinion

class Player(BasicMinion):
    def __init__(self) -> None:
        super().__init__()
        self.mana = 0
        self.max_mana = 0
        self.armor = 0
        self.attack = 0
        self.arrow_wood = 0
        self.arrow_copper = 0
        self.arrow_steal = 0
        self.goold = 900
        self.exp = 0 
        self.level = 1
        self.equipment = []

# --------------------------------------------------------------------
        self.Fire_ball = True
        self.Lightning = False
        self.Ice_wall = False
        self.Heal = False
# --------------------------------------------------------------------
        self.name = input("Enter your name: ")
        inp = input("Select classes a - Warrior / b - Mag / c - Bard / d - Archer ")

        if "a" == inp.lower():
            self.hp = 100
            self.max_hp = 150
            self.mana = ""
            self.max_mana = ""
            self.armor = 7
            self.attack = 10
            self.name = self.name + " Warrior"
            
        elif "b" == inp.lower():
            self.hp = 20
            self.max_hp = 20
            self.mana = 130
            self.max_mana = 150
            self.armor = 2
            self.name = self.name + " Mag"

        if "c" == inp.lower():
            self.hp = 55
            self.max_hp = 70
            self.armor = 4
            self.attack = 10
            self.name = self.name + " Bard"
        
        if "d" == inp.lower():
            self.hp = 75
            self.max_hp = 90
            self.armor = 5
            self.arrow_wood = 15
            self.arrow_copper = 0
            self.arrow_steal = 0
            self.name = self.name + " Archer"

    def statystic(self):
        print("=<>="*20)
        print(f"\t \t \t NAME: {self.name}")
        print(f"hp = {self.hp} | Max hp = {self.max_hp} | mana = {self.mana} | max_mana = {self.max_mana} | level = {self.level}")
        print(f"goold = {self.goold} | attack = {self.attack} | armor = {self.armor} | wooden a. = {self.arrow_wood} | copper a. = {self.arrow_copper} | steal a. = {self.arrow_steal}")
        print(f"equipment = {self.equipment}")
        print("=<>="*20)


    def is_the_hero_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def level_up(self):
        if self.exp >= 1000:
            print("!!!"*50)
            print("\t"*3, " LEVEL UP !!!")
            print("!!!"*50)
            self.level += 1
            self.hp += 10
            self.max_hp += 10
            self.attack += 4
            self.mana += 20
            self.max_mana += 20
            self.exp = 0

# --------------------------------------------------------------------

# --------------------------------------------------------------------
    def księga_zaklęć(self,opponent):
        print("-*-"*40)
        print(f"a -{self.Fire_ball} - 50 mana")
        print(f"b -{self.Lightning} - 130 mana")
        print(f"c -{self.Ice_wall} - między 100-200 exp")
        print(f"d -{self.Heal} - 100 mana")
        print("-*-"*40)
        inp = input("? - ")
        if inp.lower() == "a":
            if self.Fire_ball and self.mana >= 50:
                print("Bammmmmm! Bammmmmm! Bammmmmm!")
                opponent.hp -= randint(5,15)
                self.mana -= 50

        elif inp.lower() == "b":
            if self.Lightning and self.mana >= 130:
                print("Bzzzzzz! Bzzzzzz! Bzzzzzz!")
                opponent.hp -= randint(10,30)
                self.mana -= 130

        elif inp.lower() == "c":
                print("Blinkkkk Blinkkkk Blinkkkk")
                self.exp -= randint(100,200)
                self.hp += randint(10,15)
                self.mana += randint(30,50)
                print("Odnowiłeś {self.hp} hp i {self.mana} many, ale straciłeś {self.exp}")

        elif inp.lower() == "d":
            if self.Heal and self.mana >= 100:
                self.hp += randint(35,50)
                self.mana -= 100
                print("Odnowiłeś {self.hp} hp")
        else:
                print("Nie znasz tego zklecia")

    def bow_and_arrow(self,opponent):
        print("z"*40)
        print(f"a - Wooden arrow - {self.arrow_wood} - 1 strzała")
        print(f"b - Copper arrow - {self.arrow_copper} - 1 strzała")
        print(f"c - Steal arrow - {self.arrow_steal} - 1 strzała")
        print("z"*40)
        inp = input("? - ")
        if inp.lower() == "a":
            if self.arrow_wood >= 1:
                opponent.hp -= randint(4,10)
                self.arrow_wood -= 1 

        if inp.lower() == "b":
            if self.arrow_copper >= 1:
                opponent.hp -= randint(10,14)
                self.arrow_copper -= 1   

        if inp.lower() == "c":
            if self.arrow_steal >= 1:
                opponent.hp -= randint(14,18)
                self.arrow_steal -= 1          
# --------------------------------------------------------------------
    # def Obrona(self, opponent):
    #     opponent.basicAtack = opponent.basicAtack - self.armor 
    #     return opponent.basicAtack

    def fight(self, opponent):
        fight = True
        while fight:

            if opponent.hp <= 0:
                print("Koniec Walki")
                print(f"Dostajesz {opponent.exp} exp / Znajdujesz {opponent.goold} goold")
                print("---"*30)
                self.exp += opponent.exp
                self.goold += opponent.goold
                break
            
            if self.hp <= 0:
                print("Umarłeś")
                break
            
            self.hp -= opponent.basicAtack()
            print(f"Otrzymałeś {opponent.basicAtack()} obr")
            print(f"Masz {self.hp} hp Przeciwnik {opponent.name} ma {opponent.hp}")
            print("---"*30)

            print("a - zwykły atak | z - księga zaklęć | b - atak Łucznika")
            print("---"*30)

            co = input("Co robisz ? ")
            if co.lower() == "a":
                opponent.hp -= self.basicAtack()
                print(f"Zadajesz {self.basicAtack()} obr")
            
# --------------------------------------------------------------------
# Możecie dorobić zaklęcia ;) 
# --------------------------------------------------------------------
            if  co.lower() == "z":
                self.księga_zaklęć(opponent)

            if  co.lower() == "a":
                self.fight(opponent)

            if  co.lower() == "b":
                self.bow_and_arrow(opponent)    