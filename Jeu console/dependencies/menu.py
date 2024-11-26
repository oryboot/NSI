from .bird import Red, Chuck, Bomb, birds_data

bird_names = ['chuck', 'red', 'bomb']


def choose_character():
    """
    Fonction qui demande à l'utlisateur de choisir un oiseau.
    Elle renvoie le nom de l'oiseau en question en minuscules.
    """
    character = input('Quel personnage veux-tu ? Red, Chuck, Bomb').lower()
    return character


def valid_name(name):
    """
    Fonction permettant de vérifier qu'un nom (string) est bien dans la liste des noms de bird possibles.
    Elle renvoie True si c'est le cas, False sinon
    """
    if name in bird_names:
        return True
    else:
        return False


def assign_bird(name):
    """
    Fonction qui permet d'attribuer au joueur l'oiseau correspondant au nom choisi qui est donné en argument.
    Elle retourne le 'joueur' alors créé.
    """
    if name == 'red':
        player = Red(**birds_data['Red'])#si le nom donné est red, on crée un Red
    elif name == 'chuck':
        player = Chuck(**birds_data['Chuck'])#si c'est chuck, on crée un Chuck 
    elif name == 'bomb':
        player = Bomb(**birds_data['Bomb'])#et si c'est bomb, on crée un Bomb
    return player

def create_player():
    """
    Fonction qui crée un oiseau en demandant au joueur de le choisir.
    On retourne cet oiseau ainsi créé.
    """
    nom = choose_character()  # on demande au joueur de choisir un oiseau
    while not valid_name(nom):#tant que le format du nom  n'est pas valide
        print('Valeur invalide !')
        nom = choose_character()  # on redemande au joueur de choisir un oiseau
    return assign_bird(nom)#on retourne l'oiseau créé


def menu(start_game):
    """
    Fonction qui lance le menu du jeu. Elle prend en paramètre un booléen start_game et retourne ce même booléen.
    """
    while not start_game:#tant qu'on ne lance pas le jeu
        print("Bienvenue dans Oiseaux en Colère !\nDans ce jeu votre objectif sera d'éliminer la menace Picoo.\n\n   1-Commencer le jeu  2-Règles")#on affiche l'introduction et on demande au joueur s'il souhaite jouer.
        choice = input()
        if choice == '2':#si le joueur choisit d'afficher les règles
            print("Voici les règles du jeu :\nVous incarnez un oiseau au choix parmi Red, Chuck et Bomb. Chacun a ses statistiques propres.\nVotre but est de récupérer un oeuf que les méchants cochons, les Picoos, vous ont volé. Déterminé comme jamais,\nvous devrez passer à travers différents stages et affronter différents Picoo pour récupérer votre précieux oeuf auprès du Maléfique King Picoo.")#on les affiche
        elif choice == '1':#s'il choisit de commencer le jeu
            start_game = True#on donne la valeur True à la variable start_game
    return start_game
