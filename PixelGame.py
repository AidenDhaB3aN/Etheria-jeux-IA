import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load('Image/background nuage2.png').convert()
ground_image = pygame.image.load('Image/sol test.png').convert()

player_image = pygame.image.load('Image/Player idle.png').convert_alpha()

player_pos = [0, screen_height // 2]  # Position initiale du personnage à gauche de l'écran
player_jump = False  # Le personnage ne saute pas initialement
player_facing_left = False  # Variable pour vérifier si le personnage regarde à gauche

# Image du saut du joueur
player_jump_image = pygame.image.load('Image/Player Jump.png').convert_alpha()

# Créez des masques de collision pour le personnage et le sol
player_mask = pygame.mask.from_surface(player_image)
ground_mask = pygame.mask.from_surface(ground_image)


# Obtenez le rectangle de collision pour le sol
ground_rect = ground_image.get_rect()
# Abaissez le rectangle de collision du sol
ground_rect.y = screen_height + ground_image.get_height()  # Augmentez la valeur pour abaisser la collision

# Gravité
gravity = 0.5
# Vitesse verticale initiale du personnage
player_y_velocity = 0


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player_pos[0] += 3  # Augmentation de la vitesse de déplacement
        player_facing_left = False  # Le personnage regarde à droite
    if keys[K_LEFT]:
        player_pos[0] -= 3  # Augmentation de la vitesse de déplacement
        player_facing_left = True  # Le personnage regarde à gauche
    if keys[K_SPACE] and not player_jump:
        player_jump = True  # Le personnage saute
        player_jump_count = 10  # Nombre de sauts

    # Faire sauter le personnage
    if player_jump:
        if player_jump_count >= -10:
            neg = 1
            if player_jump_count < 0:
                neg = -1
            player_pos[1] -= (player_jump_count ** 2) * 0.2 * neg  # Formule de saut
            player_jump_count -= 1
        else:
            player_jump = False
            player_jump_count = 5

    # Vérification de la collision avec le sol
    player_rect = player_image.get_rect(topleft=player_pos)
    overlap_area = player_mask.overlap_area(ground_mask, (player_rect.x - ground_rect.x, player_rect.y - ground_rect.y))
    if overlap_area > 0:
        player_pos[1] = ground_rect.y

    # Calculer les coordonnées de la caméra pour suivre le personnage
    camera_x = max(0, player_pos[0] - screen_width // 2)
    camera_y = max(0, player_pos[1] - screen_height // 2)

    # Affichage des éléments
    screen.blit(background_image, (0 - camera_x, 0 - camera_y))
    screen.blit(ground_image, (0 - camera_x, screen_height - ground_image.get_height() - camera_y))

    # Affichage de l'image appropriée du personnage
    if player_jump:
        screen.blit(player_jump_image, (player_pos[0] - camera_x, player_pos[1] - camera_y))
    else:
        if player_facing_left:
            player_image_flipped = pygame.transform.flip(player_image, True, False)
            screen.blit(player_image_flipped, (player_pos[0] - camera_x, player_pos[1] - camera_y))
        else:
            screen.blit(player_image, (player_pos[0] - camera_x, player_pos[1] - camera_y))

    pygame.display.flip() 
    
    # Met à jour l'affichage
    clock.tick(60)




