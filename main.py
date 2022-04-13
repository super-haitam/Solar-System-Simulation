from get_planets import get_planets_dict, planets_order
import pygame
import math
pygame.init()

# Screen
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 190)

# FPS
clock = pygame.time.Clock()

# Vars
planets_colors = {"SUN": (210, 210, 0),
                  "MERCURY": (200, 131, 0),
                  "VENUS": (251, 131, 0),
                  "EARTH": (0, 200, 255),
                  "MARS": (173, 150, 0)}


# Class
class Planet:
    def __init__(self, name, sun_distance, diameter, vel):
        self.name = name
        self.sun_distance = sun_distance * 1.5
        self.diameter = int(diameter / 2000)
        self.vel = vel

        self.x, self.y = WIDTH / 2 + self.sun_distance, HEIGHT / 2
        self.color = planets_colors[self.name]

        self.angle = 0
        self.points = [(self.x, self.y)]

    def implement_angle(self, amount):
        self.angle += amount
        self.x = WIDTH / 2 + math.cos(self.angle) * self.sun_distance
        self.y = HEIGHT / 2 + math.sin(self.angle) * self.sun_distance
        self.points.append((self.x, self.y))

    def draw(self):
        pygame.draw.lines(screen, self.color, False, self.points)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.diameter)

        font = pygame.font.SysFont("comicsans", 10)
        txt = font.render(self.name, True, WHITE)
        screen.blit(txt, (self.x - txt.get_width()/2, self.y - txt.get_height()/2))


# Functions
def draw_screen():
    screen.fill(DARK_BLUE)

    for planet in all_planets:
        planet.implement_angle(-1 * planet.vel/1000)
        planet.draw()

    pygame.display.flip()


# Planets list ["Distance from Sun", "Diameter", "Orbital Velocity"]
all_planets = [Planet("SUN", 0, 139000, 0)]
planets = get_planets_dict()
for num, planet_str in enumerate(planets):
    if planets_order[num] == planet_str:
        all_planets.append(Planet(planet_str,
                                  planets[planet_str]["Distance from Sun"],
                                  planets[planet_str]["Diameter"],
                                  planets[planet_str]["Orbital Velocity"]))
del planets

# Mainloop
running = True
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    draw_screen()
