import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 800, 600
player_size = 50
ground_height = 50
gravity = 1
jump_height = 15

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario Bros Platformer")


# Position initiale du joueur
player_x = width // 2
player_y = height - ground_height - player_size

# Variables de mouvement du joueur
player_x_speed = 5
player_y_speed = 0
is_jumping = False

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des touches de déplacement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player_x_speed = 5
            elif event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_y_speed = -jump_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_speed = 0

    # Mise à jour de la position du joueur
    player_x += player_x_speed
    player_y += player_y_speed

    # Appliquer la gravité
    player_y_speed += gravity

    # Si le joueur touche le sol, réinitialiser le saut
    if player_y >= height - ground_height - player_size:
        player_y = height - ground_height - player_size
        is_jumping = False

    # Effacer l'écran
    screen.fill(white)

    # Dessiner le joueur
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))

    # Dessiner le sol
    pygame.draw.rect(screen, black, (0, height - ground_height, width, ground_height))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôle de la fréquence d'images
    pygame.time.Clock().tick(30)