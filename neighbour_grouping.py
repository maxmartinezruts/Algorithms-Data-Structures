import pygame
import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt

# Screen parameters
width = 800
height = 800
center = np.array([width/2, height/2])
screen = pygame.display.set_mode((width, height))

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255,255, 0)
fpsClock = pygame.time.Clock()
fps = 400

def cartesian_to_screen(car_pos):
    factor = 0.02
    screen_pos = np.array([center[0] * factor + car_pos[0], center[1] * factor - car_pos[1]]) / factor
    screen_pos = screen_pos.astype(int)
    return screen_pos

# Convert coordinates form screen to cartesian  (used to draw in pygame screen)
def screen_to_cartesian(screen_pos):
    factor = 0.02
    car_pos = np.array([screen_pos[0] - center[0], center[1] - screen_pos[1]]) * factor
    car_pos = car_pos.astype(float)
    return car_pos

class Space:
    def __init__(self, n, m):
        start = time.time()
        self.n = n
        self.m = m
        self.points = []
        self.lines = {}
        self.projections = []

        for p in range(n):
            self.points.append(self.Point(self, p))


        self.angles = np.arange(0,math.pi, math.pi/m)

        print('-----', start-time.time())


        for angle in self.angles:
            line = self.Line(angle)
            self.lines[angle] = line
            for point in self.points:
                projection_distance = point.distance*math.cos(point.angle-angle)
                projection = self.Projection(projection_distance,point,line)
                point.projections[angle] = projection
                line.grid[int(projection_distance)].append(projection)
                self.projections.append(projection)


    class Point:
        def __init__(self, space, i):
            self.space = space
            self.pos = np.random.uniform(-7,7,(2))
            self.angle = math.atan2(self.pos[1],self.pos[0])
            self.distance = np.linalg.norm(np.array([0,0])- self.pos)
            self.projections = {}
            self.index = i


        def check_neighbours(self):
            i = 0

            for angle in self.space.angles:

                cell = int(self.projections[angle].distance)
                next_neighbours = [0]*len(self.space.points)
                c = 0
                for projection in self.space.lines[angle].grid[cell-1] + self.space.lines[angle].grid[cell] + self.space.lines[angle].grid[cell+1]:
                    if np.linalg.norm(self.pos-projection.point.pos)<0.4:
                        if i==0:

                            next_neighbours[projection.point.index] = 1

                        elif self.neighbours[projection.point.index] == 1:
                            c+=1
                            next_neighbours[projection.point.index] = 1
                i+=1
                print(c)
                self.neighbours = list(next_neighbours)

            final = []
            for p in range(len(self.neighbours)):
                if self.neighbours[p] ==1:
                    final.append(self.space.points[p])
            self.neighbours = final

    class Projection:
        def __init__(self, distance, point, line):
            self.point = point
            self.line = line
            self.distance = distance
            self.pos = np.array([math.cos(line.angle), math.sin(line.angle)])*distance




    class Line:
        def __init__(self, angle):
            self.angle =  angle
            self.p1 = 10 * np.array([math.cos(angle), math.sin(angle)])
            self.p2 = -10 * np.array([math.cos(angle), math.sin(angle)])
            self.projections = []
            self.grid = {}

            for i in range(-70,70):
                self.grid[i] = []

    def draw(self):
        pygame.event.get()
        screen.fill((0, 0, 0))

        for point in self.points:
            pygame.draw.circle(screen, red, cartesian_to_screen(point.pos), 3)

        for line in self.lines.values():
            pygame.draw.line(screen, white, cartesian_to_screen(line.p1),cartesian_to_screen(line.p2), 1)

        for p in self.projections:
            pygame.draw.circle(screen, green, cartesian_to_screen(p.pos), 3)

        for p in self.points[0].neighbours:
            pygame.draw.circle(screen, yellow, cartesian_to_screen(p.pos), 5)


        pygame.display.flip()

ns =  []
t1s = []
t2s = []
for i in range(16):
    plane = Space(2**i, 8)
    start = time.time()

    plane.points[0].check_neighbours()
    print(time.time() - start)
    ns.append(i)
    t1s.append(time.time() - start)



    start = time.time()
    p1 = plane.points[0]
    for p2 in plane.points:
        d = np.linalg.norm(p1.pos-p2.pos)
    print(time.time()-start)
    t2s.append(time.time() - start)

plt.plot(ns,t1s)
plt.plot(ns,t2s)
plt.show()

while True:
    plane.draw()
