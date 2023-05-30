import csv
import re

filename = '/Users/reuben/Development/Python/Contacts Fix/contacts-2.csv'

match_all_numbers = "[\(?\+\)?^0-9]"
is_us_number = "^\(?\d{3}\)? ?\d{3} ?\d{4}\s"
chars = "()- "


with open(filename, 'r') as csvfile:
    contactsreader = csv.DictReader(csvfile)

    line_count = 0

    for row in contactsreader:

        test_char = row["Mobile Phone"]

        if test_char:
            match test_char[0]:
                case "+":
                    # International number
                    print(test_char.replace('-','').replace(' ',''))
                case "(":
                    # Local US Number
                    print(test_char.replace('(','').replace(')','').replace(' ','').replace('-',''))
                case _:
                    print(f'{test_char} did not match any criteria.')
            
            


        """ if (test_char):
            if (test_char[0] == "+"):
                print(f'Skipping {test_char}: starts with +.')

            elif " " in test_char:
                print(test_char.replace(" ",""))
        
        else:
            print(f'-' * 75) """
        
        line_count += 1
        
    print(f'Processed {line_count} lines.')