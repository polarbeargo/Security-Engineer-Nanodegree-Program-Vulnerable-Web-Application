import datetime, hashlib
from django.utils import safestring
from API.models import db
from sqlalchemy import Column, Integer, DateTime, String, BigInteger

class Customer(db.Model):
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    banner = Column(String)
    createdDate = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updateDate = Column(DateTime, onupdate=datetime.datetime.utcnow)
    deletedDate = Column(DateTime)

    def __init__(self, firstname, lastname, username, email, password, banner):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.banner = safestring.mark_safe(banner)

    def process(self):
        db.session.add(self)
        db.session.commit()
        return self

    def serialize(self):
        return {
            'id': self.id, 
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'createdDate': self.createdDate
        }