import numpy as np

def bag_of_words_vector(tokens, vocab):
    wd_ind = {word: idx for idx, word in enumerate(vocab)}
    
    bow = np.zeros(len(vocab), dtype=int)
    
    for t in tokens:
        if t in wd_ind:
            bow[wd_ind[t]] += 1
    
    return bow