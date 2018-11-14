#! python3

# Email finder using Python
# (1) Create list of possible addresses given name and domain
# (2) Check list using validate_email module
# (3) Return valid addresses

import re
import sys

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

    list.append(first + '@' + domain)                    # first@example.com
    list.append(first[0] + '@' + domain)                 # f@example.com
    list.append(first[0] + last + '@' + domain)          # flast@example.com
    list.append(first[0] + '.' + last + '@' + domain)    # f.last@example.com
    list.append(first[0] + '_' + last + '@' + domain)    # f_last@example.com
    list.append(first[0] + '-' + last + '@' + domain)    # f-last@example.com
    list.append(first[0] + '-' + last + '@' + domain)    # first@example.com
    list.append(first + last + '@' + domain)             # firstlast@example.com
    list.append(first + '.' + last + '@' + domain)       # first.last@example.com
    list.append(first + '_' + last + '@' + domain)       # first_last@example.com
    list.append(first + '-' + last + '@' + domain)       # first-last@example.com
    list.append(first[0] + last[0] + '@' + domain)       # fl@example.com
    list.append(first[0] + '.' + last[0] + '@' + domain) # f.l@example.com
    list.append(first[0] + '-' + last[0] + '@' + domain) # f_l@example.com
    list.append(first[0] + '-' + last[0] + '@' + domain) # f-l@example.com
    list.append(first + last[0] + '@' + domain)          # fistl@example.com
    list.append(first + '.' + last[0] + '@' + domain)    # first.l@example.com
    list.append(first + '_' + last[0] + '@' + domain)    # fist_l@example.com
    list.append(first + '-' + last[0] + '@' + domain)    # fist-l@example.com
    list.append(last + '@' + domain)                     # last@example.com
    list.append(last[0] + '@' + domain)                  # l@example.com

    return(list)

# Find combinations for given input
email_list = email_list(first_name, last_name, domain_name)

# TODO: Validate them one by one


# TODO: If all are valid, give a catch-all warning
