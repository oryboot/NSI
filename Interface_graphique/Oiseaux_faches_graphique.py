#on importe les bibliothèques et modules dont on a besoin
import pygame
import math
from pygame.locals import*
import pytmx
import sys

screen=pygame.display.set_mode((512,400))#on initialise la fenêtre
pygame.display.set_caption('Oiseaux Fâchés')#on lui donne un nom
pygame.mixer.init()

# Initialisation d'images obscènes

def scale_by(image,factor) :
    """
    Fonction qui permet de changer les dimensions d'une image de manière proportionnelle étant donné que
    pygame.transform.scale_by refuse de fonctionner.
    Cette fonction prend donc comme paramètres image (l'image que l'on souhaite transformer) et factor (le facteur de redimmensionnement).
    Elle retourne l'image ainsi transformée.
    """
    return pygame.transform.scale(image,(image.get_rect().w*factor,image.get_rect().h))#on redimensionne l'image 

def any_dict(dict) :
    """
    Fonction qui permet de vérifier s'il y a au moins une valeur True dans un dictionnaire donné en argument.
    Elle retourne alors True si c'est le cas.
    """
    occurences=[]
    for value in dict.values() :
        occurences.append(value)
    return any(occurences)

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
        self.l_sprites={'haut':[pygame.transform.scale(pygame.image.load('Interface_graphique/tmx_and_tilesets/red_sprite.png').convert_alpha(),(30,30))],
                        'bas': [pygame.transform.scale(pygame.image.load('Interface_graphique/tmx_and_tilesets/red_sprite.png').convert_alpha(),(30,30))],
                        'droite' : [pygame.transform.scale(pygame.image.load('Interface_graphique/tmx_and_tilesets/red_sprite.png').convert_alpha(),(30,30))],
                        'gauche' : [pygame.transform.scale(pygame.image.load('Interface_graphique/tmx_and_tilesets/red_sprite.png').convert_alpha(),(30,30))]}#on crée un dictionnaire avec les différents sprites du personnage
        self.direction='bas'#on initialise sa direction ('bas' par défaut)
        self.directions={'bas':False,'haut':False,'gauche':False,'droite':False}
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
        rect.topleft=(self.x,self.y+12)#on ajuste les coordonnées du rectangle
        rect.height=20
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
            
def refresh(perso,map,screen,tmx_data,clonelist) :
    """
    Fonction qui raffraîchit l'affichage du jeu.
    Elle ne retourne rien. Elle prend en paramètres le perso, la map, l'écran et les données tmx de la map.
    """
    screen.blit(map,(0,0))#on affiche la map
    perso.draw(screen)#on affiche le perso
    afficher_tiles('Front_decos',tmx_data,screen)#et on affiche les tuiles qui doivent être sur le perso
    PiggyAI(bird,clonelist)
    pygame.display.flip()#on actualise l'affichage

class Clone :
    """
    Crée un clone cochon sur un endroit de la carte :3
    """
    def __init__(self,name,x,y,spd_x,spd_y,x_dest,y_dest) :
        self.name=name
        self.x=x
        self.y=y
        self.spd_x=spd_x
        self.spd_y=spd_y
        self.x_dest=x_dest
        self.y_dest=y_dest
        self.sprite = pygame.transform.scale(pygame.image.load("Interface_graphique/tmx_and_tilesets/"+self.name+".png").convert_alpha(),(25,25))



