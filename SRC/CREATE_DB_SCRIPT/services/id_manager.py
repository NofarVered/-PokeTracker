import base64


def id_encoding(first_field: str, second_field: str):
    string_to_encode = first_field+second_field
    string_to_encode_bytes = string_to_encode.encode('ascii')
    base64_bytes = base64.b64encode(string_to_encode_bytes)
    return base64_bytes.decode('ascii')


def id_dencoding(base64_string: str):
    base64_bytes = base64_string.encode('ascii')
    base64_bytes = base64.b64decode(base64_bytes)
    return base64_bytes.decode('ascii')
