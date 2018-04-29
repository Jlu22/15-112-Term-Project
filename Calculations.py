import math

def center(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    newX = (x1 + x2) // 2
    newY = (y1 + y2) // 2
    return (newX, newY)

def calculateVerts(points, depth):
    verts = []
    numPoints = len(points)
    halfVal = numPoints//2
    firstPoint = points[0]
    midPoint = points[halfVal]
    centerPoint = center(firstPoint, midPoint)
    halfDepth = depth/2
    for index in range(numPoints): # portion into the screen
        x, y = points[index]
        cx, cy = centerPoint
        newX = (x - cx) / 200 # 200 pixels ~ 1 inch
        newY = (y - cy) / 200
        verts.append((newX, newY, -halfDepth))
    for index in range(numPoints): # portion out of screen
        x, y = points[index]
        cx, cy = centerPoint
        newX = (x - cx) / 200 # 200 pixels ~ 1 inch
        newY = (y - cy) / 200
        verts.append((newX, newY, halfDepth))
    return verts

def calculateEdges(verts):
    edges = []
    length = len(verts)
    for vert in range(length//2):
        edges.append((vert, vert + length//2))
        if vert == length//2 - 1:
            edges.append((vert, 0))
        else:
            edges.append((vert, vert + 1))
    for vert in range(length//2, length):
        if vert == length -1:
            edges.append((vert, length//2))
        else:
            edges.append((vert, vert + 1))
    return edges
    