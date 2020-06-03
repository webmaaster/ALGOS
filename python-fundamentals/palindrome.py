

# def isPal(stringInPut):
#     newstr = ""

#     for i in range(len(stringInPut)-1, -1, -1):
#         newstr += stringInPut[i]

#         print(newstr)

#         if newstr == stringInPut:
#             return True

#         else: 
#             return False

#  print(isPal("racecar"))
#  print(isPal("potato"))



# def isPal(stringInPut):
#     for i in range(0, len(stringInPut)/2, 1):
#         if stringInPut[i] != stringInPut[len(stringInPut)-1 -i]:
#             return False

#     return True

# print(isPal("potatop"))
# print(isPal("racecare"))


# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def countdown(someNum):
#     newarr = []
#     for i in range(someNum, -1, -1):
#         newarr.append(i)

#     return newarr 

# print(countdown(5))



# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2



# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def values_greater_than_second(someList):
#     newlist =[]

#     if len(someList)<2:
#         return False

#     secondval = someList[1]

#     for i in range(0, len(someList), 1):
#         if someList[i] >secondval:
#             newlist.append(someList[i])

#         print(len(newlist))
#         return newlist

# print(values_greater_than_second([5,4,9,3,12]))


# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    newlist = []
    















