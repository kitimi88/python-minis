import os
import sys
import qrcode

def qr_generator():
    data = input("Enter data to encode in QR code: ")
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", black_color="white")

    filename = input("Enter filename including extension (.jpg, .png): ")
    
    path_option = input("Do you want to specify a file path to save the QR code? (y/n) ")
    if path_option == 'y' or path_option == 'Y':
        path = input("Enter file path to save the QR code: ")
        filename = path + "/" + filename
    
    img.save(filename)
    print(f"Your QR code has been saved to {filename}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'QR Code Generator'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    qr_generator()
    
    while True:
        response = input('\nDo you want to continue? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select y or n.\n')
            continue

if __name__ == '__main__':
    main()
