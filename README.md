# Email Finder

A Python script to find valid email addresses given a first name, last name and domain.

### Introduction

Given <code>first name</code>, <code>last name</code> and <code>domain name</code> the program:

1. Creates list of 20 possible formats given name and domain

2. Verifies whether email addresses exists

3. Returns valid addresses

### Dependencies

* [dns.resolver](https://github.com/rthalley/dnspython) (DNS toolkit) <code>pip install dnspython</code>

* [Pyperclip](https://github.com/asweigart/pyperclip) (clipboard functions) <code>pip install pyperclip</code>

### Usage

<code>python email-verifier.py [first name] [last name] [domain]  </code>

Alternatively, if arguments are missing, the script will request user input.

### Errors

The script will detect and handle basic errors:

**1. Domain not found** on DNS query

**2. No answer** for DNS query

**3. SMTP Server disconnection**

The program tends to not work / return false positives for personal emails, probably due to filters / catch-all addresses.  

### Improvements

This program can be improved with additional features:

**1. Stronger email verification**

Email verification using existing modules such as [Validate_email](https://github.com/syrusakbary/validate_email/) or APIs such as [Mailgun](https://www.mailgun.com/email-validation) or [MailboxValidator](https://www.mailboxvalidator.com/).

**2. Generic emails**

If no valid email address is returned, generic email addresses (e.g. info@domain) will be checked.

**3. Optional middle name**

Add possibility to input middle name and support additional email formats.

**4. Bulk finder**

Find multiple addresses at once from a given file.

**5. SMTP response**

Add more allowed responses than the standard 250 success code.

**6. Search engine check**

Run a second verification to check whether the email address(es) found has been indexed by a search engine.
