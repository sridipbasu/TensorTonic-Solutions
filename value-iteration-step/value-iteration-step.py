def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    n_states = len(values)
    new_values = []

    for s in range(n_states):
        best = float('-inf')  # track max over actions
        
        for a in range(len(transitions[s])):
            q = rewards[s][a]
            
            # expected future value
            future = 0.0
            for s_next in range(n_states):
                future += transitions[s][a][s_next] * values[s_next]
            
            q += gamma * future
            best = max(best, q)
        
        new_values.append(best)

    return new_values