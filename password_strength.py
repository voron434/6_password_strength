def get_password_strength(password):
    strength = 0
    symbols = '#$@'
    digits = '0123456789'
    password_blacklist = ['password1', '12345', 'qwerty', 'bestpassword', 'password']
    if not (password.islower() or password.isupper()):
        strength += 1

    for digit in digits:
        if digit in password:
            strength += 1
            break

    for symbol in symbols:
        if symbol in password:
            strength += 1
            break

    for password_from_blacklist in password_blacklist:
        if password.lower() == password_from_blacklist.lower():
            break
    else:
        strength += 4

    if len(password) > 18:
        strength += 3
    elif len(password) > 12:
        strength += 2
    elif len(password) > 6:
        strength += 1

    return strength



if __name__ == '__main__':
    password = input('Enter password to check:')
    print('Уровень вашего пароля: %s' % get_password_strength(password))

