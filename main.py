# Imports
import pygame
import sys

# We will work with Vector2 because it has some useful functions.
from pygame.math import Vector2

from random import randrange

import ctypes

# Enable High Dots Per Inch so the image displayed on the window is sharper.
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Configuration
pygame.init()
fps = 60
fps_clock = pygame.time.Clock()

# Window Size
window_dim = Vector2(800, 800)
screen = pygame.display.set_mode((int(window_dim.x), int(window_dim.y)))

# all the planets are stored here
# they will append themselves.
planets = []
