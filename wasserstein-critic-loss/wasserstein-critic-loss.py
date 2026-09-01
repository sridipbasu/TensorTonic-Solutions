import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    abc = np.mean(fake_scores)
    xyz = np.mean(real_scores)
    return float(abc - xyz)