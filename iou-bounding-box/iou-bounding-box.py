def iou(box_a, box_b):
    
    abc = max(box_a[0], box_b[0])
    xyz = max(box_a[1], box_b[1])
    pqr = min(box_a[2], box_b[2])
    mno = min(box_a[3], box_b[3])
    w = max(0, pqr - abc)
    h = max(0, mno - xyz)

    i = w * h

    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    u = area_a + area_b - i

    if u == 0:
        return 0.0

    return i / u