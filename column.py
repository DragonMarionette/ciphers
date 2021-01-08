import operator


def convert_key(key):
    key_numeric = []
    for i in range(len(key)):
        key_numeric.append([i, ord(key[i])])
    key_numeric.sort(key=operator.itemgetter(1, 0))
    return [l[0] for l in key_numeric]


def col_encode(message, key_str):
    key = convert_key(key_str)
    width = len(key)
    height = -(len(message) // -len(key))  # ceiling of (message / key) lengths
    message_encoded = [' '] * (width * height)

    for i in range(len(message)):
        message_encoded[(key[i % width] * height) + (i // width)] = message[i]
    return ''.join(message_encoded)


def col_decode(message, key_str):
    key = convert_key(key_str)
    width = len(key)
    height = len(message) // len(key)
    message_decoded = ['\0'] * (len(message))

    for i in range(len(message)):
        message_decoded[(i % height) * width + key.index(i // height)] = message[i]
    return ''.join(message_decoded)
