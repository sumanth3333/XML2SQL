# Importing the required libraries
import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
import xml.etree.ElementTree as Xet
import os 
import sys 



#set up database connection mysql/project/NSF
try:
    connSqlServer = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='NSF'
    )

    if connSqlServer.is_connected():
        cursor = connSqlServer.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("** Database connected ** !: ", record)
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_SCHEMA = 'NSF' AND TABLE_NAME = '{}'"
        
#-------------------------------------
#creating tables
#-------------------------------------
#Award Table 
        cursor.execute(sql.format('award'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS award (AwardTitle VARCHAR(255),AGENCY VARCHAR(255),AwardEffectiveDate VARCHAR(255),AwardExpirationDate VARCHAR(255),AwardTotalIntnAmount VARCHAR(255),AwardAmount BIGINT, AbstractNarration TEXT , MinAmdLetterDate varchar(255), MaxAmdLetterDate varchar(255),CFDA_NUM VARCHAR(255), NSF_PAR_USE_FLAG BIGINT, FUND_AGCY_CODE BIGINT, AWDG_AGCY_CODE BIGINT, FUND_OBLG VARCHAR(255), AwardID BIGINT UNIQUE PRIMARY KEY,INDEX idx_award_id (AwardID))") 
            print("Award Tables created")

#-------------------------------------
#Award Instrument table

        cursor.execute(sql.format('award_instrument'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award Instrument table already exists")
        else: 
            cursor.execute("CREATE TABLE IF NOT EXISTS award_instrument (Value VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_instrument_award_id (AwardID))")

            print("Award Instrument Tables created ") 
 
 
#-------------------------------------
#Organization table  
        cursor.execute(sql.format('organization'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Organization table already exists")
        else: 
            cursor.execute("CREATE TABLE IF NOT EXISTS organization (Code BIGINT, AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_organization_award_id (AwardID))")
            print("Organization Tables created ")           
#-------------------------------------
#Award_organization table  
        cursor.execute(sql.format('award_organization'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_organization table already exists")
        else: 
            cursor.execute("CREATE TABLE IF NOT EXISTS award_organization (Code BIGINT, AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_organization_award_id (AwardID))")
            print("Award_organization Tables created ")
#-------------------------------------
#Program_officer table 

        cursor.execute(sql.format('program_officer'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Program_officer table already exists")
        else: 
            cursor.execute("CREATE TABLE IF NOT EXISTS program_officer (SignBlockName VARCHAR(255),PO_EMAI VARCHAR(255),PO_PHON VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),INDEX idx_Program_officer_award_id (AwardID))")
            print("Program_officer Tables created ")
#-------------------------------------
        cursor.execute(sql.format('investigator'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Investigator table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS investigator (FirstName VARCHAR(255), LastName VARCHAR(255), PI_MID_INIT VARCHAR(255), PI_SUFX_NAME VARCHAR(255),PI_FULL_NAME VARCHAR(255),EmailAddress VARCHAR(255), NSF_ID BIGINT, StartDate VARCHAR(255),EndDate VARCHAR(255), RoleCode VARCHAR(255), FirstName2 VARCHAR(255), LastName2 VARCHAR(255), PI_MID_INIT2 VARCHAR(255), PI_SUFX_NAME2 VARCHAR(255),PI_FULL_NAME2 VARCHAR(255),EmailAddress2 VARCHAR(255),NSF_ID2 VARCHAR(255), StartDate2 VARCHAR(255), EndDate2 VARCHAR(255), RoleCode2 VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),INDEX idx_investigator_award_id (AwardID))")  
            print("Investigator Tables created ")

#-------------------------------------
#Institution table 
        cursor.execute(sql.format('institution'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Institution table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS institution (Name VARCHAR(255),CityName VARCHAR(255),ZipCode VARCHAR(255),PhoneNumber BIGINT,StreetAddress VARCHAR(255),StreetAddress2 VARCHAR(255), CountryName VARCHAR(255),StateName VARCHAR(255),StateCode VARCHAR(255), CONGRESSDISTRICT BIGINT,CONGRESS_DISTRICT_ORG VARCHAR(255),ORG_UEI_NUM VARCHAR(255), ORG_LGL_BUS_NAME VARCHAR(255),ORG_PRNT_UEI_NUM VARCHAR(255),AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_institution_award_id (AwardID))")  
            print("Institution Tables created ")  
#-------------------------------------
#Performance_institution table    

        cursor.execute(sql.format('performance_institution'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Performance_institution table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS performance_institution (Name VARCHAR(255),CityName VARCHAR(255),StateCode VARCHAR(255),ZipCode VARCHAR(255),StreetAddress VARCHAR(255),CountryCode VARCHAR(255),CountryName VARCHAR(255),StateName VARCHAR(255),CountryFlag VARCHAR(255),CONGRESSDISTRICT VARCHAR(255),CONGRESS_DISTRICT_PERF VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),INDEX idx_performance_institution_award_id (AwardID))")   
            print("Performance_institution Tables created ")
            
#-------------------------------------
#Program_element table
        cursor.execute(sql.format('program_element'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award Instrument table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS program_element (Code VARCHAR(255),Text VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),INDEX idx_program_element_award_id (AwardID))")
            print("Program_element Tables created ")
            
#-------------------------------------
#Program_reference table
        cursor.execute(sql.format('program_reference'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Program_reference table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS program_reference (Code VARCHAR(255),Text VARCHAR(255), AwardID BIGINT, FOREIGN KEY(AwardID) REFERENCES award(AwardID),INDEX idx_program_reference_award_id (AwardID))") 
            print("Program_reference Tables created ")
#-------------------------------------
#Appropriation table
        cursor.execute(sql.format('appropriation'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Appropriation table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS appropriation (Code VARCHAR(255), Name VARCHAR(255), APP_SYMB_ID BIGINT, AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_appropriation_award_id (AwardID))")
            print("Appropriation Tables created ")
#-------------------------------------
#Fund table
        cursor.execute(sql.format('fund'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Fund table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS fund (Code VARCHAR(255), Name VARCHAR(225), FUND_SYMB_ID VARCHAR(255), AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_fund_award_id (AwardID))") 
            print("Fund Tables created ")

#-------------------------------------
#Division table  
        cursor.execute(sql.format('division'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Division table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS division (Abbreviation VARCHAR(255), LongName VARCHAR(255), AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_division_award_id (AwardID))")
            print("Division Tables created")
                 
  
  
#-------------------------------------
#Directorate table 
        cursor.execute(sql.format('directorate'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Directorate table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS directorate (Abbreviation VARCHAR(255), LongName VARCHAR(255), AwardID BIGINT,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_directorate_award_id (AwardID))")
            print("Directorate Tables created ")
           
#-------------------------------------
#Award_institution table 
        cursor.execute(sql.format('award_institution'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_institution table already exists")
        else:
            cursor.execute("CREATE TABLE award_institution (AwardID BIGINT,Name VARCHAR(255),CityName VARCHAR(255), StateName VARCHAR(255), ORG_UEI_NUM VARCHAR(255), ORG_LGL_BUS_NAME VARCHAR(255), FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_institution_award_id (AwardID))")
            print("Award_institution Tables created ") 
#-------------------------------------
#Award_investigator table 
        cursor.execute(sql.format('award_investigator'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_investigator table already exists")
        else:
            #cursor.execute("CREATE TABLE IF NOT EXISTS award_investigator (AwardID BIGINT, FirstName VARCHAR(225),LastName VARCHAR(225), NSF_ID BIGINT, RoleCode VARCHAR(225), FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_investigator_award_id (AwardID))")
            cursor.execute("CREATE TABLE IF NOT EXISTS award_investigator (AwardID BIGINT, FirstName VARCHAR(255), LastName VARCHAR(255), PI_MID_INIT VARCHAR(255), PI_SUFX_NAME VARCHAR(255),PI_FULL_NAME VARCHAR(255),EmailAddress VARCHAR(255), NSF_ID BIGINT, StartDate VARCHAR(255),EndDate VARCHAR(255), RoleCode VARCHAR(255), FirstName2 VARCHAR(255), LastName2 VARCHAR(255), PI_MID_INIT2 VARCHAR(255), PI_SUFX_NAME2 VARCHAR(255),PI_FULL_NAME2 VARCHAR(255),EmailAddress2 VARCHAR(255),NSF_ID2 VARCHAR(255), StartDate2 VARCHAR(255), EndDate2 VARCHAR(255), RoleCode2 VARCHAR(255),FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_investigator_award_id (AwardID))")
            print("Award_investigator Tables created ")
#-------------------------------------
#Award_performance_institution table
        cursor.execute(sql.format('award_performance_institution'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_performance_institution table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS award_performance_institution (AwardID BIGINT, Name VARCHAR(225),CityName VARCHAR(225), StateName VARCHAR(225), FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_performance_institution_award_id (AwardID))")
            print("Award_performance_institution Tables created ")  
            
            
#-------------------------------------          
#Award_program_reference table           
        cursor.execute(sql.format('award_program_reference'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_program_reference table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS award_program_reference (AwardID BIGINT, Code VARCHAR(255),Text VARCHAR(255), FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_program_reference_award_id (AwardID))")
            print("Award_program_reference Tables created ")  
            
#-------------------------------------  
#award_program_element table
        cursor.execute(sql.format('award_program_element'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("Award_program_element table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS award_program_element (AwardID BIGINT, Code VARCHAR(224),Text VARCHAR(225), FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_award_program_element_award_id (AwardID))")
            print("Award_program_element Tables created ") 
            
#-------------------------------------  
#info
        cursor.execute(sql.format('info'))
        table_exists = cursor.fetchone()

        if table_exists:
            print("info table already exists")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS info (AwardID BIGINT, MinAmdLetterDate varchar(255),MaxAmdLetterDate varchar(255), AwardEffectiveDate VARCHAR(255), AwardExpirationDate VARCHAR(255),AwardTotalIntnAmount VARCHAR(255), AwardAmount BIGINT, AbstractNarration TEXT, First_Investigator VARCHAR(255), Second_Investigator VARCHAR(255), SignBlockName VARCHAR(255), Name VARCHAR(255) ,FOREIGN KEY(AwardID) REFERENCES award(AwardID), INDEX idx_info_award_id (AwardID))")

            
            # print("Info Tables created ")                 
#------------------------------------- 
#setting path
        xml_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
        print(xml_directory)
        path = xml_directory+'/xml/'
        xml_files = [f for f in os.listdir(path) if f.endswith('.xml')]

        if xml_files:
            # iterate through xml files and insert data into database
            for xml_file in xml_files:
                tree = Xet.parse(path + xml_file)
                root = tree.getroot()

#-------------------------------------
                for award in root.findall('Award'):
                    award_id = award.find('AwardID').text
                    award_title = award.find('AwardTitle').text
                    award_agency = award.find('AGENCY').text
                    award_effectivedate = award.find('AwardEffectiveDate').text
                    award_expirationdate = award.find('AwardExpirationDate').text
                    award_total_amount = award.find('AwardTotalIntnAmount'). text
                    award_amount = award.find('AwardAmount').text
                    award_abstract_narration = award.find('AbstractNarration').text
                    award_min_amd_ldate = award.find('MinAmdLetterDate').text
                    award_max_amd_ldate = award.find('MaxAmdLetterDate').text
                    # award_arraamount = award.find('ARRAAmount').text
                    #tran_type = award.find('TRAN_TYPE').text 
                    cfda_num = award.find('CFDA_NUM').text
                    nsf_par_use_flag = award.find('NSF_PAR_USE_FLAG').text
                    fund_agcy_code = award.find('FUND_AGCY_CODE').text
                    awdg_agcy_code = award.find('AWDG_AGCY_CODE').text
                    fund_oblg = award.find('FUND_OBLG').text
                    #trying to avoid duplicate value
                    
# Check if the award instrument already exists and works for duplicate data                    
                    
                    
                    cursor.execute("SELECT 1 FROM award USE INDEX (idx_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()

                    if result and result[0]:
                        print(f"AwardID {award_id} already exists in award table. Skipping update on table..")
                    else:
                        try:
                            cursor.execute('INSERT INTO award (AwardTitle,AGENCY,AwardEffectiveDate,AwardExpirationDate,AwardTotalIntnAmount,AwardAmount,AbstractNarration,MinAmdLetterDate,MaxAmdLetterDate,CFDA_NUM,NSF_PAR_USE_FLAG,FUND_AGCY_CODE,AWDG_AGCY_CODE,FUND_OBLG,AwardID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )', (award_title, award_agency, award_effectivedate, award_expirationdate, award_total_amount,award_amount, award_abstract_narration, award_min_amd_ldate, award_max_amd_ldate, cfda_num, nsf_par_use_flag, fund_agcy_code, awdg_agcy_code, fund_oblg, award_id)) #fund_oblg
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue 
                        
#-------------------------------------
                for award_instrument in award.findall('AwardInstrument'):
                    value = award_instrument.find('Value').text
                    award_id = award.find('AwardID').text
        
#Check if the award instrument already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM award_instrument USE INDEX (idx_award_instrument_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    
                    result = cursor.fetchone()
                    if result and result[0]:
                        print(f"AwardID {award_id} already exists in award_instrument table. Skipping update on table..")
                    else:
                        try:
                            cursor.execute('INSERT INTO award_instrument (Value, AwardID) VALUES (%s, %s)', (value, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue   
                        
#-------------------------------------                       
               
                for award_organization in award.findall('Organization'): 
                    code = award_organization.find('Code').text
                    award_id = award.find('AwardID').text
                
                    cursor.execute("SELECT 1 FROM organization USE INDEX (idx_organization_award_id) WHERE AwardID = %s Limit 1", (award_id,))                   
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in institution table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO organization (AwardID,Code ) VALUES (%s, %s)', (award_id,code))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
                                 
                       
#Check if the award organization already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM award_organization USE INDEX (idx_award_organization_award_id) LEFT JOIN organization USE INDEX (idx_organization_award_id) ON award_organization.AwardID = organization.AwardID WHERE award_organization.AwardID = %s LIMIT 1", (award_id,))
                    #cursor.execute("SELECT 1 FROM award_performance_institution USE INDEX (idx_award_performance_institution_award_id) LEFT JOIN performance_institution USE INDEX (idx_performance_institution_award_id) ON award_performance_institution.AwardID = performance_institution.AwardID WHERE award_performance_institution.AwardID = %s LIMIT 1", (award_id,))
                    
                    
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in award_organization table. Skipping update on table...")                    
                    else:
                        try:
                            cursor.execute('INSERT INTO award_organization (Code, AwardID) VALUES (%s, %s)', (code, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue                      
#-------------------------------------  
                for program_officer in award.findall('ProgramOfficer'):
                    sign_block_name = program_officer.find('SignBlockName').text
                    po_email = program_officer.find('PO_EMAI').text
                    po_phone = program_officer.find('PO_PHON').text
                    award_id = award.find('AwardID').text
        
#Check if the award program_officer already exists and works for duplicate data
                                               
                    cursor.execute("SELECT 1 FROM program_officer USE INDEX (idx_Program_officer_award_id) WHERE AwardID = %s LIMIT 1", (award_id, ))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in program_officer table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO program_officer (SignBlockName, PO_EMAI, PO_PHON, AwardID) VALUES (%s, %s,%s, %s)', (sign_block_name,po_email,po_phone, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue

#------------------------------------- 
                for investigator, investigator2 in zip(award.findall('Investigator'), award.findall('Investigator')[1:] + [None]):
                    fname = investigator.find('FirstName').text
                    lname = investigator.find('LastName').text
                    pi_mid_init = investigator.find('PI_MID_INIT').text
                    pi_sufx = investigator.find('PI_SUFX_NAME').text
                    pi_full_name = investigator.find('PI_FULL_NAME').text
                    email = investigator.find('EmailAddress').text
                    nsf_id = investigator.find('NSF_ID').text
                    start_date = investigator.find('StartDate').text
                    end_date = investigator.find('EndDate').text
                    role_code = investigator.find('RoleCode').text
                    award_id = award.find('AwardID').text                     
                        
                    cursor.execute("SELECT 1 FROM investigator USE INDEX (idx_investigator_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in investigator table. Skipping update on table...")                      
                    else:
                        try:
                            fname2 = investigator2.find('FirstName').text
                            lname2 = investigator2.find('LastName').text
                            pi_mid_init2 = investigator2.find('PI_MID_INIT').text
                            pi_sufx2 = investigator2.find('PI_SUFX_NAME').text
                            pi_full_name2 = investigator2.find('PI_FULL_NAME').text
                            email2 = investigator2.find('EmailAddress').text
                            nsf_id2 = investigator2.find('NSF_ID').text
                            start_date2 = investigator2.find('StartDate').text
                            end_date2 = investigator2.find('EndDate').text
                            role_code2 = investigator2.find('RoleCode').text
            
            # Insert both Investigator elements into the database
                            cursor.execute('INSERT INTO investigator (FirstName,LastName,PI_MID_INIT,PI_SUFX_NAME,PI_FULL_NAME,EmailAddress,NSF_ID,StartDate,EndDate,RoleCode, FirstName2 ,LastName2 , PI_MID_INIT2 , PI_SUFX_NAME2, PI_FULL_NAME2, EmailAddress2 , NSF_ID2 , StartDate2 , EndDate2, RoleCode2, AwardID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                                       (fname, lname, pi_mid_init, pi_sufx, pi_full_name, email, nsf_id, start_date, end_date, role_code, fname2, lname2, pi_mid_init2, pi_sufx2, pi_full_name2, email2, nsf_id2, start_date2, end_date2, role_code2, award_id))
                        except AttributeError:
            
                 
            # Handle the case where there is no second Investigator element
                            cursor.execute('INSERT INTO investigator (FirstName,LastName,PI_MID_INIT,PI_SUFX_NAME,PI_FULL_NAME,EmailAddress,NSF_ID,StartDate,EndDate,RoleCode, AwardID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                           (fname, lname, pi_mid_init, pi_sufx, pi_full_name, email, nsf_id, start_date, end_date, role_code, award_id))
                       
                            continue
# Check if the award investigator already exists and works for duplicate data
                for investigator, investigator2 in zip(award.findall('Investigator'), award.findall('Investigator')[1:] + [None]):
                    fname = investigator.find('FirstName').text
                    lname = investigator.find('LastName').text
                    pi_mid_init = investigator.find('PI_MID_INIT').text
                    pi_sufx = investigator.find('PI_SUFX_NAME').text
                    pi_full_name = investigator.find('PI_FULL_NAME').text
                    email = investigator.find('EmailAddress').text
                    nsf_id = investigator.find('NSF_ID').text
                    start_date = investigator.find('StartDate').text
                    end_date = investigator.find('EndDate').text
                    role_code = investigator.find('RoleCode').text
                    award_id = award.find('AwardID').text 
                    
                    cursor.execute("SELECT 1 FROM award_investigator USE INDEX (idx_award_investigator_award_id) LEFT JOIN investigator USE INDEX (idx_investigator_award_id) ON award_investigator.AwardID = investigator.AwardID WHERE award_investigator.AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in award_investigator table. Skipping update on table...")
                    else:
                        try:
                            fname2 = investigator2.find('FirstName').text
                            lname2 = investigator2.find('LastName').text
                            pi_mid_init2 = investigator2.find('PI_MID_INIT').text
                            pi_sufx2 = investigator2.find('PI_SUFX_NAME').text
                            pi_full_name2 = investigator2.find('PI_FULL_NAME').text
                            email2 = investigator2.find('EmailAddress').text
                            nsf_id2 = investigator2.find('NSF_ID').text
                            start_date2 = investigator2.find('StartDate').text
                            end_date2 = investigator2.find('EndDate').text
                            role_code2 = investigator2.find('RoleCode').text
                                
                            cursor.execute('INSERT INTO award_investigator (AwardID,FirstName,LastName,PI_MID_INIT,PI_SUFX_NAME,PI_FULL_NAME,EmailAddress,NSF_ID,StartDate,EndDate,RoleCode, FirstName2 ,LastName2 , PI_MID_INIT2 , PI_SUFX_NAME2, PI_FULL_NAME2, EmailAddress2 , NSF_ID2 , StartDate2 , EndDate2, RoleCode2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                                       (award_id,fname, lname, pi_mid_init, pi_sufx, pi_full_name, email, nsf_id, start_date, end_date, role_code, fname2, lname2, pi_mid_init2, pi_sufx2, pi_full_name2, email2, nsf_id2, start_date2, end_date2, role_code2, ))
                        except AttributeError:
            
                 
            # Handle the case where there is no second award Investigator element
                            cursor.execute('INSERT INTO award_investigator (AwardID,FirstName,LastName,PI_MID_INIT,PI_SUFX_NAME,PI_FULL_NAME,EmailAddress,NSF_ID,StartDate,EndDate,RoleCode ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                           (award_id,fname, lname, pi_mid_init, pi_sufx, pi_full_name, email, nsf_id, start_date, end_date, role_code))
                       
                            continue
             
#------------------------------------- 

                for institution in award.findall('Institution'):
                    name = institution.find('Name').text
                    city = institution.find('CityName').text
                    zip_code = institution.find('ZipCode').text
                    phone_num = institution.find('PhoneNumber').text
                    add = institution.find('StreetAddress').text
                    add2 = institution.find('StreetAddress2').text
                    country_name = institution.find('CountryName').text
                    state_name = institution.find('StateName').text
                    state_code = institution.find('StateCode').text
                    congressdist = institution.find('CONGRESSDISTRICT').text
                    congress_dist_org = institution.find('CONGRESS_DISTRICT_ORG').text
                    org_uei = institution.find('ORG_UEI_NUM').text
                    org_lgl = institution.find('ORG_LGL_BUS_NAME').text
                    org_prnt = institution.find('ORG_PRNT_UEI_NUM').text
                    award_id = award.find('AwardID').text
                       
# Check if the  institution already exists and works for duplicate data                       
                    cursor.execute("SELECT 1 FROM institution USE INDEX (idx_institution_award_id)WHERE AwardID = %s Limit 1", (award_id,))                   
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in institution table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO institution (Name,CityName,ZipCode,PhoneNumber,StreetAddress,StreetAddress2,CountryName,StateName,StateCode,CONGRESSDISTRICT,CONGRESS_DISTRICT_ORG,ORG_UEI_NUM,ORG_LGL_BUS_NAME,ORG_PRNT_UEI_NUM,AwardID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (name,city,zip_code,phone_num,add,add2,country_name,state_name,state_code,congressdist,congress_dist_org,org_uei,org_lgl,org_prnt, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
# Check if the award award_institution already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM award_institution USE INDEX (idx_award_institution_award_id) LEFT JOIN institution USE INDEX (idx_institution_award_id) ON award_institution.AwardID = institution.AwardID WHERE award_institution.AwardID = %s LIMIT 1", (award_id,))
                    
                    result = cursor.fetchone()

                    if result:
                        print(f"AwardID {award_id} already exists in award_institution table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO award_institution (AwardID, Name, CityName, StateName, ORG_UEI_NUM, ORG_LGL_BUS_NAME) VALUES (%s, %s, %s, %s, %s, %s)', (award_id, name, city, state_name, org_uei, org_lgl ))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue                       
#-------------------------------------

                for performance_institution in award.findall('Performance_Institution'):
                    name = performance_institution.find('Name').text
                    city_name = performance_institution.find('CityName').text
                    state_code = performance_institution.find('StateCode').text
                    zip_code = performance_institution.find('ZipCode').text
                    stress_address = performance_institution.find('StreetAddress').text
                    country_code = performance_institution.find('CountryCode').text
                    country_name = performance_institution.find('CountryName').text
                    state_name = performance_institution.find('StateName').text
                    country_flag = performance_institution.find('CountryFlag').text
                    congress_district = performance_institution.find('CONGRESSDISTRICT').text
                    congress_district_perf = performance_institution.find('CONGRESS_DISTRICT_PERF').text
                    award_id = award.find('AwardID').text
                        
# Check if the award performance_institution already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM performance_institution USE INDEX (idx_performance_institution_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in performance_institution table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO performance_institution (Name, CityName, StateCode, ZipCode, StreetAddress, CountryCode, CountryName, StateName, CountryFlag, CONGRESSDISTRICT, CONGRESS_DISTRICT_PERF, AwardID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (name, city_name, state_code, zip_code, stress_address, country_code, country_name, state_name, country_flag, congress_district, congress_district_perf, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
#Check if the award award_performance_institution already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM award_performance_institution USE INDEX (idx_award_performance_institution_award_id) LEFT JOIN performance_institution USE INDEX (idx_performance_institution_award_id) ON award_performance_institution.AwardID = performance_institution.AwardID WHERE award_performance_institution.AwardID = %s LIMIT 1", (award_id,))
                    
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in award_performance_institution table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO award_performance_institution (AwardID, Name, CityName, StateName) VALUES (%s, %s, %s, %s)', (award_id,name,city_name,state_name))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
 
#-------------------------------------
                for program_element in award.findall('ProgramElement'):
                    code = program_element.find('Code').text
                    text = program_element.find('Text').text
                    award_id = award.find('AwardID').text
                           
# Check if the award program_element already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM program_element USE INDEX (idx_program_element_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in program_element table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO program_element (Code, Text, AwardID) VALUES (%s, %s, %s)', (code, text, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
                        
# Check if the award program_element already exists and works for duplicate data                       
           
                    cursor.execute("SELECT 1 FROM award_program_element USE INDEX (idx_award_program_element_award_id)  WHERE award_program_element.AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in award_program_element table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO award_program_element (AwardID, Code, Text) SELECT award.AwardID, program_element.Code, program_element.Text FROM award LEFT JOIN program_element ON program_element.AwardID = award.AwardID WHERE award.AwardID = %s', (award_id,))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue  
                    
#-------------------------------------
                for program_reference in award.findall('ProgramReference'):
                    code = program_reference.find('Code').text
                    text = program_reference.find('Text').text
                    award_id = award.find('AwardID').text
                                                  
# Check if the award program_reference already exists and works for duplicate data
                        
                    cursor.execute("SELECT 1 FROM program_reference USE INDEX (idx_program_reference_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in program_reference table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO program_reference (Code,Text, AwardID) VALUES (%s, %s, %s)', (code,text,award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue                                            
                        
# Check if the award award_program_reference already exists and works for duplicate data
                    
                        cursor.execute("SELECT 1 FROM award_program_reference USE INDEX (idx_award_program_reference_award_id) LEFT JOIN program_reference USE INDEX (idx_program_reference_award_id) ON award_program_reference.AwardID = program_reference.AwardID WHERE award_program_reference.AwardID = %s LIMIT 1", (award_id,))
                        
                        result = cursor.fetchone()
                        if result:
                            print(f"AwardID {award_id} already exists in award_program_reference table. Skipping update on table...")
                        else:
                            try:
                                cursor.execute('INSERT INTO award_program_reference (AwardID, Code,Text) VALUES (%s, %s, %s)', (award_id,code,text))
                            except mysql.connector.IntegrityError:
                                print(f"Skipping duplicate record with AwardID {award_id}")
                                continue                       
#-------------------------------------
                for appropriation in award.findall('Appropriation'):
                    code = appropriation.find('Code').text
                    name = appropriation.find('Name').text
                    app_symb = appropriation.find('APP_SYMB_ID').text
                    award_id = award.find('AwardID').text
              
                
#Check if the appropriation already exists and works for duplicate data
                    cursor.execute("SELECT 1 FROM appropriation USE INDEX (idx_appropriation_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in appropriation table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO appropriation (Code,Name,APP_SYMB_ID, AwardID) VALUES (%s, %s, %s, %s)', (code,name,app_symb,award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
#-------------------------------------                       
                                               
                for fund in award.findall('Fund'):
                    code = fund.find('Code').text
                    name = fund.find('Name').text
                    fund_symb = fund.find('FUND_SYMB_ID').text
                    award_id = award.find('AwardID').text
       
# Check if the fund already exists and works for duplicate data
                    cursor.execute("SELECT 1 FROM fund USE INDEX (idx_fund_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in fund table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO fund (Code,Name,FUND_SYMB_ID, AwardID) VALUES (%s, %s, %s, %s)', (code,name,fund_symb,award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue

#------------------------------------- 
                for organization in award.findall('Organization'):
                    #code = organization.find('Code').text
                    for division in organization.findall('Division'):
                        abbreviation = division.find('Abbreviation').text 
                        long_name = division.find('LongName').text
                        award_id = award.find('AwardID').text
             
#Check if the award - organization - division already exists and works for duplicate data
                    cursor.execute("SELECT 1 FROM division USE INDEX (idx_division_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in division table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO division (Abbreviation, LongName, AwardID) VALUES (%s, %s, %s)', (abbreviation, long_name, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
#-------------------------------------   
                for organization in award.findall('Organization'):
                    for directorate in organization.findall("Directorate"):
                        abbreviation = directorate.find('Abbreviation').text
                        long_name = directorate.find('LongName').text
                        award_id = award.find('AwardID').text
                    
#                         
# # Check if the award - organization - directorate already exists and works for duplicate data
                    cursor.execute("SELECT 1 FROM directorate USE INDEX (idx_directorate_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()
                    if result:
                        print(f"AwardID {award_id} already exists in directorate table. Skipping update on table...")
                    else:
                        try:
                            cursor.execute('INSERT INTO directorate (Abbreviation, LongName, AwardID) VALUES (%s, %s, %s)', (abbreviation, long_name, award_id))
                        except mysql.connector.IntegrityError:
                            print(f"Skipping duplicate record with AwardID {award_id}")
                            continue
#-------------------------------------                     
                    cursor.execute("SELECT 1 FROM info USE INDEX (idx_info_award_id) WHERE AwardID = %s LIMIT 1", (award_id,))
                    result = cursor.fetchone()

                    if result:
                        print(f"AwardID {award_id} already exists in info table. Skipping update on table...")
                    else:
                        cursor.execute("INSERT INTO info (AwardID, MinAmdLetterDate, MaxAmdLetterDate, AwardEffectiveDate, AwardExpirationDate, AwardTotalIntnAmount, AwardAmount, AbstractNarration, First_Investigator, Second_Investigator, SignBlockName, name) \
                        SELECT award.AwardID, award.MinAmdLetterDate, award.MinAmdLetterDate, award.AwardEffectiveDate, award.AwardExpirationDate, award.AwardTotalIntnAmount, award.AwardAmount, award.AbstractNarration, \
                        investigator.PI_FULL_NAME as First_Investigator, investigator.PI_FULL_NAME2 as Second_Investigator , program_officer.SignBlockName, institution.name\
                        FROM award \
                        JOIN investigator ON award.AwardID =investigator.AwardID \
                        JOIN program_officer ON investigator.AwardID=program_officer.AwardID \
                        JOIN institution ON program_officer.AwardID = institution.awardID\
                        WHERE award.AwardID = %s", (award_id,))
                    try:
        
                        print(f"AwardID {award_id} successfully inserted into info table.")
                    except:
        
                        print(f"Failed to insert AwardID {award_id} into info table. Rolling back transaction.")

#------------- this is server transaction commitment------------------
            connSqlServer.commit()
            print("Data inserted successfully")
        else:
            print("No xml files found in the directory")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connSqlServer.is_connected():
        cursor.close()
        connSqlServer.close()
        print("MySQL connection is closed")