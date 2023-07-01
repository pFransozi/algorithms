symbols = '$¢£¥€¤'

codes = [ord(x) for x in symbols]

print(codes)

codes = list(filter(lambda c: c, map(ord, symbols)))

print(codes)