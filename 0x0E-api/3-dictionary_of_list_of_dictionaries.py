#!/usr/bin/python3
'''pull todo list for employee and write to json file'''
import json
import requests
import sys

# { "USER_ID": [ {
#  "username": "USERNAME",
#  "task": "TASK_TITLE",
#  "completed": TASK_COMPLETED_STATUS
# },
#  {"username": "USERNAME",
#  "task": "TASK_TITLE",
#  "completed": TASK_COMPLETED_STATUS
# } ], ...

if __name__ == '__main__':

    all_users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    all_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    # write to json file
    with open('todo_all_employees.json', 'w') as f:
        jdump = {usr.get('id'): [{
            'username': usr.get('username'),
            'task': td.get('title'),
            'completed': td.get('completed')
        } for td in all_todos if usr.get('id') == td.get('userId')
        ] for usr in all_users
        }
        json.dump(jdump, f)
