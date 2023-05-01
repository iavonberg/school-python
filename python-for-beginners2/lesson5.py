#Input from user
'''
name = input('What is your name?: ')
print('Hello', name)
'''

#Statistics Module
'''
import statistics

exList = [5,9,2,9,7,4,3,1,8,3]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)
'''

#Import Syntax

'''
# import statistics as s
# from statistics import mean as m, stdev as s
from statistics import *

exList = [5,9,2,9,7,4,3,1,8,3]

# print(s.mean(exList))
print(mean(exList))
print(stdev(exList))
'''

#Importing Modules
'''
import exampleModule

exampleModule.exampleFunc('Test')
'''

#try/except
'''
try:
    name = input('What is your name?: ')
    print(int(name))
    

except TypeError as t:
    print('Type error triggered')
    print('Do more things')

except NameError as n:
    print('name error triggered')

except Exception as e:
    print('any other exception')

print('code continues onward')
'''

#tuples & lists
'''
def example():
    return 15,19

a,b = example()

print(a)
print(b)

x = [6,2,3,6,8,9,4,3]

print(x)
print(x[5])
x.append(12)
print(x)
x.insert(5,7)
print(x)
x.remove(7)
print(x)
print(x.index(12))
print(x.count(3))
x.sort()
print(x)

x = ['spot', 'cam', 'jan', 'dave', 'zack']
print(x)
x.sort()
print(x)
x.reverse()
print(x)
'''

#dictionaries

gradeDict = {
    'Kelly':89,
    'David': 65,
    'Jack': 95,
    'Samantha': 78
}

print(gradeDict)
print(gradeDict['David'])
gradeDict['David'] = 56
print(gradeDict)
gradeDict['Jessy'] = 92
print(gradeDict)
del gradeDict['David']
print(gradeDict)

gradeDict = {
    'Kelly':[89,88],
    'Jack': [95,87],
    'Samantha': [78,89],
    'Jessy': [92,99]
}

print(gradeDict)

