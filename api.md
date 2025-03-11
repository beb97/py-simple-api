# Routes de l'API :

## POST /users : 
Crée un utilisateur dans la base de données.

    curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://127.0.0.1:5000/users

##  GET /users : 
Liste tous les utilisateurs de la table users.

    curl http://127.0.0.1:5000/users

## GET /users/<int:id> : 

Affiche les détails d’un utilisateur spécifique par ID.

    curl http://127.0.0.1:5000/users/1

## PUT /users/<int:id> : 

Met à jour les informations d’un utilisateur.

    curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Updated", "email": "john.updated@example.com"}' http://127.0.0.1:5000/users/1

## DELETE /users/<int:id> : 
Supprime un utilisateur.

    curl -X DELETE http://127.0.0.1:5000/users/1
