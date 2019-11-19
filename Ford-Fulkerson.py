import numpy as np
import pygame
import math


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
    screen_pos = np.array([center[0] * factor + car_pos[0], center[1] * factor - car_pos[1]]) / factor
    screen_pos = screen_pos.astype(int)
    return screen_pos


class Graph:
    class Node:
        class Connection:
            def __init__(self, edge, n1, n2):
                self.A = n1
                self.edge = edge
                self.B = n2
        def __init__(self):
            self.pos = np.random.uniform(-7, 7, (2))
            self.connections = []
            self.k = math.inf
            self.min_edge = None

    class Edge:
        def __init__(self,n1,n2):
            self.A = n1
            self.B = n2
            n1.connections.append(n1.Connection(self, n1, n2))
            n2.connections.append(n2.Connection(self, n2, n1))

            self.w = np.linalg.norm(n1.pos-n2.pos)


    def __init__(self, n):
        self.n = n
        self.nodes = []
        self.edges = []


        for i in range(n):
            self.nodes.append(self.Node())

        for i in range(len(self.nodes)):
            for j in range(i+1,len(self.nodes)):
                n1 = self.nodes[i]
                n2 = self.nodes[j]
                if np.linalg.norm(n1.pos-n2.pos) < 1.5:
                    self.edges.append(self.Edge(n1,n2))

    def prim(self):

        self.MST = []

        # Set of nodes
        self.S = []

        # Set of nodes
        self.V = list(self.nodes)

        self.openSet = [self.nodes[0]]
        self.closedSet = []
        self.nodes[0].k = 0

        while len(self.closedSet)<len(self.nodes):

            minScore = math.inf
            for node in self.openSet:

                if node.k < minScore:
                    minScore = node.k
                    node_A = node
            self.V.remove(node_A)
            self.closedSet.append(node_A)
            self.openSet.remove(node_A)
            self.S.append(node_A)
            if node_A.min_edge != None:
                self.MST.append(node_A.min_edge)


            for connection in node_A.connections:
                node_B = connection.B
                if node_B in self.V:
                    if connection.edge.w < node_B.k:
                        node_B.k =connection.edge.w
                        node_B.min_edge = connection.edge

                    if node_B not in self.openSet and node_B not in self.closedSet:
                        self.openSet.append(node_B)




    def draw(self):
        pygame.event.get()
        screen.fill((0, 0, 0))



        for edge in self.edges:
            pygame.draw.line(screen, gray, cartesian_to_screen(edge.A.pos), cartesian_to_screen(edge.B.pos), 1)

        for edge in self.MST:
            pygame.draw.line(screen, red, cartesian_to_screen(edge.A.pos), cartesian_to_screen(edge.B.pos), 7)

        for node in self.nodes:
            pygame.draw.circle(screen, green, cartesian_to_screen(node.pos), 3)

        pygame.display.flip()

graph = Graph(500)

graph.prim()
while True:
    graph.draw()



