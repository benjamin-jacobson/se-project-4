import os

from Flask import Flask, jsonify, make_response
from flask_migrate import flask_migrate
from flask_restful import Api, Resource

from models import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_restful
app.json.compact = flask_restful

# Migrations
migrate = Migrate(app,db)
db.init_app(app)

api = Api(app)

class Users(Resource):
    def get(self):
    users = [u.to_dict() for u in Users.query.all()]
    return make_response(jsonify(users),200)

aoi.add_resource(Users, '/users')