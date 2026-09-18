from ultra_points_functions import *
import math

def find_distance(x1, y1, x2, y2):
    deltaX = abs(x2 - x1)
    deltaY = abs(y2 - y1)
    
    resultDirection = math.sqrt(deltaX ** 2 + deltaY ** 2)
    
    return resultDirection

def find_line_corner(x1, y1, x2, y2):
    distance = find_distance(x1, y1, x2, y2)
    deltaY = abs(y2 - y1)
    
    sinCorner = math.sin(distance / deltaY)
    cornerCount = math.asin(sinCorner)

    cornerCount = math.degrees(cornerCount)

    return cornerCount
    
if __name__ == "__main__":
    x1, y1 = most_top_point_left(letter_image)
    x2, y2 = most_bottom_point_left(letter_image)

    print(find_line_corner(x1, y1, x2, y2))
