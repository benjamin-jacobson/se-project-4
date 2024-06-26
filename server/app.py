import os

from flask import Flask, jsonify, make_response, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from server.models import db, User
# from models import db, User

from dotenv import load_dotenv
load_dotenv()

# app = Flask(__name__)
app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Migrations
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Users(Resource):

    def get(self):
        users = [u.to_dict() for u in User.query.all()]
        return make_response(jsonify(users),200)

api.add_resource(Users, '/users')

# read this for below explanation https://github.com/learn-co-curriculum/python-p4-deploying-flask-react-app-to-render
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")
