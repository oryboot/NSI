from .bird import Bird

bird_names = ['chuck', 'red', 'bomb']


def choose_character():
    character = input('Quel personnage veux-tu ? Red, Chuck, Bomb')
    character=character.lower()
    return character


def valid_name(name):
    if name in bird_names:
        return True
    else:
        return False


def assign_player_bird(name):
    player = Bird(name)
    return player

def create_player(start):
    if start:
        nom = choose_character()  # on demande au joueur de choisir un oiseau
        while not valid_name(nom):
            nom = choose_character()  # on demande au joueur de choisir un oiseau
            if valid_name(nom):
                print('Valeur invalide !')
        return assign_player_bird(nom)


def menu(play):
    while not play:
        print(
            "Bienvenue dans Oiseaux en Colère !\nDans ce jeu votre objectif sera d'éliminer la menace Picoo.\n\n   1-Débuter le jeu  2-Règles")
        choice = input()
        if choice == '2':
            print(
                "Voici les règles du jeu :\nVous incarnez un oiseau au choix parmi Red, Chuck et Bomb. Chacun a ses statistiques propres.\nVotre but est de récupérer un oeuf que les méchants cochons, les Picoos, vous ont volé. Déterminé comme jamais,\nvous devrez passer à travers différents stages et affronter différents Picoo pour récupérer votre précieux oeuf auprès du Maléfique King Picoo.")
        elif choice == '1':
            play = True
    return play
