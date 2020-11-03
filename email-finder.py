#! python3

# Email finder using Python
# (1) Create list of possible addresses given name and domain
# (2) Verify whether email addresses exist
# (3) Return valid addresses

import re
import sys
import socket
import smtplib
import pyperclip
import dns.resolver

# Collect first name, last name, domain
try:
    first_name = sys.argv[1]       # First name
except IndexError:
    first_name = str(input('Please enter first name: > '))

try:
    last_name = sys.argv[2]        # Last name
except IndexError:
    last_name = str(input('Please enter last name: > '))

try:
    domain_name = sys.argv[3]      # Domain
except IndexError:
    domain_name = str(input('Please enter domain: > '))

# Regex for names
name_regex = re.compile(r'([a-zA-Z])')

# Regex for domain
domain_regex = re.compile(r'''(
[a-zA-Z0-9.-]+         # second-level domain
(\.[a-zA-Z]{2,})       # top-level domain
)''', re.VERBOSE)

def regex_check(regex, name):
    """
    Check proper format of first name, last name and domain using regex.
    If not formatted properly, ask user to input a new first/last/domain name.
    """
    while True:
        match = re.match(regex, name)
        if match == None:
            if name == first_name:
                required = 'first name'
            elif name == last_name:
                required = 'last name'
            elif name == domain_name:
                required = 'domain name'
            print('%s is not a valid %s.' % (name, required))
            name = str(input('Please enter %s again: > ' % required))
            continue
        else:
            break

# Regex check
regex_check(name_regex, first_name)
regex_check(name_regex, last_name)
regex_check(domain_regex, domain_name)

def formats(first, last, domain):
    """
    Create a list of 20 possible email formats combining:
    - First name:          [empty] | Full | Initial |
    - Delimitator:         [empty] |   .  |    _    |    -
    - Last name:           [empty] | Full | Initial |
    """
    list = []

    list.append(first[0] + '@' + domain)                 # f@example.com
    list.append(first[0] + last + '@' + domain)          # flast@example.com
    list.append(first[0] + '.' + last + '@' + domain)    # f.last@example.com
    list.append(first[0] + '_' + last + '@' + domain)    # f_last@example.com
    list.append(first[0] + '-' + last + '@' + domain)    # f-last@example.com
    list.append(first + '@' + domain)                    # first@example.com
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

emails_list = formats(first_name, last_name, domain_name)

def verify(list, domain):
    """
    Create a list of all valid addresses out of a list of emails.
    """

    valid = []

    for email in list:
        try:
            records = dns.resolver.query(domain, 'MX')
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            print('DNS query could not be performed.')
            quit()

        # Get MX record for the domain
        mx_record = records[0].exchange
        mx = str(mx_record)

        # Get local server hostname
        local_host = socket.gethostname()

        # Connect to SMTP
        smtp_server = smtplib.SMTP()
        smtp_server.connect(mx)
        smtp_server.helo(local_host)
        smtp_server.mail(email)
        code, message = smtp_server.rcpt(email)

        try:
            smtp_server.quit()
        except smtplib.SMTPServerDisconnected:
            print('Server disconnected. Verification could not be performed.')
            quit()

        # Add to valid addresses list if SMTP response is positive
        if code == 250:
            valid.append(email)
        else:
            continue

    return(valid)

valid_list = verify(emails_list, domain_name)

def return_valid(valid, possible):
    """
    Return final output comparing list of valid addresses to the possible ones:
    1. No valid  > Return message
    2. One valid > Copy to clipboard
    3. All valid > Catch-all server
    4. Multiple  > List addresses
    """
    if len(valid) == 0:
        print('No valid email address found for ' + first_name + ' ' + last_name)
    elif len(valid) == 1:
        print('Valid email address found and copied to clipboard: ' + valid[0])
        pyperclip.copy(valid[0])
    elif len(valid) == len(possible):
        print('Catch-all server. Verification not possible.')
    else:
        print('Multiple valid email addresses found:')
        for address in valid:
            print(address)

return_valid(valid_list, emails_list)
