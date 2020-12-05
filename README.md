# MaxFlaskStore


## **Contenu**

**MaxFlaskStore** est une API type e-commerce développée en Python Flask.

L'API permet d'effectuer les action **CRUD** (Create, Read, Update, Delete) sur des produits d'un shop en ligne.

Celle-ci dispose donc de **5** routes :
- **`GET`** *`/product`* `:` Obtenir tous les produits
- **`GET`** *`/product/<id>`* `:` Obtenir un produit
- **`POST`** *`/product`* `:` Ajouter un produit
- **`UPDATE`** *`/product/<id>`* `:` Modifier un produit
- **`DELETE`** *`/product/<id>`* `:` Supprimer un produit

L'API interagit avec une base de données **SQLite** à l'aide des ORM **SQLAlchemy** et **Marshmallow**.

---

## **Lancement**

L'API est déployée dans un conteneur Docker sur un serveur Heroku à l'adresse suivante :
```
https://max-flask-store.herokuapp.com
```
Celle-ci est donc actuellement déjà déployée est prête à être utilisée.

---

## **Utilisation**

Voici 3 manières différentes d'utiliser l'API :

1. Avec la console grace à la commande `curl`
2. Avec un `navigateur web` ( méthodes GET uniquement )
3. Avec l'application `Postman` ( une collection Postman `MaxFlaskStore.postman_collection.json` contenant tous les endpoints est disponibles dans ce dépôt )

<br>

- ### **Obtenir tous les produits** ( **`GET`** *`/product`* ) 
Commande curl :
```
curl https://max-flask-store.herokuapp.com/product
```
URL : https://max-flask-store.herokuapp.com/product

<br>

- ### **Obtenir un produit** ( **`GET`** *`/product/<id>`* )
Commande curl :
```
curl https://max-flask-store.herokuapp.com/product/1
```
URL : https://max-flask-store.herokuapp.com/product/1

<br>

- ### **Ajouter un produit** ( **`POST`** *`/product`* )
Commande curl :
```json
curl -d '{"name":"Produit 4","description":"Description produit 4","price":4,"quantity":10}' -H "Content-Type: application/json" -X POST https://max-flask-store.herokuapp.com/product
```

<br>

- ### **Modifier un produit** ( **`UPDATE`** *`/product/<id>`* )
Commande curl :
```json
curl -d '{"name":"Produit 2 (updated)","description":"Description produit 2 (updated)","price":2,"quantity":10}' -H "Content-Type: application/json" -X PUT https://max-flask-store.herokuapp.com/product/2
```

<br>

- ### **Supprimer un produit** ( **`DELETE`** *`/product/<id>`* )
Commande curl :
```
curl -X DELETE https://max-flask-store.herokuapp.com/product/3
```
