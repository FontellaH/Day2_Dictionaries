# 1 Update Values in Dictionaries and Lists
    #1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    #2 Change the last_name of the first student from 'Jordan' to 'Bryant'
    #3 In the sports_directory, change 'Messi' to 'Andres'
    #4 Change the value 20 in z to 30


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#answer

# 1
x[1][0]=15
print(x)

# 2
students[0]['last_name'] = 'Bryant'
print(students)

# 3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# 4
z[0]['y']=30
print(z)






# 2.Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name'])
    iterateDictionary(students)






#  3 Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
    
    iterateDictionary2('first_name',students)
    iterateDictionary2('last_name',students)       






#4 Iterate Through a Dictionary with List Values


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
            print("")

dojo = {
    
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)



# output:
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





