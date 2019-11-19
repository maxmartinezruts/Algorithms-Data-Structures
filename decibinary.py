import numpy as np
import pygame
import math
import time


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
gray = (130,130,130)
fpsClock = pygame.time.Clock()
fps = 400

# Convert coordinates form cartesian to screen  (used to draw in pygame screen)
def cartesian_to_screen(car_pos):
    factor = 0.02
    screen_pos = np.array([center[0] * factor + car_pos[0], center[1] * factor - car_pos[1]*3.5]) / factor
    screen_pos = screen_pos.astype(int)
    return screen_pos


class Graph:
    class Node:
        def __init__(self, pos):
            self.pos = pos
            self.connections = []
            self.anticonnections = []
            self.k = math.inf
            self.min_edge = None
            self.parent = None

    class Edge:
        def __init__(self,n1,n2):
            self.A = n1
            self.B = n2
            n1.connections.append(self)
            n2.connections.append(self)
            self.capacity = (7 -self.A.pos[0])**1.3
            self.flow = 0
            self.residual = self.capacity-self.flow

            # self.w = np.linalg.norm(n1.pos-n2.pos)


    def __init__(self, n):
        self.n = n
        self.nodes = []
        self.edges = []
        self.p = None

        xs = np.random.uniform(-7,7,n)
        xs = -xs**2/3.5+7

        ys = np.random.uniform(-2,2,n)
        xs = np.sort(xs)


        for i in range(n):
            self.nodes.append(self.Node(np.array([xs[i],ys[i]])))

        for i in range(len(self.nodes)):
            for j in range(0,len(self.nodes)):
                n1 = self.nodes[i]
                n2 = self.nodes[j]
                if np.linalg.norm(n1.pos-n2.pos) < 2:
                    self.edges.append(self.Edge(n1,n2))

        self.s = self.nodes[10]
        self.t = self.nodes[90]

    def FF(self):
        while True:
            p = self.BFS()

            if p != None:

                self.augment(p)
            else:
                break
            self.draw()
            time.sleep(0.1)

    def BFS(self):
        s = self.s
        t = self.t
        self.openSet = [s]
        self.closedSet = []
        while len(self.openSet)>0:
            node_A = self.openSet[0]
            print(len(self.openSet))
            if node_A == t:
                node = node_A
                path = []
                while node != s:
                    path.append(node.parent)
                    node=node.parent.A

                return path[::-1]
            self.closedSet.append(node_A)
            self.openSet.remove(node_A)

            for edge in node_A.connections + node_A.anticonnections:
                if edge.residual > 0.00001:
                    node_B = edge.B
                    if node_B not in self.openSet and node_B not in self.closedSet:
                        self.openSet.append(node_B)
                        node_B.parent = edge


        return None

    def augment(self,p):
        min_residual = math.inf

        for edge in p:
            if edge.residual < min_residual:
                min_residual = edge.residual
        for edge in p:
            edge.flow += min_residual
            edge.residual -= min_residual
        return

    def draw(self):
        pygame.event.get()
        screen.fill((0, 0, 0))




        for edge in self.edges:
            pygame.draw.line(screen, gray, cartesian_to_screen(edge.A.pos), cartesian_to_screen(edge.B.pos), int(edge.capacity))

        for edge in self.edges:
            pygame.draw.line(screen, white, cartesian_to_screen(edge.A.pos), cartesian_to_screen(edge.B.pos), int(edge.flow))

        for node in self.nodes:
            pygame.draw.circle(screen, green, cartesian_to_screen(node.pos), 3)


        pygame.draw.circle(screen, yellow, cartesian_to_screen(self.s.pos), 10)
        pygame.draw.circle(screen, red, cartesian_to_screen(self.t.pos), 10)


        pygame.display.flip()


graph = Graph(100)
graph.FF()
while True:
    graph.draw()





G = Graph()
Gf = Graph()