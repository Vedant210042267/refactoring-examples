"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random
import random

# --- Configuration ---
BOID_COUNT = 50
LIMIT_X_LOW, LIMIT_X_HIGH = -450, 50.0
LIMIT_Y_LOW, LIMIT_Y_HIGH = 300.0, 600.0
VELOCITY_X_LOW, VELOCITY_X_HIGH = 0, 10.0
VELOCITY_Y_LOW, VELOCITY_Y_HIGH = -20.0, 20.0

COHESION_FACTOR = 0.01
SEPARATION_DISTANCE_SQ = 100
MATCH_SPEED_DISTANCE_SQ = 10000
MATCH_SPEED_FACTOR = 0.125

