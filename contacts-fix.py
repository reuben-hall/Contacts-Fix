import csv
import re

filename = '/Users/reuben/Development/Python/Contacts Fix/contacts-2.csv'

# match_all_numbers = "[\(?\+\)?^0-9]"
is_us_number = "^[1-9]{10}"
is_uk_number = "07\d{9}"
is_ph_number = "09\d{9}"
# chars = "()- "


with open(filename, 'r') as csvfile:
    contactsreader = csv.DictReader(csvfile)

    line_count = 0

    for row in contactsreader:

        test_char = row["Mobile Phone"]

        if test_char:
            match test_char[0]:
                case "+":
                    # International number
                    pass
                    # print(test_char.replace('-','').replace(' ',''))
                case "(":
                    # Local US Number
                    pass
                    # print(test_char.replace('(','').replace(')','').replace(' ','').replace('-',''))
                case _:
                    test_char = test_char.replace('(','').replace(')','').replace(' ','').replace('-','')
                    # print(test_char)
                    if re.match(is_us_number, test_char):
                        print(f'{test_char} is probably US number.')
                    elif re.match(is_uk_number, test_char):
                        print(f'{test_char} is probably a UK number.')
                    elif re.match(is_ph_number, test_char):
                        print(f'{test_char} is probably a PH number.')
            
            
            
        # line_count += 1
        
    print(f'Processed {line_count} lines.')