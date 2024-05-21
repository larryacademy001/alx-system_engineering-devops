#!/usr/bin/python3
'''
Get Employee Data from API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_req = requests.get('{}/users/{}'.format(REST_API, user_id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            employee_name = user_req.get('name')
            all_tasks = list(filter(lambda x: x.get('userId') == user_id, task_req))
            tasks_done = list(filter(lambda x: x.get('completed'), all_tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(tasks_done),
                    len(all_tasks)
                )
            )
            if len(tasks_done) > 0:
                for task in tasks_done:
                    print('\t {}'.format(task.get('title')))
