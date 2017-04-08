def get_password_strength(password):
    strength = 0
    symbols = '#$@'
    digits = '0123456789'
    password_blacklist = ['password1', '12345', 'qwerty', 'bestpassword', 'password']
    if not (password.islower() or password.isupper()):
        strength += 2
    for digit in digits:
        if digit in password:
            strength += 2
            break
    for symbol in symbols:
        if symbol in password:
            strength += 2
            break
    for password_from_blacklist in password_blacklist:
        if password.lower() == password_from_blacklist.lower():
            break
    else:
        strength += 4

    return strength



if __name__ == '__main__':
    password = input()
    print('Уровень вашего пароля: %s' % get_password_strength(password))
