# Password Gen-z :
import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passkey = ''.join(random.choice(characters) for _ in range(length))
    return passkey

def main():
    while True:
        print("\n-----------Password Generator------------")
        print("[1] Start generating password")
        print("[2] Exit")
        try:
            choice = int(input("Enter you choice : "))
            if(choice == 1):
                try:
                    length = int(input("Enter the length to generate password : "))
                    if(length <= 0):
                        print('----------------------------------------------')
                        print('Warning: The length must be greater than zero.')
                        print('----------------------------------------------')
                    else:
                        print('--------------------------------------------------')
                        print(f'Generated Password: {generate_password(length)}')
                        print('--------------------------------------------------')
                except ValueError:
                    print('-------------------------------------')
                    print('Warning: The length must be a number.')
                    print('-------------------------------------')
            if(choice == 2):
                print('-----------')
                print("Exiting....")
                print('-----------')
                break
            elif(choice < 1 and choice > 2):
                print('------------------------')
                print('Warning: Invalid choice.')
                print('------------------------')
        except ValueError:
            print('-------------------------------------')
            print('Warning: The choice must be a number.')
            print('-------------------------------------')


if __name__ == "__main__": 
    main()