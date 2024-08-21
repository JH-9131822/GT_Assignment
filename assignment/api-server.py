from datetime import date, datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
import json
from pydantic import BaseModel
from modules.gt_database import GT_Database
from modules.gt_applicant import GT_Applicant, GT_FamilyMember, GT_ApplicantManager
from modules.gt_application import GT_Application, GT_ApplicationManager
from modules.gt_scheme import GT_SchemeManager
from modules.gt_application import GT_Application

app = FastAPI()

db = GT_Database()

class API_FamilyMember(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth : str
    relationshipId : int

class API_Applicant(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth : str
    employmentStatusId : int
    maritalStatusId : int
    familyMember: List[API_FamilyMember] = []

class API_Application(BaseModel):
    applicantId: int
    schemeIds: List[int] = []

# ===========================================================
# API Routes
@app.get("/")
async def read_root():
    return {"Message" : "Congrats! This is your first API!"}

@app.get("/api/applicants")
async def get_applicants():
    applicantList = GT_ApplicantManager.GetAllApplicants(db)
    jsonData = jsonable_encoder(applicantList)
    return JSONResponse(content=jsonData)

@app.get("/api/schemes")
async def get_schemes():
    schemeList = GT_SchemeManager.GetAllSchemes(db)
    jsonData = jsonable_encoder(schemeList)
    return JSONResponse(content=jsonData)

@app.get("/api/schemes/eligible")
async def get_eligibleSchemes(applicantId : int):
    applicant = GT_Applicant.GetApplicantForID(db, applicantId)
    eligibleSchemeList = GT_SchemeManager.GetEligibleSchemesFor(db, applicant)
    jsonData = jsonable_encoder(eligibleSchemeList)
    return JSONResponse(content=jsonData)

@app.get("/api/applications")
async def get_applications():
    applicationList = GT_ApplicationManager.GetAllApplications(db)
    jsonData = jsonable_encoder(applicationList)
    return JSONResponse(content=jsonData)

@app.post("/api/applicants")
async def post_applicants(apiApplicant : API_Applicant):
    # Save Applicant's details
    newApplicant = GT_Applicant([])
    newApplicant.firstName = apiApplicant.firstName
    newApplicant.lastName= apiApplicant.lastName
    newApplicant.dateOfBirth = datetime.strptime(apiApplicant.dateOfBirth, '%Y-%m-%d').date()
    newApplicant.employmentStatusId = apiApplicant.employmentStatusId
    newApplicant.maritalStatusId = apiApplicant.maritalStatusId
    newApplicant.SaveRecord(db)

    # Save Family Members Details
    newApplicant.familyMemberList = []
    for apiFamilyMember in apiApplicant.familyMember:
        dob = datetime.strptime(apiFamilyMember.dateOfBirth, '%Y-%m-%d').date()
        newFamilyMember = GT_FamilyMember(apiFamilyMember.firstName, apiFamilyMember.lastName, dob, apiFamilyMember.relationshipId)
        newApplicant.familyMemberList.append(newFamilyMember)
    newApplicant.SaveFamilyMembersRecord(db)
    return {"message": "Success",}

@app.post("/api/applications")
async def post_applications(apiApplication : API_Application):
    for schemeId in apiApplication.schemeIds:
        GT_Application.SubmitApplication(db, apiApplication.applicantId, schemeId)
    return {"message": "Success",}


