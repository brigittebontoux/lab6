def encode(password):
    encoded_pass = ''
    for char in password:
        encoded_pass = encoded_pass + str((int(char)+3)%10)
    return encoded_pass


def decode():
    pass

def menu():
    while True:
        print('')
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        user_input = input('Please enter an option: ')
        if user_input == '1':
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!')
        elif user_input == '2':
            print(f'The encoded password is {encoded_pass}, and the original password is {password}.')
        elif user_input == '3':
            break

print(menu())


