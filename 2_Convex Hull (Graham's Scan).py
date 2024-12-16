def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def graham_scan(points):
    points.sort(key=lambda p: (p[1], p[0]))
    start = points[0]

    points = sorted(points, key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), p))

    hull = []
    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) <= 0:
            hull.pop()  
        hull.append(point)
    
    return hull

import math

points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = graham_scan(points)
print("Convex Hull:", hull)
