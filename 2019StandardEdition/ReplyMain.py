import pprint as pp

import pandas as pd


class Esamination:
    def __init__(self, map, constraint):
        info = map.iloc[0, 0].split()
        self.infoCustomerOffices = []
        self.map = []
        self.constraint = []
        mapsizex, mapsizey, numCustomerOffices, numReplyOffices = info[0], info[1], info[2], info[3]
        for k in range(0,len(constraint[0])):
            self.constraint.append(contraint.iloc[k, 0].split())
        for i in range(1, int(numCustomerOffices) + 1):
            self.infoCustomerOffices.append(map.iloc[i, 0].split())
        for y in range(i + 1, i + int(mapsizey) + 1):
            self.map.append(map.iloc[y, 0].split())
        pp.pprint(self.map)




if __name__ == "__main__":
    map = pd.read_csv("./Maps/0_exsample.txt", header=None)
    contraint = pd.read_csv("./Maps/constraint.txt", header=None)
    Esamination(map, contraint)
