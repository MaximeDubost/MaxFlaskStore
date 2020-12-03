import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

## Application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

## Base de donnée
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # Database
ma = Marshmallow(app) # ORM

## Classe Product 
class Product(db.Model):
    """ Classe "Produit" """
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

class ProductSchema(ma.Schema):
    """ Schéma "Produit """
    class Meta:
        """ Schéma """
        fields = ('id', 'name', 'description', 'price', 'quantity')


# Initialisation du schéma
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


##
## ROUTES 
##


## GET hello_world():
@app.route('/', methods=['GET'])
def hello_world():
    """ Affiche 'Hello World' """
    return jsonify({'msg': "Hello World"})

## POST add_product():
@app.route('/product', methods=['POST'])
def add_product():
    """ Créer un produit """

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product = Product(name, description, price, quantity)

    db.session.add(product)
    db.session.commit()

    return product_schema.jsonify(product)

## GET get_products():
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

##
## SERVER
##

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)