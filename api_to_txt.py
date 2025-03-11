import requests
import json

# URL de l'API pour obtenir tous les utilisateurs
url = "http://127.0.0.1:5000/users"  # Remplace avec l'URL de ton API si nécessaire

# Effectuer la requête GET pour obtenir les utilisateurs
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    users = response.json()  # Récupère les données JSON de la réponse
    
    # Sauvegarder les données dans un fichier .txt au format JSON
    with open('data_extraction.txt', 'w') as file:
        json.dump(users, file, indent=4)  # Le paramètre indent=4 pour une meilleure lisibilité
    
    print("Les utilisateurs ont été enregistrés avec succès dans 'users_data.txt'.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
