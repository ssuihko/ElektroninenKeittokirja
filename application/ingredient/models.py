from application import db

class ingredient(db.Model):

    __tablename__ = "ingredient"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    recommendation = db.Column(db.String(144), nullable=True)
  
    def __init__(self, name, recommendation):
        self.name = name
        self.recommendation = recommendation
