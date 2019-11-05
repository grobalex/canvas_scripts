from config import *
import os
import requests
import pprint
import getpass
import json
import cmd
import csv

###############
# Global Vars #
###############

dir_path = os.path.dirname(os.path.realpath(__file__))
canvas_url = ""
TOKEN = ""
course_id = 162
assignment_id_test = 1684

#########
# OAuth #
#########


### 
#Do OAuth and get token (valid for 1hr)

#API to get all assignemnts 
#API get all submissions 


'''for each pdf:
    upload_file_
'''

#############
# API Calls #
#############

def get_call(url):
    return requests.get(canvas_url + url, headers={'Authorization': 'token %s' % TOKEN}).json()

def post_call(url):
    return requests.get(canvas_url + url, headers={'Authorization': 'token %s' % TOKEN}).json()

def post_file(url, file):
    return requests.post(canvas_url + '/api/v1/courses/%s/assignments/%s/submissions/%s/comments/files' % (course_id, assignment_id, user_id), headers={'Authorization': 'token %s' % TOKEN}, files=files)
    
def handle_response(response):
    try:
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))    
    
####################
# Submission Calls #
####################

def get_submissions(course_id, assignment_id):
    dict_of_assignment = dict()
    list_of_user_ids = []
    assignments = get_call("/api/v1/courses/%s/assignments/%s" % (course_id, assignment_id))
    for assign in assignments:
        dict_of_submissions[assign["id"]] =  assign["name"]

    print(dict_of_assignment)
    single_assignment = input("Which Assignment? ")
    submissions = get_call("/api/v1/courses/%s/assignments/%s/submissions" % (course_id, single_assignment))
    for sub in submissions:
        list_of_user_ids.append(sub["user_id"])
        upload_file("file", single_assignment, sub["user_id"])
    

def upload_file(file_loc,assignment_id, user_id ):
    files = {'upload_file': open(file_loc,'rb')}
    #data = json.loads('{}')
    response = requests.post(canvas_url + '/api/v1/courses/%s/assignments/%s/submissions/%s/comments/files' % (course_id, assignment_id, user_id), headers={'Authorization': 'token %s' % TOKEN}, files=files)


