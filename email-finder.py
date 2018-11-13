#! python3

# Email finder using Python
# (1) Create list of possible addresses given name and domain
# (2) Check list using validate_email module
# (3) Return valid addresses

import re
import sys
import validate_email

# Collect first name, last name, domain
try:
    input_first = sys.argv[1]       # First name
except IndexError:
    input_first = input('Please enter first name: > ')

try:
    input_last = sys.argv[2]        # Last name
except IndexError:
    input_last = input('Please enter last name: > ')

try:
    input_domain = sys.argv[3]      # Domain
except IndexError:
    input_domain = input('Please enter domain: > ')

# Convert in strings
first_name = str(input_first)
last_name = str(input_last)
domain_name = str(input_domain)

# Regex for names
name_regex = re.compile(r'([a-zA-Z])')

# Regex for domain
domain_regex = re.compile(r'''(
[a-zA-Z0-9.-]+         # second-level domain
(\.[a-zA-Z]{2,})       # top-level domain
)''', re.VERBOSE)

def regex_check(regex, name):
    while True:
        match = re.match(regex, name)
        if match == None:
            print('Name not formatted properly. Please enter it again.')
            name = str(input('Name: > '))
            continue
        else:
            break

# Regex check
regex_check(name_regex, first_name)
regex_check(name_regex, last_name)
regex_check(domain_regex, domain_name)

# List combinations from components

def email_list(first, last, domain):
    list = []
    list.append("test")
    return list

# Find combinations for given input
email_list(first_name, last_name, domain_name)

print(email_list)

# TODO: Validate them one by one

# TODO: If all are valid, give a catch-all warning

# TODO: List all valid email addresses

# TODO (OPTIONAL): Create file with email(s) or copy to clipboard
