from datetime import datetime
from project.models import T_Message , T_Paramerter , T_Exhibit ,T_Cartlist , T_User
from project import db

def create_message(user_id,message):
    message_comp = T_Message(F_UserID=user_id,F_Message=message,F_TimeStamp=datetime.now())
    db.session.add(message_comp)
