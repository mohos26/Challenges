# https://edabit.com/challenge/ZvjGe7dQAbvbxoPGZ
# 4.11.2023
# Very Hard


def rgb_or_hex(*args):
    if type(args[0]) == str:
        return [int(f'0x{args[0][1:3]}', 16), int(f'0x{args[0][3:5]}', 16), int(f'0x{args[0][5:]}', 16)]
    return f'#{hex(args[0])[2:]}{hex(args[1])[2:]}{hex(args[2])[2:]}'


def rgb_or_hex_gpt(*args):
    if len(args) == 1 and isinstance(args[0], str) and args[0].startswith("#") and len(args[0]) == 7:
        # Input is a hexadecimal string
        hex_value = args[0][1:]  # Remove the '#' character
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        return r, g, b
    elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
        # Input is RGB tuple
        r, g, b = args
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_color
    else:
        raise ValueError("Invalid input format. Provide either RGB tuple or hexadecimal string.")
