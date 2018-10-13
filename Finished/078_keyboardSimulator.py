print(ord("a"), ord("A"), ord("a") - ord("A"))


def keytouchar(char, shift = False, caplock = False):
    if caplock == True:
        shift = True
    if shift == True:
        print(chr(ord(char) + 32))
    else:
        print(char)

keytouchar(input(), shift=True)

mktange
sub_shift = dict(zip("`1234567890-=[]\;',./", "~!@#$%^&*()_+{}|:\"<>?"))
def keytochar(key='a', shift=False, caps=False, ctrl=False, alt=False):
    if (key.isalpha()): return key.upper() if shift != caps else key.lower()
    return sub_shift[key] if shift and key in sub_shift else key

def string_convert(string):
    result, skey, status = [], dict(zip("scta",[False]*4)), False
    for c in string:
        if (c == '^'): status = True
        elif (status): skey[c.lower()], status = c.islower(), False
        else: result += keytochar(c, *[skey[c] for c in 'scta'])
    return ''.join(result)