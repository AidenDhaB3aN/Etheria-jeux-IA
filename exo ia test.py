import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de Plateforme")

# Couleurs
blanc = (255, 255, 255)

# Personnage
personnage_taille = 50
personnage_x = (largeur_fenetre - personnage_taille) // 2
personnage_y = hauteur_fenetre - personnage_taille - 20
personnage_vitesse = 5
saut = False
saut_compteur = 10

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and personnage_x > 0:
        personnage_x -= personnage_vitesse
    if touches[pygame.K_RIGHT] and personnage_x < largeur_fenetre - personnage_taille:
        personnage_x += personnage_vitesse

    # Gestion du saut
    if not saut:
        if touches[pygame.K_SPACE]:
            saut = True
    else:
        if saut_compteur >= -10:
            neg = 1
            if saut_compteur < 0:
                neg = -1
            personnage_y -= (saut_compteur ** 2) * 0.5 * neg
            saut_compteur -= 1
        else:
            saut = False
            saut_compteur = 10

    # Effacer l'écran
    fenetre.fill(blanc)

    # Dessiner le personnage
    pygame.draw.rect(fenetre, (0, 128, 255), (personnage_x, personnage_y, personnage_taille, personnage_taille))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de rafraîchissement
    pygame.time.Clock().tick(60)