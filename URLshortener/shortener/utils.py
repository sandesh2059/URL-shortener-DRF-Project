BASE62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def base62(num):
    if num == 0:
        return BASE62[0]
    res = ''
    while num>0:
        res = BASE62[num%62] + res
        num //= 62
    return res