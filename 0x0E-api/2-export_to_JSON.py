#!/usr/bin/python3
'''pull todo list for employee and write to json file'''
import json
import requests
import sys

# { "USER_ID": [{
# "task": "TASK_TITLE",
# "completed": TASK_COMPLETED_STATUS,
# "username": "USERNAME"}
# ]}

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(sys.argv[1])
                           ).json()
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(sys.argv[1])
        ).json()

        print('Employee {} is done with tasks({}/{}):'.format(
            usr.get("name"),
            len([x for x in todos if x.get("completed")]),
            len(todos)
        ))
        print('\n'.join('\t {}'.format(x.get("title"))
              for x in todos if x.get('completed')))

        # write to json file
        with open('{}.json'.format(sys.argv[1]), 'w') as f:
            jdump = {sys.argv[1]: [{
                'task': td.get('title'),
                'username': usr.get('username'),
                'completed': td.get('completed')
            } for td in todos]
            }
            json.dump(jdump, f)
