def check_symbol(password):
    symbols = '#$@'
    for symbol in symbols:
        if symbol in password:
            return 1
    return 0


def check_digit(password):
    digits = '0123456789'
    for digit in digits:
        if digit in password:
            return 1
    return 0


def check_blacklist(password):
    password_blacklist = ['password1', '12345', 'qwerty', 'bestpassword', 'password']
    for password_from_blacklist in password_blacklist:
        if password.lower() == password_from_blacklist.lower():
            return 0
    return 4


def check_length(password):
    if len(password) > 12:
        return 2
    elif len(password) > 6:
        return 1
    else:
        return 0

def get_password_strength(password):
    strength = 1
    password_checkers = [check_blacklist,
                         check_digit,
                         check_length,
                         check_symbol
                        ]
    for checker in password_checkers:
        strength += checker(password)
    return strength



if __name__ == '__main__':
    password = input('Enter password to check:')
    print('Your password level: %s' % get_password_strength(password))
