import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialisation de l'application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Base de donnée
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la base de données
db = SQLAlchemy(app)

# Initialisation de l'ORM
ma = Marshmallow(app)

# Classe "Produit"
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

""" TODO """
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': "Hello World"})

# Lancement du serveur
if __name__ == '__main__':
    app.run(debug=True)