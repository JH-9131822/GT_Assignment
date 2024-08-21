from datetime import date

class GT_UserInput:
    def GetInput_MultipleChoices_ID(choiceList, title):
        choice = GT_UserInput.GetInput_MultipleChoices(choiceList, title)
        return choice.id

    def GetInput_MultipleChoices_Name(choiceList, title):
        choice = GT_UserInput.GetInput_MultipleChoices(choiceList, title)
        return choice.name

    def GetInput_MultipleChoices(choiceList, title):
        readInput = True
        minValue = 0
        maxValue = 0
        while readInput:
            if title != "":
                print(title)    # display the title
            for status in choiceList:
                if minValue == 0:
                    minValue = status.id
                maxValue = status.id
                print("  [" + str(status.id) + "] " + status.name)

            userInput = 0   # define the initial value as integer
            try:
                userInput = int(input("Enter your choice: "))
            except:
                pass
            finally:
                if userInput >= minValue and userInput <= maxValue:
                    readInput = False
                else:
                    print("> Invalid choice. Please select between " + str(minValue) + " to " + str(maxValue))
                    print("")
        for status in choiceList:
            if status.id == userInput:
                return status
        return None

    def GetInput_YesNo(question):
        print(question + "  [Y] Yes  [N] No")
        userInput = input("Answer: ")
        if userInput == 'Y' or userInput == 'y':
            return True
        else:
            return False

    def GetInput_Date():
        readInput = True
        dateOfBirth = date.fromisoformat("1900-01-01")
        while readInput:
            try:
                userInput = input("Enter Date of Birth in format YYYYMMDD or YYYY-MM-DD: ")
                dateOfBirth = date.fromisoformat(userInput)
                readInput = False
            except:
                print("> Invalid date. Please enter a date in this format: YYYYMMDD or YYYY-MM-DD")
                print("")
        return dateOfBirth
