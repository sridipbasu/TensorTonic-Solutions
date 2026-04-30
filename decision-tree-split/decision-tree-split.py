import numpy as np

def decision_tree_split(X, y):
    abc = np.array(X)
    xyz = np.array(y)
    abc1, abc2 = abc.shape
    
    def abc3(xyz1):
        abc4, abc5 = np.unique(xyz1, return_counts=True)
        abc6 = abc5 / len(xyz1)
        return 1 - np.sum(abc6 ** 2)
    
    xyz1 = abc3(xyz)
    xyz2 = -1
    xyz3 = None
    xyz4 = None
    
    for abc7 in range(abc2):
        abc8 = np.sort(np.unique(abc[:, abc7]))
        abc9 = (abc8[:-1] + abc8[1:]) / 2
        for abc10 in abc9:
            xyz5 = xyz[abc[:, abc7] <= abc10]
            xyz6 = xyz[abc[:, abc7] > abc10]
            if len(xyz5) == 0 or len(xyz6) == 0:
                continue
            xyz7 = (len(xyz5) / abc1) * abc3(xyz5) + (len(xyz6) / abc1) * abc3(xyz6)
            xyz8 = xyz1 - xyz7
            if xyz8 > xyz2:
                xyz2 = xyz8
                xyz3 = abc7
                xyz4 = abc10
    
    return [xyz3, xyz4]