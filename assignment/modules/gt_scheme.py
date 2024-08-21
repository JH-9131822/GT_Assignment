from modules.gt_general import GT_Helper
from modules.gt_database import GT_Database
from modules.gt_userinput import GT_UserInput
from modules.gt_criteria import GT_Criteria

class GT_Benefit:
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1] if data[1] is not None else ""

    def Display(self):
        print(" + Benefit: " + self.name)

class GT_Scheme:
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1] if data[1] is not None else ""
        self.description = data[2]  if data[2] is not None else ""

    def GetSchemeForID(db, schemeId):
        db.Connect()
        sql = "SELECT * FROM schemes WHERE schemes.schemeId = " + str(schemeId)
        try:
            db.cursor.execute(sql)
        except db.connection.Error as error:
            print("Failed to select record from MySQL: {}".format(error))
        finally:
            results = db.cursor.fetchall()
            db.Disconnect()
            for data in results:
                scheme = GT_Scheme(data)
                return scheme

    def GetCriterias(self, db):
        sql = """   SELECT criterias.*
                    FROM schemes
                    INNER JOIN scheme_criterias
                        ON schemes.schemeId = scheme_criterias.schemeId
                    INNER JOIN criterias
                        ON scheme_criterias.criteriaId = criterias.criteriaId
                    AND schemes.schemeId = """ + str(self.id)
        db.Connect()
        self.criteriaList = []
        try:
            db.cursor.execute(sql)
        except:
            pass
        finally:
            qResult = db.cursor.fetchall()
            for result in qResult:
                self.criteriaList.append(GT_Criteria(result))
        db.Disconnect()
        return self.criteriaList

    def GetBenefits(self, db):
        sql = """   SELECT benefits.*
                    FROM schemes
                    INNER JOIN scheme_benefits
                        ON schemes.schemeId = scheme_benefits.schemeId
                    INNER JOIN benefits
                        ON scheme_benefits.benefitId = benefits.benefitId
                    AND schemes.schemeId = """ + str(self.id)
        db.Connect()
        self.benefitList = []
        try:
            db.cursor.execute(sql)
        except:
            pass
        finally:
            qResult = db.cursor.fetchall()
            for result in qResult:
                self.benefitList.append(GT_Benefit(result))
        db.Disconnect()
        return self.benefitList



class GT_SchemeManager:
    def GetAllSchemes(db):
        return GT_Helper.ReadTable(db, "schemes", GT_Scheme)

    def DisplayAllSchemes(db):
        print("---------------------------------")
        print("    List of Available Schemes")
        print("=================================")
        print("")

        schemeList = GT_Helper.ReadTable(db, "schemes", GT_Scheme)

        counter = 1
        for scheme in schemeList:
            print("[Scheme " + str(counter) + "] " + scheme.name)
            benefitList = scheme.GetBenefits(db)
            for benefit in benefitList:
                benefit.Display()
            criteriaList = scheme.GetCriterias(db)
            for criteria in criteriaList:
                criteria.Display()
            print("")
            counter += 1
        print("")

    def GetEligibleSchemesFor(db, applicant):
        schemeList = GT_Helper.ReadTable(db, "schemes", GT_Scheme)

        eligibleSchemes = []
        for scheme in schemeList:
            failed = False
            criteriaList = scheme.GetCriterias(db)
            for criteria in criteriaList:
                if criteria.CheckEligibility(applicant) == False:
                    failed = True;
                    break
            if failed == False:
                eligibleSchemes.append(scheme)
                #print("Scheme: '" + scheme.name + "': Eligible")
            else:
                pass
                #print("Scheme: '" + scheme.name + "': NOT Eligible")
        return eligibleSchemes

    


