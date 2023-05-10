import psutil
import pygame

# Window

width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Memory Usage")
pygame.display.init()

# Bar Color
yellow = (255, 255, 0)
green = (0, 255, 0)
# Text Color
white = (255, 255, 255)
black = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font("Roboto-Medium.ttf", 26)
fontPercentage = pygame.font.SysFont("Arial", 16)

# Showing Memory Usage

def show_memory_usage():
  mem = psutil.virtual_memory()
  width = width_screen - 2 * 20  # Dynamic.
  screen.fill(white)
  pygame.draw.rect(screen, green, (20, 50, width, 70))
  width = width * mem.percent / 100 # Making a proportional width based upon the percentual number. (The width now has a percentual value).
  pygame.draw.rect(screen, yellow, (20, 50, width, 70))
  total = round(mem.total / 1024, 2)
  text_bar = f"Memory Usage: (Total: {str(total)} KB):"  # When concatenating, one needs to convert a num type to a str type.
  text = font.render(text_bar, 1, black)
  screen.blit(text, (20, 10))
  screen.blit(
    fontPercentage.render(f"Memory Percentage: {str(mem.percent)}%.", 1, black),
    (25, 55))


def show_cpu_usage():
  capacity = psutil.cpu_percent(interval=0)
  width = width_screen - 2 * 20
  pygame.draw.rect(screen, green, (20, 250, width, 70))
  width = width * capacity / 100
  pygame.draw.rect(screen, yellow, (20, 250, width, 70))
  text = font.render("CPU Usage:", 1, black)
  screen.blit(text, (20, 210))


# Create Clock
clock = pygame.time.Clock()
count = 60

finished = False

while not finished:

  for event in pygame.event.get():
    # print(event)
    if event.type == pygame.QUIT:
      finished = True

  if count == 60:
    show_memory_usage()
    show_cpu_usage()
    count = 0

  pygame.display.update()
  clock.tick(60) # For each second, 60 frames.
  count = count + 1 # When 60, execute functions and reset count.

pygame.display.quit()

""""
import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
"""
