#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
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
    user_name = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": user_name,
            })
    updateUser[EmpID] = totalTasks

    file_Json = EmpID + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
