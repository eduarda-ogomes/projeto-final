class House():
    def __init__(self, name_house, chores, resident, admins):
        self.name_house =  name_house
        self.chores = []
        self.resident = []
        self.admins = []

    

    def add_admins(self, account):  ##feito
        self.admins.append(account)
        print("Admin adicionado com sucesso ")
        

    

