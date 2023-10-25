
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








unencoded_password = input("Please enter a password to encode: ")

print("Encoded Password is: \n")
print(encoder(unencoded_password))
encoded = encoder(unencoded_password)
print("Unencoded Password is: \n")
print(unencoded_password(encoded))
