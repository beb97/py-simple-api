from flask import Blueprint, request, jsonify
import mysql.connector

users_blueprint = Blueprint('users', __name__)

# Configuration de la connexion MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  # Remplace par ton nom d'utilisateur MySQL
    password="root",  # Remplace par ton mot de passe MySQL
    database="simple_py_api"
)

# Fonction pour obtenir le curseur MySQL
def get_db_cursor():
    return db.cursor(dictionary=True)

# CREATE - Ajouter un utilisateur
@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    cursor = get_db_cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    
    return jsonify({"message": "Utilisateur créé"}), 201

# READ - Lister tous les utilisateurs
@users_blueprint.route('/users', methods=['GET'])
def get_users():
    cursor = get_db_cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    return jsonify(users)

# READ - Détails d'un utilisateur par ID
@users_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    cursor = get_db_cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    
    if user is None:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
    return jsonify(user)

# UPDATE - Mettre à jour un utilisateur
@users_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    cursor = get_db_cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, id))
    db.commit()
    
    if cursor.rowcount == 0:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
    return jsonify({"message": "Utilisateur mis à jour"})

# DELETE - Supprimer un utilisateur
@users_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = get_db_cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    db.commit()
    
    if cursor.rowcount == 0:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
    return jsonify({"message": "Utilisateur supprimé"})