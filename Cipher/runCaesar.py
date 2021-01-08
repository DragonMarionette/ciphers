from Cipher.caesar import *


# get user intent: encode or decode?
while True:
    enc_dec = input("Are you encoding or decoding? type 'e' to encode and 'd' to decode: ")
    if enc_dec.lower() == "e":
        encode = True
        break
    elif enc_dec.lower() == "d":
        encode = False
        break
    else:
        print("Input was not valid. Please try again.\n")

# get message from user
my_msg = input(f"Input a string to {'encode' if encode else 'decode'}: ")

# get key from user
while True:
    my_key = input("Input a key number: ")
    if my_key.isnumeric():
        my_key = int(my_key)
        break
    else:
        print("Input was not a number. Please try again.\n")

# do encoding or decoding
if encode:
    msg_encoded = shift_encode(my_msg, my_key)
    print(f"\nEncoded message: {msg_encoded}")
else:
    msg_decoded = shift_decode(my_msg, my_key)
    print(f"\nDecoded message: {msg_decoded}")