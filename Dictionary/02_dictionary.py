'''
StudentID:    20CS061
Student Name: Tarsh Pathak
AIM: Write a Python script to merge two Python dictionaries
 '''
#Create Dictionary
mydict1 = {"fast": "In a quick manner",
           "Sam": "A coder",
           "marks": [2, 3, 4, 5],
           "anotherDict": {'Tarsh': 'Player'},
           1: 2}
# Creating a Dictionary to update the values
updateDict = {
    'Lovish': 'Friend',
    "Shubham": "Friend",
    "Divya": "Friend",
    "Sam": "A Dancer",
}
# Using update function to update and add the values to mydict1
mydict1.update(updateDict)
print(mydict1)