#!/usr/bin/python3
"""
Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    EmpID = argv[1]
    tasks = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(EmpID)
    empDATA = 'https://jsonplaceholder.typicode.com/users/{}'.format(EmpID)

    employee = sessionReq.get(tasks)
    employeeName = sessionReq.get(empDATA)

    json_req = employee.json()
    emp_name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
