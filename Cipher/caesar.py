def shift(message, key):
    message_bytes = bytearray(message, 'ascii')
    message_encoded = bytearray(len(message))
    for i in range(len(message)):
        if not 32 <= message_bytes[i] <= 126:
            raise Exception(f"Character '{message[i]}' at index {i} of message cannot be interpreted")
        message_encoded[i] = (message_bytes[i] - 32 + key) % 95 + 32  # 95 valid characters from ' ' to '~'
    return message_encoded.decode('ascii')


def shift_encode(message, key):
    return "[" + shift(message, key) + "]"


def shift_decode(message, key):
    return shift(message[1:-1], -key)
