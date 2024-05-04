from app import app
from models import db, User

with app.app_context():
    print('Deleting existing users...')
    User.query.delete()

    print('Creating user objects...')
    u1 = User(name = "Bob", greeting = "Hey!")
    u2 = User(name = "Mike", greeting = "Hola!")
    u3 = User(name = "Sue", greeting = "Bonjour!")
    u4 = User(name = "Jane", greeting = "Hello!")

    print('Adding user objects to transaction')
    db.session.add_all([u1, u2, u3, u4])

    print('Committing transaction...')
    db.session.commit()

    print('Comlplete.')