# Sarah Wiessler
# I pledge my honor that I have abided by the Stevens Honor System

# Skeleton code provided on canvas, author - jrr

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # input checking
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a <= 0 or b <= 0 or c <= 0:
           return 'NotATriangle' 
    except:
        return 'NotATriangle'

    # find count of each duplicate side length
    sides = [a, b, c]
    num_a = sides.count(a)
    num_b = sides.count(b)
    num_c = sides.count(c)

    # Check if right
    sides.sort()
    # sum of any two side lengths must be greater than third length
    if sides[0] + sides[1] <= sides[2]:
        return "NotATriangle"
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return 'Right'

    # Determine triangle from side count
    if num_a == 3:
        return 'Equilateral'
    elif (num_a or num_b) == 2:
        return 'Isoceles'
    elif (num_a and num_b) == 1:
        return 'Scalene'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        # Wiessler Tests
        # invalid input
        self.assertEqual(classifyTriangle("zoinks",4,5),'NotATriangle','zoinks,4,5 is NotATriangle')
        self.assertEqual(classifyTriangle(-1,4,4),'NotATriangle','-1,4,4 is NotATriangle')
        self.assertEqual(classifyTriangle(0,4,4),'NotATriangle','0,4,4 is NotATriangle')
        self.assertEqual(classifyTriangle([20],4,4),'NotATriangle','[20],4,4 is NotATriangle')
        # sides do not equal a triangle
        self.assertEqual(classifyTriangle(3,4,8),'NotATriangle','3,4,8 is NotATriangle')
        # valid input
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 is an Equilateral triangle')
        self.assertEqual(classifyTriangle(10,15,20),'Scalene','10,15,30 is a Scalene triangle')
        self.assertEqual(classifyTriangle(10.5,10.5,20),'Isoceles','10.5,10.5,30 is an Isoceles triangle')
        # large input
        self.assertEqual(classifyTriangle(300000,400000,500000),'Right','300000,400000,500000 is a Right triangle')
        


if __name__ == '__main__':
    # running classify triangle through main
    # not a triangle (sum of two sides is not greater than third) 
    runClassifyTriangle(1,2,3)
    # right triangle
    runClassifyTriangle(5, 12, 13)
    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       