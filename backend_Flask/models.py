from extensions import db
class User(db.Model):
    userID = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(44))
    passwd = db.Column(db.String(44))
    # userRole = db.Column(db.String(44))
    # userGroup = db.Column(db.String(44))
    userCity = db.Column(db.String(44))
     