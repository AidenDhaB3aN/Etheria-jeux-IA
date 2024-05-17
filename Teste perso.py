import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load('Image/background nuage.png').convert()
player_images = pygame.image.load('Image/Player stand.png').convert_alpha()
ground_image = pygame.image.load('Image/ground.png').convert()

screen.blit(background_image, (0, 0))
screen.blit(ground_image, (0, screen_height - ground_image.get_height()))  # Affichage du sol en bas de l'écran
player_pos = (screen_width // 2, screen_height // 2)  # Position initiale du personnage au centre de l'écran
player_index = 0  # Index du sprite du personnage
screen.blit(player_images, player_pos)
pygame.display.flip()  # Met à jour l'affichage

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Mise à jour des positions (par exemple, pour que le personnage se déplace vers la droite)
    player_pos = (player_pos[0] + 1, player_pos[1])  # Déplacement de 1 pixel vers la droite
    
    # Changement de sprite du personnage pour l'animation
   # player_index = (player_index + 1) % len(player_images)  # Boucle à travers les images du personnage
    
    # Affichage des éléments
    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (0, screen_height - ground_image.get_height()))
    screen.blit(player_images, player_pos)
    pygame.display.flip()  # Met à jour l'affichage
    
    # Pause pour éviter que le jeu ne fonctionne trop vite
    pygame.time.delay(10)
