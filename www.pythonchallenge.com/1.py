s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

"""
# mannul

chars = []
upper_limit = ord('z')
for i in s:
    if i in (" ", ".", "(", ")", "'"):
        chars.append(i)
    elif ord(i) + 2 > upper_limit:
        chars.append(chr(ord(i) + 2 - 26))
    else:
        chars.append(chr(ord(i) + 2))

s = "".join(chars)
print s
"""

# recommended

import string

old_chars = string.lowercase
new_chars = old_chars[2:] + old_chars[:2]
tr = string.maketrans(old_chars, new_chars)
s = s.translate(tr)
print s
