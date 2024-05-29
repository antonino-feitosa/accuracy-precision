
import pygame, random, argparse
from pygame.locals import QUIT


SAMPLE = 100
ACTIVE = 0
INTERVAL = 30

WIDTH = 400
HEIGHT = 400

points:list[tuple[float,float]] = []
count = 0
active = 0
seed = 0

dx = 0
dy = 0
sx = 0
sy = 0

def metrics():
    if active < 2:
        return [0,0,0,0]

    x_med = 0
    y_med = 0
    for i in range(0,active):
        (x,y) = points[i]
        x_med += x
        y_med += y
    x_med = x_med / active
    y_med = y_med / active

    x_var = 0
    y_var = 0
    for i in range(0,active):
        (x,y) = points[i]
        x_var += (x - x_med)**2
        y_var += (y - y_med)**2
    x_var = x_var / (active-1)
    y_var = y_var / (active-1)

    x_med = (200 - x_med)**2
    y_med = (200 - y_med)**2

    return (x_med, y_med, x_var, y_var)


def start():
    global count
    global active
    count = 0
    active = 0
    points.clear()
    for _ in range(SAMPLE):
        x = random.gauss(200 + dx, sx)
        y = random.gauss(200 + dy, sy)
        points.append((x,y))

def update():
    global count
    global active
    count += 1
    if count >= INTERVAL and active < len(points):
        active += 1
        count = 0

def draw(screen:pygame.Surface, font:pygame.font.Font):
    white = (255,255,255)
    black = (0,0,0)

    screen.fill(white)

    half_width = int(WIDTH/2)
    half_height = int(HEIGHT/2)
    

    pygame.draw.circle(screen, black, (half_width,half_height), 50, 2)
    pygame.draw.circle(screen, black, (half_width,half_height), 100, 2)
    pygame.draw.circle(screen, black, (half_width,half_height), 150, 2)

    pygame.draw.line(screen, black, (10, half_height), (WIDTH-10, half_height))
    pygame.draw.line(screen, black, (half_width, 10), (half_width, HEIGHT - 10))

    red = (255, 0, 0)
    for i in range(0, active):
        x, y = points[i]
        pygame.draw.circle(screen, red, (x,y), 3)

    surface = font.render('50', True, black, white)
    screen.blit(surface, (half_width + 1, half_height + 51))
    surface = font.render('100', True, black)
    screen.blit(surface, (half_width + 1, half_height + 101))
    surface = font.render('150', True, black)
    screen.blit(surface, (half_width + 1, half_height + 151))

    result = metrics()

    surface = font.render(f'Bias = ({result[0]:.3f}, {result[1]:.3f})', True, black)
    screen.blit(surface, (10, HEIGHT - 60))
    surface = font.render(f'Variance = ({result[2]:.3f}, {result[3]:.3f})', True, black)
    screen.blit(surface, (10, HEIGHT - 30))



def main():
    running = True
    paused = False
    clock = pygame.time.Clock()
    pygame.init()
    text_font = pygame.font.Font(None,24)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Accuracy and Precision')
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start()
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            update()
        draw(screen, text_font)

        pygame.display.update()
        clock.tick(100)

pygame.quit()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Accuracy and Precision')
    parser.add_argument("--seed", type=int, help="seed to pseudorandom number generator", default=0)
    parser.add_argument("--dx", type=int, help="x bias increment", default=0)
    parser.add_argument("--dy", type=int, help="y bias increment", default=0)
    parser.add_argument("--sx", type=int, help="x variance increment", default=0)
    parser.add_argument("--sy", type=int, help="y variance increment", default=0)
    args = parser.parse_args()
    dx = args.dx
    dy = args.dy
    sx = args.sx
    sy = args.sy
    seed = args.seed
    random.seed(seed)
    start()
    main()









