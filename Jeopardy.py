import pygame


WIDTH, HEIGHT = 900, 500
SQUARE_SIZE = (150, 100)
MARGIN = 10
TOP_MARGIN = 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeopardy!")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 60

# Define los títulos y sus posiciones
titles = ["Category 1", "Category 2", "Category 3", "Category 4"]
title_positions = [(WIDTH - (SQUARE_SIZE[0] + MARGIN) * 4) / 2 + col * (SQUARE_SIZE[0] + MARGIN) for col in range(4)]

# Define los valores de puntos
points = [[100, 100, 100, 100],
          [150, 150, 150, 150],
          [250, 250, 250, 250],
          [400, 400, 400, 400]]

preguntas = {
    "Arte": {
        100: {"pregunta": "¿Quién pintó 'La Gioconda'?", "respuestas": {"a": "Leonardo da Vinci", "b": "Michelangelo", "correcta": "a"}},
        150: {"pregunta": "¿Quién diseñó el edificio Guggenheim de Bilbao?", "respuestas": {"a": "Frank Gehry", "b": "Zaha Hadid", "correcta": "a"}},
        300: {"pregunta": "¿En qué ciudad italiana se encuentra la Capilla Sixtina?", "respuestas": {"a": "Roma", "b": "Florencia", "correcta": "a"}},
        400: {"pregunta": "¿Cuál es el nombre del cuadro de Edward Hopper en el que una mujer está sentada sola en un restaurante?", "respuestas": {"a": "Nighthawks", "b": "American Gothic", "correcta": "b"}}
    },
    "Música": {
        100: {"pregunta": "¿Qué banda compuso la canción 'Bohemian Rhapsody'?", "respuestas": {"a": "Queen", "b": "The Beatles", "correcta": "a"}},
        150: {"pregunta": "¿Cuál es el nombre del primer álbum de Adele?", "respuestas": {"a": "19", "b": "21", "correcta": "a"}},
        300: {"pregunta": "¿Quién compuso la 'Quinta Sinfonía'?", "respuestas": {"a": "Ludwig van Beethoven", "b": "Wolfgang Amadeus Mozart", "correcta": "a"}},
        400: {"pregunta": "¿Qué banda de rock lideró Mick Jagger?", "respuestas": {"a": "The Rolling Stones", "b": "The Who", "correcta": "a"}}
    },
    "Geografía": {
        100: {"pregunta": "¿Cuál es el país más grande del mundo en términos de superficie?", "respuestas": {"a": "Rusia", "b": "China", "correcta": "a"}},
        150: {"pregunta": "¿En qué país se encuentra la ciudad de Praga?", "respuestas": {"a": "República Checa", "b": "Polonia", "correcta": "a"}},
        300: {"pregunta": "¿Cuál es la capital de Australia?", "respuestas": {"a": "Melbourne", "b": "Canberra", "correcta": "b"}},
        400: {"pregunta": "¿Qué ciudad es la más poblada de África?", "respuestas": {"a": "Lagos", "b": "El Cairo", "correcta": "a"}}
    },
    "Cine": {
        100:{"pregunta": "¿Quién interpretó a Forrest Gump en la película del mismo nombre?", "respuestas": {"a": " Tom Hanks", "b": "Robert De Niro", "correcta": "a"}},
        150: {"pregunta": "¿Qué película ganó el Oscar a la Mejor Película en el año 2021?", "respuestas": {"a": "Nomadland", "b": "The Trial of the Chicago 7", "correcta": "a"}},
        300: {"pregunta": "¿Qué actor interpretó al Joker en la película The Dark Knight?","respuestas": {"a": "Heath Ledger", "b": "Joaquin Phoenix", "correcta": "a"}},
        400: {"pregunta": "¿En qué año se estrenó la película El Padrino?", "respuestas": {"a": "1972", "b": "1989", "correcta": "a"}}
    }}


def draw_window(points2):
    WIN.fill(WHITE)
    
    # Dibuja los títulos en sus posiciones
    font = pygame.font.SysFont(None, 30)
    for i, title in enumerate(titles):
        text = font.render(title, True, BLUE)
        text_rect = text.get_rect(center=(title_positions[i] + SQUARE_SIZE[0] / 2, TOP_MARGIN / 2))
        WIN.blit(text, text_rect)
    
    # Dibuja los rectángulos y los valores de puntos
    font = pygame.font.SysFont(None, 30)
    for row in range(4):
        for col in range(4):
            x = (WIDTH - (SQUARE_SIZE[0] + MARGIN) * 4) / 2 + col * (SQUARE_SIZE[0] + MARGIN)
            y = TOP_MARGIN + row * (SQUARE_SIZE[1] + MARGIN)
            rect = pygame.draw.rect(WIN, BLUE, (x, y, SQUARE_SIZE[0], SQUARE_SIZE[1]))
            text = font.render(str(points[row][col]), True, WHITE)
            text_rect = text.get_rect(center=(x + SQUARE_SIZE[0] / 2, y + SQUARE_SIZE[1] / 2))
            WIN.blit(text, text_rect)
            if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                points2 += 1
    
    # Dibuja los puntos en la esquina superior derecha
    text = font.render("Points: {}".format(points2), True, BLACK)
    text_rect = text.get_rect(topright=(WIDTH - 10, 10))
    WIN.blit(text, text_rect)
    
    pygame.display.update()



def main():
    pygame.font.init()
    clock = pygame.time.Clock()
    run = True
    points2 = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(points2)

    pygame.quit()

if __name__ == "__main__":
    main()

    #update2