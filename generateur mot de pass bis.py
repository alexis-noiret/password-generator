import hashlib
import re
import json
import os

#Affiche le message à l'utilisateur.
#Stocke dans p la chaîne de caractères qu'il tape.
p = input("rentrez votre mot de passe: ")
#Variable de contrôle du while.
#Tant que x vaut True, la boucle continue.
x = True
#Démarre une boucle qui s’exécute jusqu'à ce qu’on passe x = False ou qu’on fasse un break.
while x:
    if(len(p) < 8):#Si la longueur du mot de passe est inférieure à 6 ou supérieure à 8, la boucle s’arrête = mot de passe invalide.
        break
    elif not re.search("[a-z]", p):#Vérifie s’il y a au moins une lettre minuscule.
#Si aucune : break → mot de passe invalide.
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[$#@]", p):
       break
    elif re.search("\\s", p):
        break
    else:
        print("mot de passe valide: ")#Si aucune des conditions précédentes n’a échoué :→ Le mot de passe est valide.
        x = False#x = False arrête la boucle.
    
        # hashé le mot de passe encode() pour convertir en bytes hexdigest() convertir en hexadecimal
        hashed_password = hashlib.sha256(p.encode()).hexdigest()
        print("Mot de passe haché (SHA-256) :", hashed_password)

        # Charger fichier JSON s'il existe
        if os.path.exists("password.json"):#Vérifie si le fichier password.json existe déjà.
            with open("password.json", "r") as f:#Ouvre le fichier en lecture.Charge son contenu dans la variable data.
                data = json.load(f)#Charge son contenu dans la variable data.

            # SI la clé "passwords" n'existe pas → on la crée
            if "passwords" not in data:
                data["passwords"] = []

        else:#Si le fichier n'existe pas :

            data = {"passwords": []}#On crée un dictionnaire avec une liste vide "passwords"

        # Vérifier si hash déjà présent
        if hashed_password in data["passwords"]:
            print("⚠ Ce mot de passe existe déjà dans le fichier !")
        else:
            # Ajouter le hash
            data["passwords"].append(hashed_password)

            # Sauvegarde
            with open("password.json", "w") as f:
                json.dump(data, f, indent=4)

            print("Mot de passe enregistré dans password.json")


if x:
    print("mot de passe non valide")
