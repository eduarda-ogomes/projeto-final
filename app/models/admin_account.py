from app.models.user_account import UserAccount
class SuperAccount(UserAccount):

    def __init__(self, username, password, permissions):

        super().__init__(username, password)
        self.permissions= permissions
        if not permissions:
            self.permissions= ['user']

    def isAdmin(self):
        return True