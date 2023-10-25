# Partner Hector Borjas
def encoder(unencoded_password):
    encoded = ""
    x = 0
    for num in unencoded_password:
        x = 0
        x += (int(num) + 3)
        if x > 9:
            x -= 10
        encoded = encoded + str(x)
    return encoded


def decoder(encoded_password):
    unencoded = ""
    x = 0
    for num in encoded_password:
        x = 0
        if int(num) < 3:
            x = 7 + int(num)
        else:
            x += (int(num) - 3)
        unencoded = unencoded + str(x)
    return unencoded


def main():
    while True:
        choice = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n \n Please enter an option: "))
        if choice == 1:
            unencoded_password = input("Please enter your password to encode: ")
            encoded_password = encoder(unencoded_password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print("The encoded password is ", end="")
            print(encoder(unencoded_password), end="")
            print(", and the original password is", unencoded_password,".")

        elif choice == 3:
            break


if __name__ == '__main__':
    main()
