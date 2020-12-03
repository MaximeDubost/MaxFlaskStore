# MaxFlaskStore

**`/!\ API EN COURS DE CRÉATION /!\`**

## Routes disponibles (03/12/2020) :

### Créer un produit :
```json
curl -d '{"name":"Produit x","description":"Description produit x","price":1,"quantity":1}' -H "Content-Type: application/json" -X POST https://max-flask-store.herokuapp.com/product
```

### Afficher tous les produits :
```
curl https://max-flask-store.herokuapp.com/product
```