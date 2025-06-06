from app.models.resident_account import ResidentAccount
class Chore():
    def __init__(self,  activity, date, status, responsable: ResidentAccount ):
        self.activity= activity    
        self.date= date
        self.status= status
        self.responsable= responsable.username