from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    greeting = db.Column(db.String)

    def __repr__(self):
        return f'<User: id {self.id} | name {self.name} | Greeting {self.greeting} >'

    
if __name__ == "__main__":
    u = User(name = "test_name", greeting = "test_greeting")
    print(u)