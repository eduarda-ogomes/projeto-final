from app.models.user_account import UserAccount
from app.models.user_message import UserMessage

from app.models.house import House
import json
import uuid


class MessageRecord():

    def __init__(self):
        self.__user_messages= []
        self.read()


    def read(self):
        try:
            with open("app/controllers/db/user_messages.json", "r") as fjson:
                user_msg = json.load(fjson)
                self.__user_messages = [UserMessage(**msg) for msg in user_msg]
        except FileNotFoundError:
            print('Não existem mensagens registradas!')


    def __write(self):
        try:
            with open("app/controllers/db/user_messages.json", "w") as fjson:
                user_msg = [vars(user_msg) for user_msg in \
                self.__user_messages]
                json.dump(user_msg, fjson)
                print(f'Arquivo gravado com sucesso (Mensagem)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Mensagem)!')


    def book(self,username,content):
        new_msg= UserMessage(username,content)
        self.__user_messages.append(new_msg)
        self.__write()
        return new_msg


    def getUsersMessages(self):
        return self.__user_messages


# ------------------------------------------------------------------------------

class UserRecord():

    def __init__(self, database):
        self.database = database
        self.__allusers= []
        self.__authenticated_users = {}
        self.read(database)
        

    def read(self,database):
        try:
            with open(f"app/controllers/db/{database}.json", "r") as fjson:
                self.__allusers = json.load(fjson)
        except FileNotFoundError:
            self.__allusers = []


    def __write(self,database):
        try:
            with open(f"app/controllers/db/{database}.json", "w") as fjson:
                json.dump(self.__allusers, fjson)
                print("Salvo com sucesso")
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Usuário)!')



    def setUser(self,username,password):
        for user in self.__allusers:
            if username == user.username:
                user.password= password
                print(f'O usuário {username} foi editado com sucesso.')
                self.__write() #### oque colocar aqui dentro, antes era account_type
                return username
        print('O método setUser foi chamado, porém sem sucesso.')
        return None


    def removeUser(self, user):
        if user in self.__allusers:
            print(f'O usuário {user.username} foi encontrado no cadastro.')
            self.__allusers.remove(user)
            print(f'O usuário {user.username} foi removido do cadastro.')
            self.__write() ### oque coloca dentro
            return user.username
        print(f'O usuário {user.username} não foi identificado!')
        return None


    def add_user(self, account):
        self.__allusers.append(vars[account])
        


  #  def getResidentAccounts(self):
  #      return self.__allusers['resident_accounts']


  #  def getCurrentUser(self,session_id):
   #     if session_id in self.__authenticated_users:
   #         return self.__authenticated_users[session_id]
   #     else:
   #         return None


    def getAuthenticatedUsers(self):
        return self.__authenticated_users


    def checkUser(self, username, password): #como vai funcionar o self authenticated_users
        for user in self.__allusers:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())  
                self.__authenticated_users[session_id] = user
                return session_id  
        return None


    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id] 
# ------------------------------------------------------------------------------



class HouseRecord:

    def __init__(self, database):
        self.database = database
        self.__allhouses= []
        self.read(database)


    def read(self,database):
        try:
            with open(f"app/controllers/db/{database}.json", "r") as fjson:
                self.__allhouses = json.load(fjson)
        except FileNotFoundError:
            self.__allhouses = []


    def __write(self,database):
        try:
            with open(f"app/controllers/db/{database}.json", "w") as fjson:
                json.dump(self.__allhouses, fjson)
                print("salvo com sucesso")
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (House)!')

    def add_house(self, house):
        self.__allhouses.append(vars[house])

        


