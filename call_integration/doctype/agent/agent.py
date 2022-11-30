# Copyright (c) 2022, Palak Padalia and contributors
# For license information, please see license.txt

import frappe
import requests

from frappe.model.document import Document

class Agent(Document):
	pass

@frappe.whitelist()

# def call():
#     a="Hello Dear"
#     return a

def new_agent(agent_name, follow_me_number):

    url = "https://api-smartflo.tatateleservices.com/v1/agent"
    payload = {
        "name": agent_name,
        "follow_me_number": follow_me_number
    }
    headers = {
        "accept": "application/json",
        "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMxMjU2MiwiaXNzIjoiaHR0cHM6XC9cL2Nsb3VkcGhvbmUudGF0YXRlbGVzZXJ2aWNlcy5jb21cL3Rva2VuXC9nZW5lcmF0ZSIsImlhdCI6MTY2NTQwMDM4MiwiZXhwIjoxOTY1NDAwMzgyLCJuYmYiOjE2NjU0MDAzODIsImp0aSI6IlRLZGJLV2tuV1lNQmcxRXUifQ.ne6SKA5wm4P_L9zFzXnCxfxCb-IzNQ9C1h6hLkT0Ozk",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

@frappe.whitelist()
    
def update_agent(agent_name, follow_me_number):
    url = "https://api-smartflo.tatateleservices.com/v1/agent/id"
    
    payload = {
        "name": agent_name,
        "follow_me_number": follow_me_number
    }

    headers = {
        "accept": "application/json",
        "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMxMjU2MiwiaXNzIjoiaHR0cHM6XC9cL2Nsb3VkcGhvbmUudGF0YXRlbGVzZXJ2aWNlcy5jb21cL3Rva2VuXC9nZW5lcmF0ZSIsImlhdCI6MTY2NTQwMDM4MiwiZXhwIjoxOTY1NDAwMzgyLCJuYmYiOjE2NjU0MDAzODIsImp0aSI6IlRLZGJLV2tuV1lNQmcxRXUifQ.ne6SKA5wm4P_L9zFzXnCxfxCb-IzNQ9C1h6hLkT0Ozk",
        "content-type": "application/json"
    }
    response = requests.put(url, json=payload, headers=headers)
    print(response.text)