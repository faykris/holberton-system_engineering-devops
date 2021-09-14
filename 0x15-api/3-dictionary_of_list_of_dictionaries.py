#!/usr/bin/python3
"""3. Dictionary of list of dictionaries - module"""
import json
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users') as response:
        html2 = response.read()
    user_d = html2.decode('utf-8')
    user_list = json.loads(user_d)

    with urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/todos') as response:
        html1 = response.read()
    todos_d = html1.decode('utf-8')
    todos_list = json.loads(todos_d)

    j_dict = {}
    j_list = []
    e_dict = {}
    for user in user_list:
        for todos in todos_list:
            if todos.get('userId') == user.get('id'):
                e_dict['username'] = user.get('username')
                e_dict['task'] = todos.get('title')
                e_dict['completed'] = todos.get('completed')
                j_list.append(dict(e_dict))
        j_dict[user.get('id')] = list(j_list)
        j_list.clear()

    j_object = json.dumps(j_dict)
    with open("todo_all_employees.json", "w") as outfile:
        outfile.write(j_object)
