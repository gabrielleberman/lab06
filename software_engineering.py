def encoder(password):

    encoded = [int(num) + 3 for num in password]
    new_password = ''.join(map(str,encoded))
    return new_password

def decoder(password):
    decoded = [int(num) - 3 for num in password]
    old_password = ''.join(map(str, decoded))
    return old_password



def main():


    while True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')

        menu_option = int(input('\nPlease enter an option: '))

        if menu_option == 3:
            break

        if menu_option == 1:
            password = input('Enter password to be encoded: ')
            encodedpass = (encoder(password))
            print("Your password has been encoded and stored!\n")

        if menu_option == 2:
            print("The encoded password is " + encodedpass + ", and the original password is " + decoder(encodedpass) + ".\n")












if __name__ == '__main__':
    main()