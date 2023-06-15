# Version 0.2
# Implementation using function for number checking

import csv
import re

filename = '/Users/reuben/Development/Python/Contacts Fix/contacts-2.csv'

# match_all_numbers = "[\(?\+\)?^0-9]"

# Match  string 10 digits long not starting with 0
is_us_number = "^[1-9]{10}"
# Match string 11 digits long starting with 07
is_uk_mobile_number = "07\d{9}"
# Match string 11 digits long starting with 09
is_ph_number = "09\d{9}"

# Accept phone number as argument and run phone number detection on it
def numbercheck(mobile_number):
    if mobile_number:
        # Replace ()- and spaces with no space
        phone_number = mobile_number.replace('(','').replace(')','').replace(' ','').replace('-','')
        
        # Run US number regex pattern
        if re.match(is_us_number, phone_number):
            #print(f'{phone_number} is probably US number.')
            # Append US country code to left of string and print result
            full_phone_number = "+1" + phone_number
            #print(f'Updated phone number is {full_phone_number}.')
            return full_phone_number
        
        elif re.match(is_uk_mobile_number, phone_number):
            #print(f'{phone_number} is probably UK mobile number.')
            full_phone_number = "+44" + phone_number[1:]
            #print(f'Updated phone number is {full_phone_number}.')
            return full_phone_number
        
        elif re.match(is_ph_number, phone_number):
            #print(f'{phone_number} is probably PH number.')
            full_phone_number = "+63" + phone_number[1:]
            #print(f'Updated phone number is {full_phone_number}.')
            return full_phone_number
        else:
            return "Number not valid"
    
with open(filename, 'r') as csvfile:
    contactsreader = csv.DictReader(csvfile)

    line_count = 0

    for row in contactsreader:
        print(numbercheck(row["Mobile Phone"]))
        line_count += 1
    
    print(line_count)