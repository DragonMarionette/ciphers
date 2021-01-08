from Cipher.column import *


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
my_key = input("Input a key string: ")

# do encoding or decoding
if encode:
    msg_encoded = col_encode(my_msg, my_key)
    print(f"\nEncoded message: [{msg_encoded}]")
else:
    msg_decoded = col_decode(my_msg[1:-1], my_key)
    print(f"\nDecoded message: {msg_decoded}")
