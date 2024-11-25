from dependencies.game_logic import jeu
from dependencies.menu import menu, create_player

play = False

selected_play = menu(play)
player = create_player(selected_play)
jeu(player)
