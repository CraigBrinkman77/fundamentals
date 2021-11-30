x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name' : 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'

print(students[0]['last_name'])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "andres"

sports_directory['soccer'][0] = "andres"

z = [ {'x': 10, 'y': 20} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(someList):
    for dict in someList:
        text= ""
        lastKey = list(dict.keys())[-1]
        # print(lastKey, type(lastKey))
        #prints one dictionary
        for key in dict:
            text += f'{key} - {dict[key]}'
            if key != lastKey:
                text += ", "
        print(text)

iterateDictionary(students)

def iterateDictionary2(key_name, list):
    for dict in list:
            print(dict[key_name])

iterateDictionary2('first_name',students)
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for key in dict: 
        keyLen = len(dict[key])
        print(f'{keyLen} {key}')
        for i in range(keyLen):
            print(dict[key][i])

printInfo(dojo)


