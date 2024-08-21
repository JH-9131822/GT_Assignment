from modules.gt_database import GT_Database
from modules.gt_userinput import GT_UserInput
from modules.gt_general import GT_UserOption, GT_Helper

class GT_Criteria:
    def __init__(self, data):
        self.criteriaId = data[0]
        self.name = data[1] if data[1] is not None else ""
        self.description = data[2] if data[2] is not None else ""
        self.useCustomFunction = data[3] if data[3] is not None else 0
        self.customFunctionName = data[4] if data[4] is not None else ""
        self.variableName = data[5] if data[5] is not None else ""
        self.operation = data[6] if data[6] is not None else 0
        self.value = data[7] if data[7] is not None else 0

    def ShowData(self):
        print("")
        print("Criteria ID: " + str(self.criteriaId))
        print("Name: " + self.name)
        print("Description: " + self.description)
        if self.useCustomFunction == 1:
            print("Custom Function Name: " + self.customFunctionName)
        else:
            print("Target Column: " + self.variableName)
            print("Checking Operator: " + str(self.operation))
            print("Value: " + str(self.value))
        print("")

    def Display(self):
         print(" - Criteria '" + self.name + "': " + self.description)

    def HasPrimaryStudentChildren(self, applicant):
        return self.HasFamilyMemberWithinAgeRange(applicant, 7, 12)

    def HasSecondaryStudentChildren(self, applicant):
        return self.HasFamilyMemberWithinAgeRange(applicant, 13, 16)

    def HasFamilyMemberWithinAgeRange(self, applicant, minAge, maxAge):
        if applicant.familyMemberList is not None:
            for familyMember in applicant.familyMemberList:
                if (familyMember):
                    age = GT_Helper.CalculateAge(familyMember.dateOfBirth)
                    if age >= minAge and age <= maxAge:
                        return True
        return False

    def ApplicantAge(self, applicant):
        age = GT_Helper.CalculateAge(applicant.dateOfBirth)
        if self.operation == 0:      # equal
            return age == self.value
        elif self.operation == 1:    # equal / more than
            return age >= self.value
        elif self.operation == 2:    # equal / less than
            return age <= self.value
        else:
            return False

    def CheckEligibility(self, applicant):
        if self.useCustomFunction == 0:
            status = getattr(applicant, self.variableName)
            if self.operation == 0:      # equal
                return status == self.value
            elif self.operation == 1:    # equal / more than
                return status >= self.value
            elif self.operation == 2:    # equal / less than
                return status <= self.value
            else:
                return False
        else:
            try:
                checker = getattr(self, self.customFunctionName)
            except AttributeError:
                raise NotImplementedError("Class `{}` does not implement `{}`".format(self.__class__.__name__, self.customFunctionName))
            finally:
                return checker(applicant)

