import requests
import hashlib
import random
from string import ascii_lowercase as letters


def basic_check(password: str) -> bool:
    """checkin if the given password has a length bigger than 8 and 
    consists of both letters and digits

    Args:
        password (str): the given password to be checked

    Returns:
        bool: True or False indicating the safety of the password due
        to the basic check took place in this function
    """
    
    if len(password) < 8:
        return False
    d = {'digits':0, 'letters':0}
    for char in password:
        d['digits'] += char.isdigit()
        d['letters'] += char.isalpha
    return d['letters'] > 0 and d['digits'] > 0


def is_password_safe(password: str) -> bool:
    """checking if the given password has been pwned before and also
    checking the basics of a safe password calling the "basic_check()"
    function

    Args:
        password (str): given password to be checked
        
    Returns:
        bool: True or False indicating if the given password is safe
    """
    
    if not basic_check(password):
        print('''the given string does not pass the basic requirements
              of a sufficient password; it should include both letters
              and digits and has have the length of more than 8
              characters''')
        return False
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


def generate_password(n: int) -> str:
    """generates a safe password of length "n"

    Args:
        n (int): the length of the password to be generated

    Returns:
        str: the generated safe password
    """
    
    if n < 8:
        ans = input('the given length is not long enough to be safe, do you want to continue anyway?(y/N)')
    if ans != 'y':
        return
    num1 = random.randint(10000)
    num2 = random.randint(10000)
    st = list(str(num1*num2))
    length = len(st)
    indices = [random.randint(length-1) for _ in range(100)]
    for i in indices:
        st[i] = random.choice(letters)
    st = ''.join(st)
    return hashlib.sha1(st.encode('utf-8')).hexdigest()[:n]


def helper_text() -> str:
    """providing the helper text if the "-h" or "--help" option is
    called

    Returns:
        str: the helper text for this library
    """
    
    text = '''
    # this module is aimed to help to make sure a chosen password is
    # safe and also generate a safe password
    
    # you have to pass either of these options:
    
    -h | --help
    # helper text for the module
    
    -v | --version
    # version of the module
    
    -c | --check
    # a password will be asked to check for its safety
    
    -g | --generate <length>
    #generates a safe password of the given length
    '''
    return text


def version() -> str:
    """returns the version of the library

    Returns:
        str: the version of the library
    """
    
    return '0.1.0'