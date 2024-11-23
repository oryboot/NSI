def maximum(char):
    """
    On définit une fonction qui à  partir d'une liste char retourne l'indice du 'personnage' qui a la plus grande vitesse cette liste.
    """
    max_indice = 0  # on initialise l'indice
    for i in range(len(char)):  # pour chaque indice de la liste
        if char[i].vitesse > char[
            max_indice].vitesse:  # si la vitesse du personnage à  l'indice i est supérieure à  celle du personnage au rang max_indice
            max_indice = i  # on change l'indice max_indice
    return max_indice  # on retourne l'indice du maximum


def verif_int(input_j):
    """
    Fonction qui permet de vérifier qu'un input d'un joueur input_j peut être converti en int
    """
    try:
        int(input_j)
        return True
    except:
        return False


def sort_speed(char):
    """
    On définit une fonction qui permet de trier une liste char par ordre décroissant (la plus grande valeur à  l'indice 0) des vitesses des personnages de la liste
    """
    new = []  # on crée une liste vide
    while len(char) != 0:  # tant qu'il y a encore des éléments dans la liste char
        new.append(char.pop(maximum(char)))  # on ajoute le personnage qui a la plus grande vitesse à  la liste new
    return new  # on retourne la liste avec les personnages triés
