import random
import time
from .menu import menu
from .picoo import Picoo
from .combat_mecanic import combat, combat_multiple


def jeu():
    """
    On définit la fonction principale du jeu.
    """
    perso = menu()
    picoo_list = ['Minion']  # on crée une liste de types possibles de picoo/cochon
    print(f'{perso.nom} et ses amis s\'endormaient paisiblement autour de leur précieux oeuf...')
    time.sleep(2.5)
    print(f'Soudain une horde de Picoos débarque et saccage tout. Alors que {perso.nom} dort encore paisiblement, ses amis sont enlevés et l\'oeuf est subtilisé...')
    time.sleep(3)
    print(f'{perso.nom} se réveille seul...')
    time.sleep(1.5)
    print("Il se rend compte que l'oeuf et ses amis ont disparu. Mais il reconnaît les traces laissés par les vils Picoo...")
    time.sleep(4)
    print('Il décide de suivre ses traces et se met alors en quête du précieux oeuf.')
    print("")
    time.sleep(2)
    stage = 1  # on initialise le numéro du stage
    lieu = 'la forêt.'  # on précise le lieu du perso pour donner du contexte
    print(f'Vous entrez dans {lieu}')
    time.sleep(3)
    stop = False
    while not stop:
        while stage < 9:  # jusqu'au stage 9
            picoo = Picoo(
                random.choice(picoo_list))  # on choisit un type de cochon au hasard dans la liste)#on crée un cochon
            if stage == 2:  # si on est au stage 2
                picoo_list.append('Corporal')  # on ajoute corporal à  la liste de cochons possibles
            if stage == 4:  # et si on est au stage 4
                picoo_list.append('Fat')  # on ajoute Fat à  la liste des cochons
                lieu = 'les mines.'
                print('Vous entrez dans les mines.')
                time.sleep(3)
            print(f'Stage {stage}: {perso.nom} affronte {picoo.nom} dans {lieu}')  # on annonce le stage et on précise les opposants
            if combat(perso, picoo):  # si le joueur remporte le combat
                print(f'Stamina :{perso.stamina}- PV {perso.nom}: {perso.PV}/{perso.PVmax} // PV {picoo.nom}: {picoo.PV}')  # on annonce le résultat
                print(f'{picoo.nom} est K.O.')  # on précise que le picoo est K.O.
                print('Bravo! Vous passez au stage suivant.')
                perso.gain_xp(30)  # on ajoute de l'XP au joueur
                print('+30 XP')
                print(f'XP :{perso.XP}, Niveau :{perso.niveau}')
                print('')
                if perso.PV + 25 <= perso.PVmax:  # si les PV du joueur le permettent
                    perso.PV += 25  # on en rajoute aux joueurs
                perso.stamina += 10  # on augmente sa stamina
                if perso.stamina >= perso.staminamax:  # si la stamina obtenue est supérieure à  la stamina max
                    perso.stamina = perso.staminamax  # on lui donne la valeur de la stamina max
                stage += 1  # on augmente le stage
            else:  # s'il perd
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1':  # on lui demande s'il souhaite reprendre
                    perso.PV = perso.PVmax  # on remet ses stats au maximum
                    perso.stamina = perso.staminamax
                else:
                    print('Êtes-vous sûr de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif:  # tant que la réponse n'est pas valide
                        rep = input()  # on redemande au joueur
                        if rep in ['1', '2']:  # sinon  on confirme qu'il veuille bien quitter
                            if rep == '1':
                                stop = True  # on arrête le jeu
                            else:  # sinon on remet ses stats au maximum
                                perso.PV = perso.PVmax
                                perso.stamina = perso.staminamax
                                verif = True
                        else:
                            print('Format invalide !')
        while stage == 9:  # au stage 9 on change de mode de jeu
            lieu = 'Château'
            print('Vous entrez dans le château.')
            time.sleep(3)
            enemies = [Picoo(random.choice(picoo_list)) for i in range(3)]  # liste des ennemis
            print(f'Stage {stage}: {perso.nom} affronte {enemies[0].nom}, {enemies[1].nom} et {enemies[2].nom}')
            if combat_multiple(perso, enemies):  # si le joueur est vainqueur
                print('Bravo! Vous passez au stage suivant.')  # on augmente ses stats
                perso.gain_xp(60)
                print('+60 XP')
                print(f'XP :{perso.XP}, Niveau :{perso.niveau}')
                print('')
                perso.stamina = perso.staminamax
                stage += 1
            else:
                print('Game Over')
                print('')
                perso.PV = perso.PVmax  # on remet ses stats au maximum
                perso.stamina = perso.staminamax
        while stage == 10:  # tant qu'il est au stage 10
            perso.PV = perso.PVmax
            perso.stamina = perso.staminamax
            perso.tour = True
            print('')
            print('Vous entrez finalement dans la demeure de King Picoo.')
            time.sleep(3)
            print('Il vous attendait...')
            time.sleep(2)
            print('Vous engagez le combat sans plus attendre.')
            print('')
            Roi = Picoo('King Picoo')  # on crée le boss
            tour = 0
            ennemi_tour = True
            while Roi.PV > 0 and perso.PV > 0:  # tant que les deux ont encore des PV
                tour += 1
                print('')
                time.sleep(1)
                print(f'{perso.nom}: Stamina: {perso.stamina}, PV:{perso.PV}/{perso.PVmax}// PV {Roi.nom}: {Roi.PV}/{Roi.PVmax}')  # on rappelle les PV de chacun
                if perso.vitesse > Roi.vitesse:  # si le personnage est plus rapide que le King Picoo
                    if perso.tour:
                        perso.attaquer(Roi)  # il attaque en premier
                    if Roi.PV > 0 and ennemi_tour:  # si le roi a encore des PV et qu'il peut jouer
                        if tour % 3 == 0:  # tous les trois tours
                            if 2 * Roi.PVmax // 3 < Roi.PV < Roi.PVmax:  # si le roi est dans son troisième tiers de PV
                                print('King Picoo envoie 3 Minions')
                                time.sleep(2)
                                combat_multiple(perso, [Picoo('Minion') for i in
                                                        range(3)])  # il envoie trois Minions au combat
                            if Roi.PVmax // 3 < Roi.PV < 2 * Roi.PVmax // 3:  # s'il est dans son deuxième tiers
                                print('King Picoo invoque 3 Corporal')
                                time.sleep(3)
                                combat_multiple(perso,
                                                [Picoo('Corporal') for i in range(3)])  # il envoie trois corporal
                            else:  # s'il est dans son premier tiers
                                print('King Picoo est très en colère. \nIl invoque trois Picoos.')
                                time.sleep(3)
                                combat_multiple(perso, [Picoo(random.choice(['Fat', 'Corporal'])) for i in range(
                                    3)])  # il envoie de manière aléatoire trois picoos parmi Corporal et Fat
                        else:  # le reste du temps
                            Roi.attaquer(perso)  # le roi attaque le joueur
                else:  # si le roi est plus rapide que le joueur
                    if ennemi_tour:
                        Roi.attaquer(perso)  # il attaque le joueur en premier
                    if perso.PV > 0:
                        if perso.tour:
                            perso.attaquer(Roi)  # puis s'il est en vie, le joueur attaque
            if Roi.PV <= 0:  # si le roi meurt
                print('Bravo! Vous avez vaincu King Picoo')  # on félicite le joueur
                time.sleep(2)
                print("Vous avez récupéré l'oeuf !")
                stage += 1  # on arrête le jeu
            else:  # si le joueur meurt
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1':  # on lui demande s'il souhaite reprendre
                    perso.PV = perso.PVmax  # on remet ses stats au maximum
                    perso.stamina = perso.staminamax
                else:
                    print('Êtes-vous sûr de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif:  # tant que la réponse n'est pas valide
                        rep = input()  # on redemande au joueur
                        if rep in ['1', '2']:  # sinon  on confirme qu'il veuille bien quitter
                            if rep == '1':
                                stage += 1
                                stop = True  # on arrête le jeu
                            else:  # sinon on remet ses stats au maximum
                                perso.PV = perso.PVmax
                                perso.stamina = perso.staminamax
                                verif = True
                        else:
                            print('Format invalide !')

        stop = True  # on arrête le jeu

