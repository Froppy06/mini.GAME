from http.client import IM_USED
from opponentBasicNPC import OpponentBasic
from playerNPC import Player
from sprzedawcaS import Sprzedawca
from czarodziejkaNPC import Czarodziejka
from eventsE import Events
from INN import Inn

print("=<>="*20)
player = Player()
sprzedawca = Sprzedawca()
czarodziejka = Czarodziejka()
events = Events()
inn = Inn()
game = True
while game:

    events.envents(player)

    if player.is_the_hero_alive() != True:
        print("=<>="*20)
        print("\t \t \t \t GAME OVER !!!")
        print("=<>="*20)
        break
    
    print("Pojedynek - p | Sprzedawca - z | Statystic - s | ")
    print("Czarodziejka - cz |  Eksploruje - e | Inn - i |")
    what_are_you_doing = input("Co robisz ")
    if what_are_you_doing.lower() == "p":         
        opponent = OpponentBasic(player)
        player.fight(opponent)
    elif what_are_you_doing.lower() == "s":
        player.statystic()
    # --------------------------------------------------------------
    elif what_are_you_doing.lower() == "z":
        sprzedawca.services()
        sprzedawca.zbroja(player)
        sprzedawca.bron(player)
    
    # -------------------------------------------------------------- 
    elif what_are_you_doing.lower() == "cz":
        czarodziejka.inf()
        czarodziejka.wizyta(player)
    # --------------------------------------------------------------
    elif what_are_you_doing.lower() == "i":
        inn.inf()
        inn.food(player)
        inn.sleep(player)
    # --------------------------------------------------------------
  
    else:
        print("Nie ma takiej komendy")

    player.level_up()