def PiggyAI(bird,clonelist):
    """
    Déplacements du cochon sur la carte en fonction de la position du joueur
    """
    liste_indices_a_supprimer = []
    
    if len(clonelist)==0:
        clonelist.append(Clone("minion",200,200,1.5,1.5,bird.x,bird.y))
    print(clonelist)
    

    for i in range(len(clonelist)):
        screen.blit(clonelist[i].sprite,(clonelist[i].x,clonelist[i].y))
        detectcollision = pygame.Rect(clonelist[i].x,clonelist[i].y,150,150)

        rect_perso = pygame.Rect(bird.x,bird.y,32,32)
        
        if rect_perso.colliderect(detectcollision)==1:
            print("spotted")

            vx = bird.x-clonelist[i].x # calcul de la distance x entre le clone et le perso
            vy = bird.y-clonelist[i].y # calcul de la distance y entre le clone et le perso
            print(vx,vy)

            clonelist[i].x += (vx*clonelist[i].spd_x) /math.sqrt(vx*vx+vy*vy) 
            clonelist[i].y += (vy*clonelist[i].spd_y) /math.sqrt(vx*vx+vy*vy) #mouvement du clone normalisé
            print(i, clonelist[i].x, clonelist[i].y)
            
            #vx = clonelist[i].x_dest-clonelist[i].x
            #vy = clonelist[i].y_dest-clonelist[i].y
            # liste_indices_a_supprimer = [i]+liste_indices_a_supprimer

            hitcollision = pygame.Rect(clonelist[i].x,clonelist[i].y,25,25)
            if rect_perso.colliderect(hitcollision)==1 and i not in liste_indices_a_supprimer:
                liste_indices_a_supprimer.append(i)
                print("deleting clone")
                
            if clonelist[i].name == "minion":
                    screen.blit(clonelist[i].sprite,(clonelist[i].x,clonelist[i].y))
            
        for i in liste_indices_a_supprimer :
                clonelist.pop(i)

tmx_data=pytmx.load_pygame('Interface_graphique/tmx_and_tilesets/Level_0bis.tmx')#on initialise les données tmx de la première map
collidable_tiles={}#on initialise le dictionnaire des collisions
collidable_tiles['1']=crea_collisions(tmx_data)#et on ajoute les collisions de la map 1
map_key='1'#on initialise la clé qui correspond à la map
map=pygame.image.load('Interface_graphique/tmx_and_tilesets/Level_0.png')#on initialise l'image de la map
bird=Perso(300,100)#le joueur
move=False#et on définit le déplacement à False au début
pygame.mixer.music.load('Interface_graphique/Sounds/forest_theme.mp3')
pygame.mixer.music.play()
clonelist=[]

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
                    bird.directions['haut']=True
                    bird.direction='haut'
                elif event.key == K_DOWN :
                    bird.directions['bas']=True
                    bird.direction='bas'
                if event.key == K_RIGHT :
                    bird.directions['droite']=True
                    bird.direction='droite'
                elif event.key == K_LEFT :
                    bird.directions['gauche']=True
                    bird.direction='gauche'
        elif event.type==KEYUP :#et s'il relève la touche
            if event.key in [K_RIGHT,K_LEFT,K_UP,K_DOWN] :
                #on arrête le mouvement
                if event.key == K_UP and bird.directions['haut']:
                    bird.directions['haut']=False
                elif event.key == K_DOWN and bird.directions['bas'] :
                    bird.directions['bas']=False
                elif event.key == K_RIGHT and bird.directions['droite']:
                    bird.directions['droite']=False
                elif event.key == K_LEFT and bird.directions['gauche'] :
                    bird.directions['gauche']=False
    
    if any_dict(bird.directions) :
        #si le mouvement est en cours
        if bird.directions['haut'] :#s'il va vers le haut
            bird.y-=2#on change ses coordonnées
            if bird.get_collision(collidable_tiles['1']) :#mais s'il entre en collision avec un objet de la map
                bird.y+=2#on annule le mouvement
        if bird.directions['bas'] :#s'il va vers le bas, on fait la même chose
            bird.y+=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.y-=2
        if bird.directions['droite'] :#vers la droite
            bird.x+=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.x-=2
        if bird.directions['gauche'] :#et vers la gauche
            bird.x-=2
            if bird.get_collision(collidable_tiles['1']) :
                bird.x+=2
    refresh(bird,map,screen,tmx_data,clonelist)#on raffraîchit la map
    

