from random import randint

CHAR_MIN = 32  # ' '
CHAR_MAX = 126  # '~'
ALPHA_LENGTH = CHAR_MAX - CHAR_MIN + 1  # number of valid characters from CHAR_MIN to CHAR_MAX inclusive


def vig(message, key, enc=True):
    # create full key, store in key_full
    key_bytes = bytearray(key, 'ascii')
    key_simple = bytearray(len(key))
    for i in range(len(key)):
        key_simple[i] = (key_bytes[i] - CHAR_MIN) % ALPHA_LENGTH
    repetitions = -(ALPHA_LENGTH // -len(key))
    key_full = (key_simple * repetitions)[:ALPHA_LENGTH]

    message_bytes = bytearray(message, 'ascii')
    message_encoded = bytearray(len(message))
    for i in range(len(message)):
        if not CHAR_MIN <= message_bytes[i] <= CHAR_MAX:
            raise Exception(f"Character '{message[i]}' at index {i} of message cannot be interpreted")
        message_encoded[i] = \
            (message_bytes[i] - CHAR_MIN + (enc - (not enc)) * key_full[i % ALPHA_LENGTH]) \
            % ALPHA_LENGTH + CHAR_MIN
    return message_encoded.decode('ascii')


def vig_encode(message, key):
    return vig(message, key, True)


def vig_decode(message, key):
    return vig(message, key, False)


def random_key(length):
    key_listed = []
    for i in range(length):
        key_listed.append(randint(CHAR_MIN, CHAR_MAX))
    return bytearray(key_listed).decode('ascii')
