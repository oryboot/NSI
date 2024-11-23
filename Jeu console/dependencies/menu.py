from .bird import Bird


def menu():
    print("Bienvenue dans Oiseaux en Colère !\nDans ce jeu votre objectif sera d'éliminer la menace Picoo.\n\n   1-Débuter le jeu  2-Règles")
    if input() == '2':
        print(
            "Voici les règles du jeu :\nVous incarnez un oiseau au choix parmi Red, Chuck et Bomb. Chacun a ses statistiques propres.\nVotre but est de récupérer un oeuf que les méchants cochons, les Picoos, vous ont volé. Déterminé comme jamais,\nvous devrez passer à travers différents stages et affronter différents Picoo pour récupérer votre précieux oeuf auprès du Maléfique King Picoo.")
    nom = ''
    while nom not in ['chuck', 'red', 'bomb']:
        nom = input('Quel personnage veux-tu ? Red, Chuck, Bomb').lower()  # on demande au joueur de choisir un oiseau
        if nom not in ['chuck', 'red', 'bomb']:
            print('Valeur invalide !')
    return Bird(nom)  # on crée un bird
