# Imports
import pygame
import sys

# We will work with Vector2 because it has some useful functions.
from pygame.math import Vector2

from random import randrange

import ctypes

# Enable High Dots Per Inch so the image displayed on the window is sharper.
ctypes.windll.shcore.SetProcessDpiAwareness(1)