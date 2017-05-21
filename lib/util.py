def full2half(s):
    n = []
    s = s.decode('utf-8')
    for char in s:
        num = ord(char)
        if num == 0x3000:
            num = 32
        elif 0xFF01 <= num <= 0xFF5E:
            num -= 0xFEE0
        num = unichr(num)
        n.append(num)
    return ''.join(n)
