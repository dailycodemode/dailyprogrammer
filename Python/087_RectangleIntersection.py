# DAILY CODE MODE
# def rectIntersection(rec1, rec2):
#     x_sec = HorIntersection(rec1, rec2)
#     y_sec = VerIntersection(rec1, rec2)
#     if x_sec != False and y_sec != False:
#         return (x_sec[0], y_sec[0], x_sec[1], y_sec[1])
#     else:
#         return None
#
#
# def HorIntersection(rec1, rec2):
#     if (rec1[0] >= rec2[0] and rec1[0] <= rec2[2]):
#         return rec1[0], rec2[2]
#     elif (rec1[2] >= rec2[0] and rec1[2] <= rec2[2]):
#         return rec2[0], rec1[2]
#     else:
#         return False
#
# def VerIntersection(rec1, rec2):
#     if (rec1[1] >= rec2[1] and rec1[1] <= rec2[3]):
#         return rec1[1], rec2[3]
#     if (rec1[3] >= rec2[1] and rec1[3] <= rec2[3]):
#         return rec2[1], rec1[3]
#     else:
#         return False
#
#
# print(rectIntersection((3, 3, 10, 10), (6, 6, 12, 12)))
#
# # Answer by DEiE
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Rectangle:
#     def __init__(self, top_left, bottom_right):
#         self.top_left = top_left
#         self.bottom_right = bottom_right
#
#     def contains(self, point):
#         return point.x >= self.top_left.x and \
#                point.x <= self.bottom_right.x and \
#                point.y >= self.top_left.y and \
#                point.y <= self.bottom_right.y
#
#     def intersects(self, rectangle):
#         print(rectangle.top_left)
#         return self.contains(rectangle.top_left) or \
#                self.contains(rectangle.bottom_right) or \
#                rectangle.contains(self.top_left) or \
#                rectangle.contains(self.bottom_right)
#
#     def get_intersect(first, second):
#         if(first.intersects(second)):
#             return Rectangle(
#                 Point(
#                     max(first.top_left.x, second.top_left.x),
#                     max(first.top_left.y, second.top_left.y)),
#                 Point(
#                     min(first.bottom_right.x, second.bottom_right.x),
#                     min(first.bottom_right.y, second.bottom_right.y)
#                 ))
#
# BREAKDOWN
# A part of programming is actually figuring out how to start it up. So in this answer we have 2 classes so lets try and set one up
#
# rect1 = Rectangle((2,5), (5,2))
#
# # If we look at the methods of the rectangle object, we can see that it is referring to an object which contains some verhy similar methods. So we'll try and create a second Rectanlge and try and pass this object into the first rectangle object
# rect2 = Rectangle((1,9), (5,2))
#
# bl_intersection = rect1.intersects(rect2)
# print(bl_intersection)
# This works and it gets sent into the intersection bit where it passes each top left and bottom right into the contains method. This method coes the same thing as mine but in a much neaater way
# One thing to note about computing is how boolean's interact with each other. The easiest way to remember is that True is 1 and that False is zero so if we multiply 1 x 1 then we return 1 i.e. True
# But if we multiply any of these by zero then we get zero.
#
# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
# print(True and True and False and False)
# True
# False
# False
# False
# False
#
# When we get to the contains method, we can see that it is expecting a point. Seeing as we've passed two sets of tuples in, we'll take a step back and turn these into points and insert them into the rectangle object and hopefully this will get us a little further
#
# If we look at the methods of the rectangle object, we can see that it is referring to an object which contains some verhy similar methods. So we'll try and create a second Rectanlge and try and pass this object into the first rectangle object
# pt1a = Point(2,5)
# pt1b = Point(5,2)
# pt2a = Point(1,9)
# pt2b = Point(4,3)
# Then we see will the rectagles still be accepted
# rect1 = Rectangle(pt1a, pt1b)
# rect2 = Rectangle(pt2a, pt2b)
#
# bl_intersection = rect1.intersects(rect2)
# print(bl_intersection)
#
# The get_intersection then checks if it actually intersects which is also a clue on how the user named his objects. Once it passes this test it returns a Rectangle in the same shape as it was passed i.e. with two points inside
#
# Summary
# I really enjoyed this challenge as it feels very neat. As for whose is better, the answer is fantastic however unfortunatly it does not work. If you draw out two triangles and pass in the values correctly as we have done then it returns false.
#
