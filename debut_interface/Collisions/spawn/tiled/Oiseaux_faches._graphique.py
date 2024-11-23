#on importe les bibliothèques et modules dont on a besoin
import pygame
from pygame.locals import*
import pytmx
import sys

screen=pygame.display.set_mode((512,400))#on initialise la fenêtre
pygame.display.set_caption('Oiseaux Fâchés')#on lui donne un nom

def scale_by(image,factor) :
    """
    Fonction qui permet de changer les dimensions d'une image de manière proportionnelle étant donné que
    pygame.transform.scale_by refuse de fonctionner.
    Cette fonction prend donc comme paramètres image (l'image que l'on souhaite transformer) et factor (le facteur de redimmensionnement).
    Elle retourne l'image ainsi transformée.
    """
    return pygame.transform.scale(image,(image.get_rect().w*factor,image.get_rect().h))#on redimensionne l'image 

def crea_collisions(tmx_data) :
    """
    Fonction qui permet de créer les collisions de la map. Elle prend en paramètre un fichier .tmx importé via pytmx.
    Elle retourne une liste de rectangles qui forment alors les collisions.
    """
    collidable_tiles=[]#on initialise la liste vide
    for layer in tmx_data.visible_layers :#on traverse les différentes couches de la map
        if isinstance(layer,pytmx.TiledTileLayer) :#on vérifie qu'il s'agit bien d'un calque de tuiles
            for x,y, gid in layer :#on parcours les différentes tuiles du calque
                layer_properties=layer.properties#on prend les propriétés de layer, cad du calque
                if gid :#s'il y a une tuile
                    if layer_properties and layer_properties.get('collisions') :#si le calque a bien une ou des propriétés, et que la propriété collisions est vraie
                        collidable_tiles.append(pygame.Rect(x*tmx_data.tilewidth,
                                                            y*tmx_data.tileheight,
                                                            tmx_data.tilewidth,
                                                            tmx_data.tileheight))#on crée un rectangle de collisions à partir de la tuile.
    return collidable_tiles#on retourne la liste de collisions

def afficher_tiles(layer_name,tmx_data,screen) :
    """
    Fonction qui permet d'afficher un calque spécifique de la map.
    Elle prend en paramètres le nom du calque spécifié, les données tmx importées (e.g. pytmx.load_pygame('fichier.tmx')) et la fenêtre.
    Elle ne retourne rien puisqu'elle ne fait qu'afficher.
    """
    for layer in tmx_data.visible_layers :#on parcourt les différents calques de la map
        if isinstance(layer,pytmx.TiledTileLayer) :#s'il s'agit bien d'un calque de tuiles
            for x,y, gid in layer :#on parcourt chaque tuile du calque
                if gid and layer.name == layer_name :#s'il y a une tuile et que le calque a le nom donné
                    tile = tmx_data.get_tile_image_by_gid(gid)#on récupère l'image associé de la tuile dans le tileset
                    if tile :#s'il y a bien une image
                        screen.blit(tile, (x*tmx_data.tilewidth, y*tmx_data.tileheight))#on l'affiche sur l'écran

