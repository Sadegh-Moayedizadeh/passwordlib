import requests
import hashlib
from getpass import getpass
import sys

messages = ('''no arguments passed;
        to find out how to use this module, pass the option "-h" or 
        "--help"''',
        ''' ''',
        )
inputs = sys.argv
if len(inputs) ==  1:
    print(messages[0])



def is_password_safe() -> bool:
    password = getpass()
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    url = 'https://api.pwnedpasswords.com/range/' + hashed_password[:5]
    response = requests.get(url)
    passwords = [tuple(item.split(':')) for item in response.text.splitlines()]
    for item in passwords:
        if item[0] == hashed_password[5:]:
            print(f'NOT SAFE; this password has been pwned in {item[1]} data breaches')
            return False
    print('FINE; the given password hasn\'t been pwned before')
    return True
if __name__ == '__main__':
    is_password_safe()
