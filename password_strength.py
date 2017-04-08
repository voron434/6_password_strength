def is_symbol_there(password):
    symbols = '#$@'
    for symbol in symbols:
        if symbol in password:
            return True


def is_digit_there(password):
    digits = '0123456789'
    for digit in digits:
        if digit in password:
            return True


def is_not_from_blacklist(password):
    password_blacklist = ['password1', '12345', 'qwerty', 'bestpassword', 'password']
    for password_from_blacklist in password_blacklist:
        if password.lower() == password_from_blacklist.lower():
            return False
    return True

def get_password_strength(password):
    strength = 1
    
    if not (password.islower() or password.isupper()):
        strength += 1
    if is_symbol_there(password):
        strength += 1
    if is_digit_there(password):
        strength += 1
    if is_not_from_blacklist(password):
        strength += 4
    if len(password) > 12:
        strength += 2
    elif len(password) > 6:
        strength += 1
    return strength



if __name__ == '__main__':
    password = input('Enter password to check:')
    print('Your password level: %s' % get_password_strength(password))
