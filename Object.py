from model.DevObjs import Developper
from model.ComputerObjs import computer


computer1 = computer("hp mt44", '500 GB')        
computer2 = computer("Dell latitude e60" , "236GB")
Developper1 = Developper("Fabricejor" , 23,3000000, "Fabrice@gmail.com", computer1)

Developper1.modif_revenue(40000)


Developper2 = Developper("Jordan_Dev",22 ,20000, "Jordan@gmail.com",computer2)
Developper2.virements(Developper1)
