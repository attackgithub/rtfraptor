from binascii import hexlify


def clsid_to_hex(data):
    """
    Convert a string class ID (as displayed) to the hex representation.
    """

    # See: https://support.microsoft.com/en-us/kb/325648
    data = data.replace('-', '')

    hex_str = data[6:8]
    hex_str += data[4:6]
    hex_str += data[2:4]
    hex_str += data[0:2]
    hex_str += data[10:12]
    hex_str += data[8:10]
    hex_str += data[14:16]
    hex_str += data[12:14]
    hex_str += data[16:]
    return hex_str


def bytes_to_clsid(data):
    """
    Convert raw bytes to a class ID representation (without the {brackets}).
    """
    data = hexlify(data)

    clsid = data[6:8]
    clsid += data[4:6]
    clsid += data[2:4]
    clsid += data[0:2]
    clsid += '-'
    clsid += data[10:12]
    clsid += data[8:10]
    clsid += '-'
    clsid += data[14:16]
    clsid += data[12:14]
    clsid += '-'
    clsid += data[16:20]
    clsid += '-'
    clsid += data[20:]

    return clsid.upper()