# https://edabit.com/challenge/ZsAXt5Kj5EP4v3ack
# 27.06.2025
# Vary Hard


def secret(txt):
    outer_tag = txt[:txt.index('>')]
    inner_tag = txt[txt.index('>') + 1:txt.index('.')]
    pad_width = txt.count('$')
    class_prefix = txt[txt.index('.') + 1:txt.index('$')]
    length = int(txt[txt.index('*') + 1:])
    res = f'<{outer_tag}>'
    for n in map(str, range(1, length + 1)):
        class_name = class_prefix + n.zfill(pad_width)
        res += f"<{inner_tag} class='{class_name}'></{inner_tag}>"
    res += f'</{outer_tag}>'
    return res
