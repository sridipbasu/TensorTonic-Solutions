def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    
    abc = sorted(enumerate(values), key=lambda x: x[1])
    
    xyz = [0.0] * len(values)
    
    mno = 0
    
    while mno < len(abc):
        pqr = mno
        
        while pqr + 1 < len(abc) and abc[pqr + 1][1] == abc[mno][1]:
            pqr += 1
        
        stu = ((mno + 1) + (pqr + 1)) / 2.0
        
        for vwx in range(mno, pqr + 1):
            yz = abc[vwx][0]
            xyz[yz] = float(stu)
        
        mno = pqr + 1
    
    return xyz