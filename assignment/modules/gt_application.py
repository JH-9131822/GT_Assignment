from modules.gt_general import GT_Helper
from modules.gt_scheme import GT_Scheme
from modules.gt_applicant import GT_Applicant

class GT_Application:
    def __init__(self, data):
        self.applicationId = data[0]
        self.applicantId = data[1] if data[1] is not None else 0
        self.schemeId = data[2] if data[2] is not None else 0
        self.status = data[3] if data[3] is not None else ""

    def SubmitApplication(db, applicantId, schemeId):
        db.Connect()
        sql = """INSERT INTO applications (`applicantId`,`schemeId`) 
                 VALUES ('{}','{}');""".format(applicantId, schemeId)
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to insert record in MySQL: {}".format(error))
        finally:
            db.connection.commit()
        db.Disconnect()

class GT_ApplicationManager:
    def GetAllApplications(db):
        db.Connect()
        sql = "SELECT * FROM applications"
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to select record from MySQL: {}".format(error))
        finally:
            result = db.cursor.fetchall()
            applicationList = []
            for data in result:
                application = GT_Application(data)
                applicationList.append(application)
        db.Disconnect()
        return applicationList

    def DisplayAllApplications(db):
        print("---------------------------------")
        print("      List of Applications")
        print("=================================")

        applicationList = GT_Helper.ReadTable(db, "applications", GT_Application)

        counter = 1
        for application in applicationList:
            scheme = GT_Scheme.GetSchemeForID(db, application.schemeId)
            applicant = GT_Applicant.GetApplicantForID(db, application.applicantId)
            print("[" + str(counter) + "] Applicant: " + applicant.firstName + " " + applicant.lastName + "   >> Scheme: " + scheme.name)
            counter += 1
        print("---------------------------------")
        print("")


