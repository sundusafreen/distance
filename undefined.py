'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code DIST_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            DIST_PY.py
*  Created:             02/10/2020
*  Last Modified:       02/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Import any required module/s
import math


# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):

    distance = 0

    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places
    d= math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
    distance = "{:.2f}".format(d)
    return distance


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    for i in range(1,test_cases+1):
        

    # Write the code here to take the x1, y1, x2 and y2 value
   
        x1,y1,x2,y2 = map(int, input().split())
   
    
    
    	# Once you have all 4 values, call the compute_distance function to find Euclidean distance
        print("Distance: " ,compute_distance(x1, y1, x2, y2))
