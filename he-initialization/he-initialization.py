import math

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    
    abc = math.sqrt(6 / fan_in)
    xyz = []
    
    for mno in W:
        pqr = []
        
        for stu in mno:
            pqr.append(stu * 2 * abc - abc)
        
        xyz.append(pqr)
    
    return xyz