class Developper:
    # le constructeur
    def __init__(self,pseudo,age,revenue,mail , computer):
        self.pseudo = pseudo
        self.age=age
        self.revenue=revenue
        self.mail = mail
        self.computer = None
        print ("Bienvenue ",pseudo , "\n Voici les spec des votre ordi:", computer.get_name(), computer.get_storage())
        
    def get_pseudo(self):
        return self.pseudo
    def get_age(self):
        return self.age
    def get_revenue(self):
        return self.revenue
    def get_mail(self):
        return self.mail
    
    def modif_revenue(self,taxes):
        self.revenue -= taxes
        print ("votre compte {} été débité de {}".format(self.pseudo,taxes) , "\nNouveau soldes {}FCFA".format(self.revenue)) 
    def virements(self, target_dev):
        target_dev.modif_revenue(self.revenue)
        print("Quelqun vous a piraté :",self.pseudo)   