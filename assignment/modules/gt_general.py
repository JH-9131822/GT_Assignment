from modules.gt_database import GT_Database
from datetime import date

class GT_UserOption:
    def __init__(self, inId, inName):
        self.id = inId;
        self.name = inName;

class GT_Global:
    employmentStatusList = []
    maritalStatusList = []
    relationshipList = []

    def InitValues(db):
        GT_Global.employmentStatusList = GT_Helper.ReadOptions(db, "employment_status")
        GT_Global.maritalStatusList = GT_Helper.ReadOptions(db, "marital_status")
        GT_Global.relationshipList = GT_Helper.ReadOptions(db, "relationship")

class GT_Helper:
    def ReadTable(db, tableName, className):
        db.Connect()
        objList = []
        try:
            db.cursor.execute("SELECT * FROM " + tableName)
        except:
            pass
        finally:
            qResult = db.cursor.fetchall()
            for result in qResult:
                obj = className(result)
                objList.append(obj)
        return objList;
        db.Disconnect()

    def ReadOptions(db, tableName):
        optionList = []
        db.Connect()
        try:
            db.cursor.execute("SELECT * FROM " + tableName)
        except:
               pass
        finally:
            qResult = db.cursor.fetchall()
            for result in qResult:
#                print(str(result[0]) + ": " + result[1])
                option = GT_UserOption(result[0], result[1])
                optionList.append(option)
        db.Disconnect()
        return optionList

    def GetOptionName(optionList, optionId):
        for option in optionList:
            if option.id == optionId:
                return option.name
        return "Invalid Option ID"

    def GetOptionByID(optionList, optionId):
        for option in optionList:
            if option.id == optionId:
                return option
        return "Invalid Option ID"

    def CalculateAge(dateOfBirth):
        today = date.today()
        return today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
