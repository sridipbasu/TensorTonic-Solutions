def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    
    abc = {xyz: mno for mno, xyz in enumerate(ordering)}
    
    return [abc[pqr] for pqr in values]