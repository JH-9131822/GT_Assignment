from datetime import date
from modules.gt_userinput import GT_UserInput
from modules.gt_general import GT_UserOption
from modules.gt_database import GT_Database
from modules.gt_scheme import GT_Scheme, GT_SchemeManager
from modules.gt_applicant import GT_Applicant, GT_ApplicantManager, GT_FamilyMember
from modules.gt_general import GT_Helper, GT_Global
from modules.gt_application import GT_Application, GT_ApplicationManager
from fastapi import FastAPI

db = GT_Database()
GT_Global.InitValues(db)

print("----------------------------------------")
print("    GovTech Assignment (Main Portal)")
print("========================================")
print("")

mainMenuList = [GT_UserOption(1, "View Available Schemes"), 
                GT_UserOption(2, "Add New Applicant"), 
                GT_UserOption(3, "View Application Status"),
                GT_UserOption(4, "Exit")]

mainLoop = True
while mainLoop:
    userInput = GT_UserInput.GetInput_MultipleChoices_ID(mainMenuList, "Main Menu")
    print("")

    if userInput == 1:
        GT_SchemeManager.DisplayAllSchemes(db)

    elif userInput == 2:
        newApplicant = GT_ApplicantManager.AddNewApplicant(db)
        if GT_UserInput.GetInput_YesNo("Show eligible schemes for this applicant?") == True:
            print("")
            eligibleSchemeList = GT_SchemeManager.GetEligibleSchemesFor(db, newApplicant)
            if len(eligibleSchemeList) != 0:
                print("================================")
                print("    List of Eligible Schemes:")
                print("--------------------------------")
                for eligibleScheme in eligibleSchemeList:
                    print(" - Scheme: " + eligibleScheme.name)
                print("--------------------------------")
                print("")
                if GT_UserInput.GetInput_YesNo("Apply for all eligible schemes?") == True:
                    for eligibleScheme in eligibleSchemeList:
                        GT_Application.SubmitApplication(db, newApplicant.applicantId, eligibleScheme.id)
                    print("> Done. Applied to all eligibles schemes")
                    print("")
            else:
                print("> No eligible schemes that the applicant can apply to.")
                print("")
        else:
            print("Done")
        print("")

    elif userInput == 3:
        GT_ApplicationManager.DisplayAllApplications(db)
        pass
        

    elif userInput == 4:
        mainLoop = False
        exit()

    else:
        pass