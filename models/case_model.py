from app import db
from datetime import datetime

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abuser_id = db.Column(db.Integer, db.ForeignKey('dog_abuser.id'), nullable=False)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=False)
    status = db.Column(db.String(120), nullable=True)