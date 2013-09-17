import math

def convexHull(points):
    lowest = points[0]
    for point in points:
        if (point[1] < lowest[1]) or (point[1] == lowest[1] and point[0] < lowest[0]):
            lowest = point
    points.remove(lowest)
    def angle(point):
        return math.atan2(point[0]-lowest[0], point[1]-lowest[1])
    points.sort(key=angle, reverse=True)

    

    return points

points = [(1, 1), (1, 5), (3, 4), (-1, 2)]
convexHull(points)

'''

a_file = open('B-sample.in')
numcases = int(a_file.readline())
print numcases

for i in range(numcases):
    
    numbeats = int(a_file.readline())
    beats = [int(x) for x in a_file.readline().split()]
    
    
    print("Case #" + str(i + 1) + ": " + "")
'''
