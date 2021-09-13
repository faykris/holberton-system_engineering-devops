#!/usr/bin/python3
"""0. Gather data from an API - Module"""
import csv
import json
import sys
import urllib.request

if __name__ == "__main__":

    f = open('{}.csv'.format(sys.argv[1]), 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    
    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                int(sys.argv[1]))) as response:
        html2 = response.read()
    user_d = html2.decode('utf-8')
    user_dict = json.loads(user_d)
    user_id = user_dict.get('id')
    user_name = user_dict.get('username')

    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/todos') as response:
        html1 = response.read()
    data = html1.decode('utf-8')
    data_list = json.loads(data)

    row = []
    for todos in data_list:
        if todos.get('userId') == int(sys.argv[1]):
            row.append(user_id)
            row.append(user_name)
            row.append(todos.get('completed'))
            row.append(todos.get('title'))
            writer.writerow(row)
        row.clear()
    f.close()
