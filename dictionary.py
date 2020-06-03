# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# x[1][0] = 15

# # Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]['last_name'] = "Bryant"
# # print(students)

# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = "Andres"
# # print(sports_directory)

# # Change the value 20 in z to 30
# z[0]['y'] = 30
# print(z)


students = [
         {'nickname':  'Michael', 'last_name' : 'Jordan'},
         {'nickname' : 'John', 'last_name' : 'Rosales'},
         {'nickname' : 'Mark', 'last_name' : 'Guillen'},
         {'nickname' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(somelist):
    for studentObj in somelist:
        outputstring = ""
        for key, value in studentObj.items():
            outputstring += f"{key} - {value} "
        print(outputstring)


def iterate_dictionary2(keyname, somelist):
    for studentObj in somelist:
        if keyname in studentObj:
            print(studentObj[keyname])
        else:
            print('key doesnt exist, try another key')
            return False

# iterate_dictionary2("last_name", students)



# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB


# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dictionary):
    for key, value in some_dictionary.items():
        print(f"{len(some_dictionary[key])} {key.upper()}")
        for item in some_dictionary[key]:
            print(item)




printInfo(dojo)

# # output:

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon