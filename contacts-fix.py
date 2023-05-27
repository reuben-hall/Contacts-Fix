import csv
import re

filename = '/Users/reuben/Development/Python/Contacts Fix/contacts-2.csv'

with open(filename, 'r') as csvfile:
    contactsreader = csv.DictReader(csvfile)

    line_count = 0

    for row in contactsreader:

        test_char = row["Mobile Phone"]
        
        if (test_char):

            if test_char[0] == "0":
                print(f'{test_char}' + ' starts with 0')
            else:
                print(f'{test_char}' + ' does not start with 0')
        
        else:
            print(f'-' * 75)
        
        line_count += 1
        
    print(f'Processed {line_count} lines.')