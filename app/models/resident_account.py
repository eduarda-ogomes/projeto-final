from app.models.user_account import UserAccount
class ResidentAccount(UserAccount):

    def __init__(self, username, password, permissions, birthday, id):

        super().__init__(username, password, id)
        self.permissions= permissions
        if not permissions:
            self.permissions= ['user']

    def isAdmin(self):
        return False