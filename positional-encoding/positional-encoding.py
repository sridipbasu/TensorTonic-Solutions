import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    pos = np.arange(seq_len, dtype=float).reshape(-1, 1)
    half_dim = (d_model + 1) // 2

    i = np.arange(half_dim, dtype=float)
    div_term = np.power(base, (2 * i) / d_model)

    angles = pos / div_term

    pe = np.zeros((seq_len, d_model), dtype=float)

    pe[:, 0::2] = np.sin(angles[:, :pe[:, 0::2].shape[1]])
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])

    return pe