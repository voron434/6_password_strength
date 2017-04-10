from getpass import getpass
import os


def check_symbol(password):
    symbols = '!@#$%^&*()_+-=:;"?/>.<,|'
    for symbol in symbols:
        if symbol in password:
            return True


def check_digit(password):
    digits = '0123456789'
    for digit in digits:
        if digit in password:
            return True


def load_blacklist(path='Blacklist.txt'):
    with open(path, mode='r', encoding='utf-8') as blacklist_file:
        blacklist = []
        for blacklist_password in blacklist_file:
            blacklist.append(blacklist_password[:-1]) #for deleting line break
    return blacklist


def check_blacklist(password):
    blacklist = load_blacklist()
    for password_from_blacklist in blacklist:
        if password.lower() == password_from_blacklist.lower():
            return False
    return True


def check_length6(password):
    if len(password) > 6:
        return True


def check_length12(password):
    if len(password) > 12:
        return True


def get_password_strength(password):
    strength = 1
    password_checkers = [{'checker': check_symbol, 'points': 2},
                         {'checker': check_digit, 'points': 1},
                         {'checker': check_blacklist, 'points': 4},
                         {'checker': check_length6, 'points': 1},
                         {'checker': check_length12, 'points': 1}
                         ]
    for checker in password_checkers:
        if checker['checker'](password):
            strength += checker['points']
    return strength


if __name__ == '__main__':
    if not os.path.exists('Blacklist.txt'):
        print('Blacklist not found, sorry... I would not add points for this type of check.'
              'There must be file "Blacklist.txt" in the same directory as this script')
    password = getpass('Enter password to check:')
    print('Your password level: %s' % get_password_strength(password))
