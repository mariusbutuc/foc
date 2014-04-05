import math

def regular_polygon_area(number_of_sides, side_length):
  """
  Calculate the area of a regular polygon
  """

  dividend = 1.0/4 * number_of_sides * side_length ** 2
  divisor = math.tan(math.pi / number_of_sides)

  return dividend / divisor

print "The area of a regular polygon with 7 sides each of length 3 is " + str(regular_polygon_area(7, 3))

# test
# print regular_polygon_area(5, 7)