class Perso :
    "Définition d'un personnage"
    def __init__(self,x,y):
        """
        Initialisation du personnage
        """
        self.l_sprites={'haut':[pygame.transform.scale(pygame.image.load('red_sprite.png').convert_alpha(),(30,30))],
                        'bas': [pygame.transform.scale(pygame.image.load('red_sprite.png').convert_alpha(),(30,30))],
                        'droite' : [pygame.transform.scale(pygame.image.load('red_sprite.png').convert_alpha(),(30,30))],
                        'gauche' : [pygame.transform.scale(pygame.image.load('red_sprite.png').convert_alpha(),(30,30))]}#on crée un dictionnaire avec les différents sprites du personnage
        self.direction='bas'#on initialise sa direction ('bas' par défaut)
        self.nb_frames=len(self.l_sprites[self.direction])#on calcule le nombre de frames de son animation
        self.current_frame=0#on initialise la frame de départ à 0
        self.x,self.y=x,y#on initialise ses coordonnées
    def draw(self,screen) :
        """
        Méthode qui affiche le personnage sur l'écran.
        Elle prend donc en paramètres l'écran.
        """
        self.nb_frames=len(self.l_sprites[self.direction])#on récupère le nombre de frames de l'animation
        screen.blit(self.l_sprites[self.direction][int(self.current_frame)%self.nb_frames],(self.x,self.y))#et on affiche le personnage sur la map
    def get_rect(self) :
        """
        Méthode qui permet de récupérer le rectangle du perso.
        Elle ne prend aucun paramètre et retourne le rectangle du joueur.
        """
        self.nb_frames=len(self.l_sprites[self.direction])#on récupère le nombre de frames de son animation
        rect = self.l_sprites[self.direction][int(self.current_frame)%self.nb_frames].get_rect()#on récupère le rectangle de sa frame actuelle
        rect.topleft=(self.x,self.y)#on ajuste les coordonnées du rectangle
        return rect#on retourne le rectangle
    def get_collision(self,liste) :
        """
        Méthode permettant de retourner True si le joueur entre en collision avec un des rectangles de la liste de collisions.
        Elle prend en paramètre la liste en question.
        """
        rect_perso=self.get_rect()#on définit le rectangle du joueur
        for rect in liste :#pour chaque rectangle de la liste
            if rect_perso.colliderect(rect) :#si le joueur est en collision avec un rectangle de la liste
                return True#on retourne True
        return False#False sinon
            
def refresh(perso,map,screen,tmx_data) :
    """
    Fonction qui raffraîchit l'affichage du jeu.
    Elle ne retourne rien. Elle prend en paramètres le perso, la map, l'écran et les données tmx de la map.
    """
    screen.blit(map,(0,0))#on affiche la map
    perso.draw(screen)#on affiche le perso
    afficher_tiles('Front_decos',tmx_data,screen)#et on affiche les tuiles qui doivent être sur le perso
    pygame.display.flip()#on actualise l'affichage

tmx_data=pytmx.load_pygame('Level_0bis.tmx')#on initialise les données tmx de la première map
collidable_tiles={}#on initialise le dictionnaire des collisions
collidable_tiles['1']=crea_collisions(tmx_data)#et on ajoute les collisions de la map 1
map_key='1'#on initialise la clé qui correspond à la map
map=pygame.image.load('Level_0.png')#on initialise l'image de la map
bird=Perso(300,100)#le joueur
move=False#et on définit le déplacement à False au début


stop=False
while not stop :#tant qu'on n'arrête pas le jeu
    for event in pygame.event.get() :
        if event.type==QUIT :#si le joueur clique sur la croix
            pygame.quit()
            sys.exit()#on quitte le jeu
        if event.type==KEYDOWN :#s'il clique sur une touche
            if event.key in [K_RIGHT,K_LEFT,K_UP,K_DOWN] :#si la touche est l'une des quatres flèches
                move=True#on initialise le mouvement
                #on change la valeur de la direction du joueur (bird) en fonction de la touche cliquée
                if event.key == K_UP :
                    bird.direction='haut'
                elif event.key == K_DOWN :
                    bird.direction='bas'
                if event.key == K_RIGHT :
                    bird.direction='droite'
                elif event.key == K_LEFT :
                    bird.direction='gauche'
        elif event.type==KEYUP :#et s'il relève la touche
            if event.key in [K_RIGHT,K_LEFT,K_UP,K_DOWN] :
                #on arrête le mouvement
                if event.key == K_UP and bird.direction=='haut':
                    move=False
                elif event.key == K_DOWN and bird.direction=='bas' :
                    move=False
                elif event.key == K_RIGHT and bird.direction=='droite':
                    move=False
                elif event.key == K_LEFT and bird.direction=='gauche' :
                    move=False
    if move :
        #si le mouvement est en cours
        if bird.direction=='haut' :#s'il va vers le haut
            bird.y-=2#on change ses coordonnées
            if bird.get_collision(collidable_tiles['1']) :#mais s'il entre en collision avec un objet de la map
                bird.y+=2#on annule le mouvement
        elif bird.direction=='bas' :#s'il va vers le bas, on fait la même chose
            bird.y+=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.y-=2
        elif bird.direction=='droite' :#vers la droite
            bird.x+=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.x-=2
        if bird.direction=='gauche' :#et vers la gauche
            bird.x-=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.x+=2
    refresh(bird,map,screen,tmx_data)#on raffraîchit la map
