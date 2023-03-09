def encoder(password):

    encoded = [int(num) + 3 for num in password]
    new_password = ''.join(map(str,encoded))
    return new_password



def main():

    print('Welcome to the encoder/decoder.')

    while True:
        print('1. Encode\n2. Decode\n3. Exit')

        menu_option = int(input('\nSelect menu option: '))

        if menu_option == 3:
            break

        if menu_option == 1:
            password = input('Enter password to be encoded: ')
            print(encoder(password))
            print()










if __name__ == '__main__':
    main()