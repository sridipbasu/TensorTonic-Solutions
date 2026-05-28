import math

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    
    if len(candidate) == 0:
        return 0.0
    
    abc = []
    
    for xyz in range(1, max_n + 1):
        
        mno = {}
        pqr = {}
        
        # Candidate n-grams
        for i in range(len(candidate) - xyz + 1):
            stu = tuple(candidate[i:i + xyz])
            mno[stu] = mno.get(stu, 0) + 1
        
        # Reference n-grams
        for i in range(len(reference) - xyz + 1):
            stu = tuple(reference[i:i + xyz])
            pqr[stu] = pqr.get(stu, 0) + 1
        
        ghi = 0
        jkl = sum(mno.values())
        
        for stu in mno:
            ghi += min(mno[stu], pqr.get(stu, 0))
        
        if jkl == 0:
            return 0.0
        
        vwx = ghi / jkl
        
        if vwx == 0:
            return 0.0
        
        abc.append(vwx)
    
    c_len = len(candidate)
    r_len = len(reference)
    
    if c_len >= r_len:
        bp = 1.0
    else:
        bp = math.exp(1 - r_len / c_len)
    
    yz = sum(math.log(val) for val in abc) / max_n
    
    return bp * math.exp(yz)