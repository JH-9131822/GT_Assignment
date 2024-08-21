from datetime import date
from modules.gt_database import GT_Database
from modules.gt_general import GT_UserOption
from modules.gt_userinput import GT_UserInput
from modules.gt_general import GT_Helper, GT_Global


class GT_Applicant:
    def __init__(self, data):
        self.familyMemberList = []
        if len(data) == 6:
            self.applicantId = data[0]
            self.firstName = data[1] if data[1] is not None else ""
            self.lastName = data[2] if data[2] is not None else ""
            self.dateOfBirth = data[3] if data[3] is not None else date(1900,1,1)
            self.employmentStatusId = data[4] if data[4] is not None else 0
            self.maritalStatusId = data[5] if data[5] is not None else 0

    def GetApplicantForID(db, applicantId):
        db.Connect()
        sql = "SELECT * FROM applicants WHERE applicantId = " + str(applicantId)
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to select record from MySQL: {}".format(error))
        finally:
            results = db.cursor.fetchall()
            for data in results:
                applicant = GT_Applicant(data)
        
        sql = "SELECT * FROM family_members WHERE applicantId = " + str(applicantId)
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to select record from MySQL: {}".format(error))
        finally:
            results = db.cursor.fetchall()
            for data in results:
                familyMember = GT_FamilyMember(data[1], data[2], data[5], data[4])
                applicant.familyMemberList.append(familyMember)

        db.Disconnect()
        return applicant

    def NewApplicant():
        newApplicant = GT_Applicant([])
        newApplicant.firstName = input("First name: ")
        newApplicant.lastName = input("Last name: ")
        newApplicant.dateOfBirth = GT_UserInput.GetInput_Date()
        print("")
        newApplicant.employmentStatusId = GT_UserInput.GetInput_MultipleChoices_ID(GT_Global.employmentStatusList, "Employment Status:")
        print("")
        newApplicant.maritalStatusId = GT_UserInput.GetInput_MultipleChoices_ID(GT_Global.maritalStatusList, "Marital Status:")
        print("")
        newApplicant.familyMemberList = GT_ApplicantManager.GetUserInput_FamilyMembers()
        return newApplicant

    def SaveRecord(self, db):
        db.Connect()
        sql = """INSERT INTO `applicants` (`firstName`,`lastName`,`dateOfBirth`,`employmentStatusId`,`maritalStatusId`) 
                 VALUES ('{}','{}','{}','{}','{}');""".format(self.firstName, self.lastName, str(self.dateOfBirth), str(self.employmentStatusId), str(self.maritalStatusId))
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to insert record in MySQL: {}".format(error))
        finally:
            db.connection.commit()
            result = db.cursor.fetchall()
            self.applicantId = db.cursor.lastrowid
            db.Disconnect()

    def SaveFamilyMembersRecord(self, db):
        if self.familyMemberList.count != 0:
            db.Connect()
            for familyMember in self.familyMemberList:
                sql = """INSERT INTO `family_members` (`firstName`,`lastName`,`dateOfBirth`,`relationshipId`,`applicantId`) 
                         VALUES ('{}','{}','{}','{}','{}');""".format(familyMember.firstName, familyMember.lastName, str(familyMember.dateOfBirth), str(familyMember.relationshipId), str(self.applicantId))
                try:
                    db.cursor.execute(sql)
                except db.connection.Error as error:
                    print("Failed to insert family member record in MySQL: {}".format(error))
                finally:
                    db.connection.commit()
                    result = db.cursor.fetchall()
            db.Disconnect()

    def ShowSummary(self):
        print("--------------------------------")
        print("      Applicant Summary")
        print("--------------------------------")
        print("Please confirm the information is correct:")
        print("First Name: " + self.firstName)
        print("Last Name: " + self.lastName)
        print("Date of Birth: " + str(self.dateOfBirth))
        print("Employment Status: " + GT_Helper.GetOptionName(GT_Global.employmentStatusList, self.employmentStatusId))
        print("Marital Status: " + GT_Helper.GetOptionName(GT_Global.maritalStatusList, self.maritalStatusId))

        if self.familyMemberList.count != 0:
            familyMemberIndex = 0
            for familyMember in self.familyMemberList:
                print("")
                print("Family Member #" + str(familyMemberIndex+1) + ":")
                print("First Name: " + familyMember.firstName)
                print("Last Name: " + familyMember.lastName)
                print("Date of Birth: " + str(familyMember.dateOfBirth))
                print("Relationship to the main applicant: " + GT_Helper.GetOptionName(GT_Global.relationshipList, familyMember.relationshipId))
        print("================================")
        print("")
        

class GT_FamilyMember:
    def __init__(self, firstName, lastName, dob, relationshipId):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dob
        self.relationshipId = relationshipId


class GT_ApplicantManager:
    def GetAllApplicants(db):
        db.Connect()
        sql = "SELECT * FROM applicants"
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to select record from MySQL: {}".format(error))
        finally:
            result = db.cursor.fetchall()
            applicantList = []
            for data in result:
                applicant = GT_Applicant(data)
                applicantList.append(applicant)
        db.Disconnect()
        return applicantList

    def GetUserInput_FamilyMembers():
        readInput = True
        numOfFamilyMember = 0
        familyMemberList = []

        print("")
        print("Family Member Details")
        print("---------------------")
        while readInput:
            if numOfFamilyMember == 0:
                question = "Add a family member?"
            else:
                question = "Add another family member?"
            if GT_UserInput.GetInput_YesNo(question) == True:
                numOfFamilyMember += 1
                familyMember = GT_ApplicantManager.AddFamilyMember(numOfFamilyMember)
                familyMemberList.append(familyMember)
                print(">> DONE. Family Member (#" + str(numOfFamilyMember) + "): " + familyMember.firstName + ", has been added.")
                print("")
            else:
                print("")
                readInput = False
        return familyMemberList

    def AddFamilyMember(num):
        print("")
        print("Family Member #" + str(num))
        firstName = input("First name: ")
        lastName = input("Last name: ")
        dateOfBirth = GT_UserInput.GetInput_Date()
        relationshipId = GT_UserInput.GetInput_MultipleChoices_ID(GT_Global.relationshipList, "Relationship to the main applicant")
        familyMember = GT_FamilyMember(firstName, lastName, dateOfBirth, relationshipId)
        return familyMember

    def AddNewApplicant(db):
        print("--------------------------------")
        print("    New Applicant Entry Form")
        print("================================")
        newApplicant = GT_Applicant.NewApplicant()
        newApplicant.ShowSummary()

        if GT_UserInput.GetInput_YesNo("Save applicant?") == True:
            newApplicant.SaveRecord(db)
            newApplicant.SaveFamilyMembersRecord(db)
            print("> Done. The Applicant's record has been saved.")
        else:
            print("> Not saving")
        print("--------------------------------")
        print("")
        return newApplicant