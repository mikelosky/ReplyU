import pprint as pp
import numpy as np
from heapq import heappush, heappop
import pandas as pd


class Esamination:
    def __init__(self, map, justmap, constraint):
        info = map.iloc[0, 0].split()
        self.infoCustomerOffices = []
        self.map = []
        self.constraint = []
        mapsizex, mapsizey, numCustomerOffices, numReplyOffices = info[0], info[1], info[2], info[3]
        for k in range(0, len(constraint[0])):
            self.constraint.append(contraint.iloc[k, 0].split())
        for i in range(1, int(numCustomerOffices) + 1):
            self.infoCustomerOffices.append(map.iloc[i, 0].split())
        for y in range(i + 1, i + int(mapsizey) + 1):
            self.map.append(list(map.iloc[y, 0]))
        # self.map = np.array(self.map).T.tolist()
        for j in range(0, len(self.infoCustomerOffices) - 1):
            start = [int(self.infoCustomerOffices[j][1]), int(self.infoCustomerOffices[j][0])]
            goal = [int(self.infoCustomerOffices[j + 1][1]), int(self.infoCustomerOffices[j + 1][0])]

            # start = [int(self.infoCustomerOffices[j][0]), int(self.infoCustomerOffices[j][1])]
            # goal = [int(self.infoCustomerOffices[j + 1][0]), int(self.infoCustomerOffices[j + 1][1])]
            Astar(self.constraint, self.map, tuple(start), tuple(goal), int(mapsizey) - 1, int(mapsizex) - 1)
        pp.pprint(justmap)


class Astar:
    def __init__(self, constraint, map, start, goal, mapsizex, mapsizey):
        self.constraint = constraint
        self.map = map
        graf = self.createListAdjancet(map, mapsizex, mapsizey)
        print(self.Astar(start, goal, graf))

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
            _, cost, costwalktot, path, current = heappop(pr_queue)
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour, costwalk in graph[current]:
                heappush(pr_queue,
                         (cost + costwalktot + self.heuristic(neighbour, goal), cost + 1, costwalktot + costwalk,
                          path + direction, neighbour))
                # print(pr_queue)
        return None

    def createListAdjancet(self, lab, rig, col):
        M = rig
        N = col
        # M = col
        # N = rig
        graph = {(i, j): [] for i, r in enumerate(lab) for j, c in enumerate(r)}
        for i in range(0, M):
            for j in range(0, N):
                temp = lab[i][j]
                if lab[i][j] != "#":
                    for x, sublist in enumerate(self.constraint):
                        for y, s in enumerate(sublist):
                            if lab[i][j] in s:
                                cost = int(self.constraint[x][1])
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
