import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)


# Initialisation de la base de données
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialisation des ORM
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    """  Classe définissant un produit
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        """ Constructeur de la classe Product

        Args:
            name (str): Nom du produit
            description (str): Description du produit
            price (float): Prix unitaire du produit
            quantity (int): Quantité de stock restant du produit
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductSchema(ma.Schema):
    """ Classe définissant la structure de la table Product
    """
    class Meta:
        """Classe définissant les colonnes de la table Product
        """
        fields = ('id', 'name', 'description', 'price', 'quantity')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/', methods=['GET'])
def home() -> Flask.response_class:
    """ Racine de l'API

    Returns:
        Response: Liste des routes disponibles
    """
    
    return jsonify({
        'routes': [
            "GET /product",
            "GET /product/<int:id>",
            "POST /product",
            "UPDATE /product/<int:id>",
            "DELETE /product/<int:id>"
        ]
    })


@app.route('/product', methods=['GET'])
def get_products() -> Flask.response_class:
    """ Obtenir la liste des produits

    Returns:
        Response: Liste des produits au format JSON
    """

    products = Product.query.all()

    return jsonify(products_schema.dump(products))


@app.route('/product/<int:_id>', methods=['GET'])
def get_product(_id: int) -> Flask.response_class:
    """ Obtenir un produit

    Args:
        _id (int): Identifiant du produit

    Returns:
        Response: Produit au format JSON
    """

    product = Product.query.get(_id)

    return product_schema.jsonify(product)


@app.route('/product', methods=['POST'])
def add_product() -> Flask.response_class:
    """ Ajouter un produit

    Returns:
        Response: Produit ajouté au format JSON
    """

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product = Product(name, description, price, quantity)

    db.session.add(product)
    db.session.commit()

    return product_schema.jsonify(product)


@app.route('/product/<int:_id>', methods=['PUT'])
def update_product(_id: int) -> Flask.response_class:
    """ Modifier un produit

    Args:
        _id (int): Identifiant du produit

    Returns:
        Response: Produit modifié au format JSON
    """

    product = Product.query.get(_id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()

    return product_schema.jsonify(product)


@app.route('/product/<int:_id>', methods=['DELETE'])
def delete_product(_id: int) -> Flask.response_class:
    """ Supprimer un produit

    Args:
        _id (int): Identifiant du produit

    Returns:
        Response: Produit supprimé au format JSON
    """

    product = Product.query.get(_id)

    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)
