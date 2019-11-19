"""
Author: Max Martinez Ruts
Date: September 2018
Description:

Algorithm used to generate a set of evenly spread points lying in the surface of a sphere, as generating points using a spherical
grid does not provide evenly spread points. This is used as a helper for shortest-path finding on a 3D space for searching
shortest paths around the globe, since having spread points is a requirement considering the way the shortest path algorithm was designed

"""

import math
import random
import numpy as np

def fibonacci_sphere(samples=1.,randomize=True):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    points = []
    offset = 2./samples
    increment = math.pi * (3. - math.sqrt(5.));

    for i in range(int(samples)):
        y = ((i * offset) - 1) + (offset / 2);
        r = math.sqrt(1 - pow(y,2))

        phi = ((i + rnd) % samples) * increment

        x = math.cos(phi) * r
        z = math.sin(phi) * r

        points.append(np.array([x,y,z])*400000)
    return points
