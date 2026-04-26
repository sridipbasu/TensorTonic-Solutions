def word_count_dict(sentences):
    abc = {}
    for xyz in sentences:
        for abc_xyz in xyz:
            if abc_xyz in abc:
                abc[abc_xyz] += 1
            else:
                abc[abc_xyz] = 1
    return abc