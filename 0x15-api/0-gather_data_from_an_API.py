#!/usr/bin/python3
"""0. Gather data from an API - Module"""
import sys
import urllib.request
import json

with urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos') as response:
    html1 = response.read()
data = html1.decode('utf-8')
data_list = json.loads(data)

completed = 0
total = 0
name = ''

for element in data_list:
    if element['completed'] == True and element['userId'] == int(sys.argv[1]):
        completed += 1
    if element['userId'] == int(sys.argv[1]):    
        total += 1

with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'
        .format(sys.argv[1])) as response:
   html2 = response.read()
user = html2.decode('utf-8')
user_dict = json.loads(user)
name = user_dict['name']

print("Employee {} is done with tasks({}/{}):".format(name, completed, total))    
for element in data_list:
    if element['completed'] == True and element['userId'] == int(sys.argv[1]):
        print("\t {}".format(element['title']))
