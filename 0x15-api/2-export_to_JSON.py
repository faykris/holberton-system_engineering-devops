#!/usr/bin/python3
"""0. Gather data from an API - Module"""
import json
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                int(sys.argv[1]))) as response:
        html2 = response.read()
    user_d = html2.decode('utf-8')
    user_dict = json.loads(user_d)

    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/todos') as response:
        html1 = response.read()
    data = html1.decode('utf-8')
    data_list = json.loads(data)

    j_dict = {}
    j_list = []
    e_dict = {}
    for todos in data_list:
        if todos.get('userId') == int(sys.argv[1]):
            e_dict['task'] = todos.get('title')
            e_dict['completed'] = todos.get('completed')
            e_dict['username'] = user_dict.get('username')
            j_list.append(dict(e_dict))

    j_dict[sys.argv[1]] = j_list
    j_object = json.dumps(j_dict)
    with open("{}.json".format(sys.argv[1]), "w") as outfile:
        outfile.write(j_object)
