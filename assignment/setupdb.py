from modules.gt_database import GT_Database

sqlStatements = []
sqlStatements.append("""CREATE TABLE `applicants` (
  `applicantId` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `employmentStatusId` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maritalStatusId` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`applicantId`),
  UNIQUE KEY `applicantId_UNIQUE` (`applicantId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `applications` (
  `applicationId` int NOT NULL AUTO_INCREMENT,
  `applicantId` int DEFAULT NULL,
  `schemeId` int DEFAULT NULL,
  `status` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Application Submitted',
  PRIMARY KEY (`applicationId`),
  UNIQUE KEY `applicationId_UNIQUE` (`applicationId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `benefits` (
  `benefitId` int NOT NULL AUTO_INCREMENT,
  `description` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`benefitId`),
  UNIQUE KEY `benefitId_UNIQUE` (`benefitId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `criterias` (
  `criteriaId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `useCustomFunction` tinyint DEFAULT '0',
  `customFunctionName` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `variableName` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `operation` int DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`criteriaId`),
  UNIQUE KEY `criteriaId_UNIQUE` (`criteriaId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `employment_status` (
  `employmentStatusId` int NOT NULL,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`employmentStatusId`),
  UNIQUE KEY `employmentStatusId_UNIQUE` (`employmentStatusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `family_members` (
  `familyMemberId` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `relationshipId` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `applicantId` int DEFAULT NULL,
  PRIMARY KEY (`familyMemberId`),
  UNIQUE KEY `familyMemberId_UNIQUE` (`familyMemberId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `marital_status` (
  `maritalStatusId` int NOT NULL,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`maritalStatusId`),
  UNIQUE KEY `maritalStatusId_UNIQUE` (`maritalStatusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `relationship` (
  `relationshipId` int NOT NULL,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`relationshipId`),
  UNIQUE KEY `relationshipId_UNIQUE` (`relationshipId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `scheme_benefits` (
  `schemeBenefitId` int NOT NULL,
  `schemeId` int DEFAULT NULL,
  `benefitId` int DEFAULT NULL,
  PRIMARY KEY (`schemeBenefitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `scheme_criterias` (
  `schemeCriteriaId` int NOT NULL,
  `schemeId` int DEFAULT NULL,
  `criteriaId` int DEFAULT NULL,
  PRIMARY KEY (`schemeCriteriaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlStatements.append("""CREATE TABLE `schemes` (
  `schemeId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`schemeId`),
  UNIQUE KEY `schemeId_UNIQUE` (`schemeId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

sqlInsert = []
sqlInsert.append("INSERT INTO `marital_status` (`maritalStatusId`, `name`) VALUES ('1', 'Single');")
sqlInsert.append("INSERT INTO `marital_status` (`maritalStatusId`, `name`) VALUES ('2', 'Married');")
sqlInsert.append("INSERT INTO `marital_status` (`maritalStatusId`, `name`) VALUES ('3', 'Divorced')")
sqlInsert.append("INSERT INTO `marital_status` (`maritalStatusId`, `name`) VALUES ('4', 'Widowed')")
sqlInsert.append("INSERT INTO `employment_status` (`employmentStatusId`, `name`) VALUES ('1', 'Employed');")
sqlInsert.append("INSERT INTO `employment_status` (`employmentStatusId`, `name`) VALUES ('2', 'Unemployed');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('1', 'Son');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('2', 'Daughter');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('3', 'Spouse');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('4', 'Father');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('5', 'Mother');")
sqlInsert.append("INSERT INTO `relationship` (`relationshipId`, `name`) VALUES ('6', 'Guardian');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('1', 'Retrenchment Assistance Scheme', 'Financial assistance for retrenched workers');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('2', 'School Meal Vouchers', 'School meal vouchers for primary students');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('3', 'Divorcee Assistance Scheme', 'Financial assistance for dicovered workers');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('4', 'Widow Assistance Scheme', 'Financial assitance for widowed workers');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('5', 'Education Vouchers', 'Education vouchers for secondary students');")
sqlInsert.append("INSERT INTO `schemes` (`schemeId`, `name`, `description`) VALUES ('6', 'Mid-Career Assistance Scheme', 'Financial assistance for retrenched mid-career');")
sqlInsert.append("INSERT INTO `benefits` (`benefitId`, `description`) VALUES ('1', 'Additional SkillsFuture credits of $500');")
sqlInsert.append("INSERT INTO `benefits` (`benefitId`, `description`) VALUES ('2', 'Additional CDC vouchers of $100');")
sqlInsert.append("INSERT INTO `benefits` (`benefitId`, `description`) VALUES ('3', 'Daily school meal vouchers $2 per day');")
sqlInsert.append("INSERT INTO `benefits` (`benefitId`, `description`) VALUES ('4', 'Education Voucher of $100 value');")
sqlInsert.append("INSERT INTO `benefits` (`benefitId`, `description`) VALUES ('5', 'Additional SkillsFuture credits of $2000');")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('1', 'Unemployed', 'Must be unemployed', '0', '', 'employmentStatusId', '0', '2');""")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('2', 'Has Primary Student Children', 'Has children study in Primary School', '1', 'HasPrimaryStudentChildren', '0', '0', '1');""")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('3', 'Divorced', 'Must be divorced', '0', '', 'maritalStatusId', '0', '4');""")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('4', 'Widowed', 'Must be widowed', '0', '', 'maritalStatusId', '0', '3');""")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('5', 'Has Secondary Student Children', 'Has children study in Secondary School', '1', 'HasSecondaryStudentChildren', '', '0', '1');""")
sqlInsert.append("""INSERT INTO `criterias` (`criteriaId`, `name`, `description`, `useCustomFunction`, `customFunctionName`, `variableName`, `operation`, `value`) 
                    VALUES ('6', 'Mid-Career', 'Above 40 year-old', '1', 'ApplicantAge', '', '1', '40');""")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('1', '1', '1');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('2', '2', '3');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('3', '3', '2');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('4', '4', '2');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('5', '5', '4');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('6', '6', '5');")
sqlInsert.append("INSERT INTO `scheme_benefits` (`schemeBenefitId`, `schemeId`, `benefitId`) VALUES ('7', '3', '5');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('1', '1', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('2', '2', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('3', '2', '2');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('4', '3', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('5', '3', '3');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('6', '4', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('7', '4', '4');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('8', '5', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('9', '5', '5');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('10', '6', '1');")
sqlInsert.append("INSERT INTO `scheme_criterias` (`schemeCriteriaId`, `schemeId`, `criteriaId`) VALUES ('11', '6', '6');")

# ========================================
# Main Codes
# ----------------------------------------
db = GT_Database()
db.Connect()

print("Creating tables...")
for sql in sqlStatements:
    try:
        db.cursor.execute(sql)
    except:
        pass
    finally:
        pass
print("> All tables created")

print("Adding records...")
for sql in sqlInsert:
    try:
        db.cursor.execute(sql)
    except ConnectionError as error:
        print(error)
    finally:
        db.connection.commit()
        result = db.cursor.fetchall()



db.Disconnect()
print("Done")