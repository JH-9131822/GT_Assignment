import requests
import json
from fastapi.encoders import jsonable_encoder
from datetime import date
from modules.gt_general import GT_UserOption
from modules.gt_userinput import GT_UserInput

def Test_PostApplicants():
    print("-----------------------")
    print("Testing Post Applicants")
    print("-----------------------")
    url = "http://localhost:8000/api/applicants/"
    fm1 = {"firstName" : "Jessica", "lastName" : "Lim", "dateOfBirth" : "1987-03-09", "relationshipId" : "6"}
    fm2 = {"firstName" : "Micky", "lastName" : "Chan", "dateOfBirth" : "2010-04-30", "relationshipId" : "4"}
    fm3 = {"firstName" : "Lucas", "lastName" : "Chan", "dateOfBirth" : "2013-12-13", "relationshipId" : "4"}

    applicant = {"firstName" : "Leonard", 
                 "lastName" : "Chan",
                 "dateOfBirth" : "1975-06-21", 
                 "employmentStatusId" : 2, 
                 "maritalStatusId" : 2,
                 "familyMember" : [fm1, fm2, fm3]}
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.post(url, data=json.dumps(applicant, default=str), headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")

def Test_GetApplicants():
    print("----------------------")
    print("Testing Get Applicants")
    print("----------------------")
    url = "http://localhost:8000/api/applicants/"
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.get(url, headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")

def Test_GetApplications():
    print("------------------------")
    print("Testing Get Applications")
    print("------------------------")
    url = "http://localhost:8000/api/applications/"
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.get(url, headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")
    
def Test_GetSchemes():
    print("-------------------")
    print("Testing Get Schemes")
    print("-------------------")
    url = "http://localhost:8000/api/schemes/"
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.get(url, headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")

def Test_GetEligibleSchemes(applicantId):
    print("----------------------------")
    print("Testing Get Eligible Schemes")
    print("----------------------------")
    url = "http://localhost:8000/api/schemes/eligible/"
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.get(url, params={"applicantId" : applicantId}, headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")

def Test_PostApplication():
    print("------------------------")
    print("Testing Post Application")
    print("------------------------")
    application = {"applicantId" : 17,
                   "schemeIds" : [1,3,6]}
    url = "http://localhost:8000/api/applications/"
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.post(url, data=json.dumps(application, default=str), headers=headers)
    print("Response Text: " + response.text)
    print("Response Status Code: " + str(response.status_code))
    print("Test Completed")
    print("--------------")
    print("")

print("----------------------------------------")
print("    GovTech Assignment (API Test)")
print("========================================")
print("")

mainMenuList = [GT_UserOption(1, "Get All Applicants"), 
                GT_UserOption(2, "Post New Applicant"), 
                GT_UserOption(3, "Get All Schemes"),
                GT_UserOption(4, "Get Eligible Schemes for Applicant ID = 1"),
                GT_UserOption(5, "Get All Applications"),
                GT_UserOption(6, "Post New Application"),
                GT_UserOption(7, "Exit")]

mainLoop = True
while mainLoop:
    userInput = GT_UserInput.GetInput_MultipleChoices_ID(mainMenuList, "Select a test to run:")
    print("")

    if userInput == 1:
        Test_GetApplicants()

    elif userInput == 2:
        Test_PostApplicants()

    elif userInput == 3:
        Test_GetSchemes()

    elif userInput == 4:
        Test_GetEligibleSchemes(1)

    elif userInput == 5:
        Test_GetApplications()

    elif userInput == 6:
        Test_PostApplication()

    elif userInput == 7:
        mainLoop = False
        exit()

    

