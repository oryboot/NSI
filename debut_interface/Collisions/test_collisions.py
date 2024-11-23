import pygame
import pytmx
from pygame.locals import*

def scale_by(image,factor) :
    return pygame.transform.scale(image,(image.get_rect().w*factor,image.get_rect().h*factor))

screen=pygame.display.set_mode((480,480))
pygame.display.set_caption('Test collisions')
map=pygame.image.load('debut_interface/Collisions/map.png').convert_alpha()
map=scale_by(map,2)

tmx_data=pytmx.load_pygame('debut_interface/Collisions/collision.tmx')

collidable_tiles=[]

for layer in tmx_data.visible_layers :
    if isinstance(layer,pytmx.TiledTileLayer) :
        for x,y, gid in layer :
            if gid :
                tile_properties=tmx_data.get_tile_properties_by_gid(gid)
                if tile_properties and tile_properties.get('collidable') :
                    collidable_tiles.append(pygame.Rect(2*x*tmx_data.tilewidth,
                                                        2*y*tmx_data.tileheight,
                                                        2*tmx_data.tilewidth,
                                                        2*tmx_data.tileheight))

class Perso :
    "Définition d'un personnage"
    def __init__(self,nom,x,y):
        self.l_sprites={'haut':[pygame.image.load("animations_sprites/images/"+nom+'_h'+str(i)+'.png') for i in range(1,10)],
                        'bas': [pygame.image.load("animations_sprites/images/"+nom+str(i)+'.png') for i in range(1,10)],
                        'droite' : [pygame.image.load("animations_sprites/images/"+nom+'_d'+str(i)+'.png') for i in range(1,9)],
                        'gauche' : [pygame.transform.flip(pygame.image.load("animations_sprites/images/"+nom+'_d'+str(i)+'.png'),True,False) for i in range(1,9)]}
        self.direction='bas'
        self.nb_frames=len(self.l_sprites[self.direction])
        self.current_frame=0
        self.x=x
        self.y=y
        self.pos=(self.x,self.y)
    def draw(self,screen) :
        self.nb_frames=len(self.l_sprites[self.direction])
        screen.blit(self.l_sprites[self.direction][int(self.current_frame)%self.nb_frames],(self.x,self.y))
    def get_rect(self) :
        self.nb_frames=len(self.l_sprites[self.direction])
        rect = self.l_sprites[self.direction][int(self.current_frame)%self.nb_frames].get_rect()
        rect.topleft=(self.x,self.y)
        rect.height+=2
        rect.width+=2
        return rect
    def get_collision(self,liste) :
        for rect in liste :
            if perso.get_rect().colliderect(rect) :
                return True

class Enemy :
    "définition d'un ennemi"
    def __init__(self,nom) :
        self.sprites=[pygame.image.load("animations_sprites/images/"+nom+''+str(i)+'.png') for i in range (1,4)]
        self.idle=pygame.image.load("animations_sprites/images/"+nom+'_idle.png')
        self.x=250
        self.y=300
        self.pos=(self.x,self.y)
        self.direction='droite'
        self.nb_frames=len(self.sprites)
        self.current_frame=0
    def draw(self, screen) :
        self.nb_frames=len(self.sprites)
        if self.direction == 'gauche' :
            screen.blit(self.sprites[int(self.current_frame)%self.nb_frames],(self.x,self.y))
        elif self.direction=='droite' :
            screen.blit(pygame.transform.flip(self.sprites[int(self.current_frame)%self.nb_frames],True,False),(self.x,self.y))
        else :
            screen.blit(self.idle,(self.x,self.y))

clock=pygame.time.Clock()
perso=Perso('zelda',30,30)
lapin=Enemy('lapin')
direction='bas'
move=False
stop=False
while not stop :
    for event in pygame.event.get() :
        if event.type==QUIT :
            pygame.quit()
        keys=pygame.key.get_pressed()
        if event.type==KEYDOWN and event.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT]:
            move=True
            if event.key==K_UP :
                perso.direction='haut'
            if event.key==K_DOWN :
                perso.direction='bas'
            if event.type==K_RIGHT :
                perso.direction='droite'
            if event.type==K_LEFT :
                perso.direction='gauche'
        elif event.type==KEYUP :
            if event.key==K_UP and perso.direction=='haut':
                perso.current_frame=0
                move=False
            if event.key==K_DOWN and perso.direction=='bas':
                perso.current_frame=0
                move=False
            if event.key==K_RIGHT and perso.direction=='droite':
                perso.current_frame=0
                move=False
            if event.key==K_LEFT and perso.direction=='gauche':
                perso.current_frame=0
                move=False
    if move :
        if perso.direction=='gauche' :
            perso.x-=2
            if perso.get_collision(collidable_tiles) :
                perso.x+=3
        if perso.direction=='droite' :
            perso.x+=2
            if perso.get_collision(collidable_tiles) :
                perso.x-=3
        if perso.direction=='haut' :
            perso.y-=2
            if perso.get_collision(collidable_tiles) :
                perso.y+=3
        if perso.direction=='bas' :
            perso.y+=2
            if perso.get_collision(collidable_tiles) :
                perso.y-=3
        perso.current_frame+=0.08
    else:
        perso.current_frame=0
    
    if lapin.pos != perso.pos :
        if lapin.x<perso.x :
            lapin.x+=0.5
            lapin.direction='droite'
        if lapin.x>perso.x :
            lapin.x-=0.5
            lapin.direction='gauche'
        if lapin.y<perso.y :
            lapin.y+=0.5
        if lapin.y>perso.y :
            lapin.y-=0.5
        lapin.current_frame+=0.03
    else :
        lapin.current_frame=0
        lapin.direction='idle'
    clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(map,(0,0))
    perso.draw(screen)
    lapin.draw(screen)
    pygame.display.flip()
