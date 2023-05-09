import pygame
import textwrap
# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeopardy")

# Definir colores
background_color = (0, 0, 255)
button_color = (0, 0, 255)

# Definir fuente
font = pygame.font.SysFont("Arial", 20)

# Definir títulos
titles = ["Arte", "Cine", "Geografía", "Música"]

# Definir tamaño de botones
button_width = 80
button_height = 80

# Definir margen entre botones
margin = 10


# Definir posición inicial de la cuadrícula
x_start = (screen_width - (button_width * 4 + margin * 3)) // 2
y_start = (screen_height - (button_height * 4 + margin * 3)) // 2

# Dibujar botones y títulos
for i in range(4):
    for j in range(4):
        button_rect = pygame.Rect(x_start + (button_width + margin) * i, y_start + (button_height + margin) * j, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect)
        if j == 0:
            title_text = font.render(titles[i], True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(x_start + (button_width + margin) * i + button_width // 2, y_start))
            screen.blit(title_text, title_rect)

# Actualizar pantalla
pygame.display.update()

# Esperar a que se cierre la ventana
# Define dictionary that maps titles to questions
questions = {
    "Arte":    "¿Quién pintó 'La Gioconda'?",
    "Música":  "¿Qué banda compuso la canción 'Bohemian Rhapsody'?",
    "Geografía":  "¿Cuál es el país más grande del mundo en términos de superficie?",   
    "Cine":"¿Quién interpretó a Forrest Gump en la película del mismo nombre?"}


# Esperar a que se cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(4):
                for j in range(4):
                    button_rect = pygame.Rect(x_start + (button_width + margin) * i, y_start + (button_height + margin) * j, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        # Get title of button that was clicked
                        title = titles[i]
                        
                        # Get corresponding question from dictionary
                        question = questions[title]
                        
                        # Draw black screen
                        screen.fill((0, 0, 0))
                        
                        # Draw question in white font
                        question_text = font.render(question, True, (255, 255, 255))
                        question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 2))
                        screen.blit(question_text, question_rect)
                        
                        # Update screen
                        pygame.display.update()