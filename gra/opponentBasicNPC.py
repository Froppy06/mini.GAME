from random import randint, choice
from basicMinionNPC import BasicMinion
from playerNPC import Player


class OpponentBasic(BasicMinion):
    def __init__(self,player) -> None:
        pass
        
        if player.level == 1:
            self.name = choice(["Jednorożec","Bazyliszek","Goblin","Werekrólik"])
            self.hp = randint(8,22)
            self.exp = randint(100,200)
            self.goold = randint(0,30)
            self.armor = 7
            self.attack = randint(2,20)
            self.name = self.name
        
        if player.level == 2:
            self.name = choice(["Jednorożec","Bazyliszek","Goblin","Werekrólik"])
            self.hp = randint(8,22)
            self.exp = randint(100,200)
            self.goold = randint(0,30)
            self.armor = 8
            self.attack = randint(2,20)
            self.name = self.name

        if player.level == 3:
            self.name = choice(["Jednorożec","Bazyliszek","Goblin","Werekrólik"])
            self.hp = randint(8,22)
            self.exp = randint(100,200)
            self.goold = randint(0,30)
            self.armor = 9
            self.attack = randint(2,20)
            self.name = self.name

        if player.level == 4:
            self.name = choice(["Duży Cyklop","Meduza","Chupacabra ","Werewolf"])
            self.hp = randint(22,36)
            self.exp = randint(100,200)
            self.goold = randint(0,50)
            self.armor = 10
            self.attack = randint(20,38)
            self.name = self.name

        if player.level == 5:
            self.name = choice(["Duży Cyklop","Meduza","Chupacabra ","Werewolf"])
            self.hp = randint(22,36)
            self.exp = randint(100,200)
            self.goold = randint(0,50)
            self.armor = 11
            self.attack = randint(20,38)
            self.name = self.name

        if player.level == 6:
            self.name = choice(["Duży Cyklop","Meduza","Chupacabra ","Werewolf"])
            self.hp = randint(22,36)
            self.exp = randint(100,200)
            self.goold = randint(0,50)
            self.armor = 12
            self.attack = randint(20,38)
            self.name = self.name

        if player.level == 7:
            self.name = choice(["Centaur","Charpie","Demon","Gryf"])
            self.hp = randint(36,50)
            self.exp = randint(100,200)
            self.goold = randint(0,70)
            self.armor = 13
            self.attack = randint(38,56)
            self.name = self.name

        if player.level == 8:
            self.name = choice(["Centaur","Charpie","Demon","Gryf"])
            self.hp = randint(36,50)
            self.exp = randint(100,200)
            self.goold = randint(0,70)
            self.armor = 14
            self.attack = randint(38,56)
            self.name = self.name

        if player.level == 9:
            self.name = choice(["Centaur","Charpie","Demon","Gryf"])
            self.hp = randint(36,50)
            self.exp = randint(100,200)
            self.goold = randint(0,70)
            self.armor = 15
            self.attack = randint(38,56)
            self.name = self.name      


    def basicBlock(self,player):
        self.attack = self.attack - player.armor
        return self.attack  
