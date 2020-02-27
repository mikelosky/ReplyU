import pprint as pp
import numpy as np
from heapq import heappush, heappop
import pandas as pd
import copy as cy


class Esamination:
    def __init__(self, map, justmap, constraint):
        Astars = Astar()
        info = map.iloc[0, 0].split()
        self.infoCustomerOffices = []
        self.map = []
        self.constraint = []
        self.paths = []
        self.pathxy = []

        mapsizex, mapsizey, numCustomerOffices, numReplyOffices = info[0], info[1], info[2], info[3]

        for k in range(0, len(constraint[0])):
            self.constraint.append(contraint.iloc[k, 0].split())
        for i in range(1, int(numCustomerOffices) + 1):
            self.infoCustomerOffices.append(map.iloc[i, 0].split())
        for y in range(i + 1, i + int(mapsizey) + 1):
            self.map.append(list(map.iloc[y, 0]))
        # self.map = np.array(self.map).T.tolist()
        for l in range(0, len(self.infoCustomerOffices)):
            for j in range(0, len(self.infoCustomerOffices)):
                if l != j:
                    self.prinntnm2 = [['' for i in range(1)] for j in range(int(mapsizey))]
                    start = [int(self.infoCustomerOffices[l][1]), int(self.infoCustomerOffices[l][0])]
                    goal = [int(self.infoCustomerOffices[j][1]), int(self.infoCustomerOffices[j][0])]

                    graf = Astar.createListAdjancet(Astars, self.map, int(mapsizey) - 1, int(mapsizex) - 1,
                                                    self.constraint)
                    info = Astar.Astar(Astars, tuple(start), tuple(goal), graf)
                    self.paths.append(info)
                    xy = self.convxy(info, start, goal)
                    self.pathxy.append(xy)
                    prinntnm1 = self.printonmap(self.map, xy)
                    for o in range(0, int(mapsizey)):
                        for t in range(0, int(mapsizex)):
                            self.prinntnm2[o][0] = self.prinntnm2[o][0] + prinntnm1[o][t]

                    pp.pprint(self.prinntnm2)
        #TODO:trovare il path comune
        pp.pprint(self.paths)
        pp.pprint(justmap)

    def convxy(self, info, star, goal):
        startx = star[0]
        starty = star[1]
        path = info[1]
        pathxy = []
        pathxy.append(star)
        for i in path:
            if i == 'D':
                startx = startx + 1
            if i == 'U':
                startx = startx - 1
            if i == 'R':
                starty = starty + 1
            if i == 'L':
                starty = starty - 1
            if i != ' ':
                pathxy.append([startx, starty])
        return pathxy

    def printonmap(self, map, xy):
        maph = cy.deepcopy(map)
        for k in xy:
            maph[k[0]][k[1]] = '$'
        return maph


class Astar:
    def heuristic(self, cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def Astar(self, start, goal, graph):

        pr_queue = []
        print(pr_queue)

        # implementazione un albero in cui i nodi genitori hanno un valore inferiore
        heappush(pr_queue, (0 + self.heuristic(start, goal), 0, 0, "", start))
        print(pr_queue)

        print("Start" + str(start))
        print("Goal" + str(goal))

        visited = set()
        while pr_queue:
            #TODO: Azzerare il costo per ogni percorso
            #TODO: Fare il bruteforce per vedere quali punti ti prende
            _, cost, costwalktot, path, current = heappop(pr_queue)
            if current == goal:
                info = [costwalktot, path]
                return info
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour, costwalk in graph[current]:
                heappush(pr_queue,
                         (costwalktot + self.heuristic(neighbour, goal), cost, costwalktot + costwalk,
                          path + direction, neighbour))
                # print(pr_queue)
        return None

    def createListAdjancet(self, lab, rig, col, constraint):
        M = rig
        N = col
        # M = col
        # N = rig
        graph = {(i, j): [] for i, r in enumerate(lab) for j, c in enumerate(r)}
        for i in range(0, M):
            for j in range(0, N):
                temp = lab[i][j]
                if lab[i][j] != "#":
                    for x, sublist in enumerate(constraint):
                        for y, s in enumerate(sublist):
                            if lab[i][j] in s:
                                cost = int(constraint[x][1])
                                break
                        else:
                            continue
                        break
                    if i + 1 < M:
                        if lab[i + 1][j] != "#":
                            graph[(i, j)].append(("D ", (i + 1, j), cost))
                    if i - 1 >= 0:
                        if lab[i - 1][j] != "#":
                            graph[(i, j)].append(("U ", (i - 1, j), cost))
                    if j + 1 < N:
                        if lab[i][j + 1] != "#":
                            graph[(i, j)].append(("R ", (i, j + 1), cost))
                    if j - 1 >= 0:
                        if lab[i][j - 1] != "#":
                            graph[(i, j)].append(("L ", (i, j - 1), cost))
        return graph


if __name__ == "__main__":
    map = pd.read_csv("./Maps/0_exsample.txt", header=None)
    justmap = pd.read_csv("./Maps/exsamplejustmap.txt", header=None)
    contraint = pd.read_csv("./Maps/constraint.txt", header=None)
    Esamination(map, justmap, contraint)
