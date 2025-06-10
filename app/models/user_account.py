import uuid
class UserAccount():

    def __init__(self, username, fullname, email, password, birthday, genero, id = None):
        self.username= username
        self.password= password
        self.fullname= fullname
        self.birthday= birthday
        self.genero= genero
        self.email= email
        if id == None:
            self.id = uuid()
    def isAdmin(self):
        return False



