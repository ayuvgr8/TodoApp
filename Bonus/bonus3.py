meals = ['cheese', 'pizza', 'pasta', 'salad']

for meal in meals:
    print(meal.capitalize())

print("bye")

# While loop run as long as condition is true
# For loop runs as long as there are item in the list which is being iterated (can be iterated over string also)  for meal in 'meals':
#
# List and String are treated aa a sequences of Obj.

# Q1: How does the for-loop work?
#
# A: The for-loop executes the indented lines n-times, where n is the number of items in the list that is being iterated.
#
# Q2: What is the difference between a while loop and a for-loop?
#
# A: A while loop iterates as long as the while-condition is True. A for-loop iterates that many times as there are items in the list that is being iterated.
#
# Q3: What are some other examples when we would need to use a for-loop?
#
# A: A for-loop is generally needed when you want to perform the same manipulation on multiple objects
# (e.g., capitalizing strings of a list). Another example of when you would need to use a for-loop is if you wanted to convert a video to grayscale.
# A video is made of hundreds or thousands of image frames. You would need to use a for-loop to iterate over the video frames and apply a grayscale effect
# to each frame. Another example would be to iterate over the pages of your blog website to extract their user comments, etc.
#
# Q4: What is the difference between match-case and if-else?
#
# Match-case is usually to match a string out of a predefined number of strings (e.g., a series of commands, months of the year, etc.).
# If-else conditionals check more complex conditions. We will cover if-else conditionals later in the course. There you will understand the exact difference.