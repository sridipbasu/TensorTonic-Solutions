import math

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    xyz = []
    abc = image_size / feature_size
    
    for i in range(feature_size):
        for j in range(feature_size):
            p = (j + 0.5) * abc
            q = (i + 0.5) * abc
            
            for s in scales:
                for r in aspect_ratios:
                    u = s * math.sqrt(r)
                    v = s / math.sqrt(r)
                    
                    xyz.append([p - u/2, q - v/2, p + u/2, q + v/2])
    
    return xyz