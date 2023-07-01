symbols = '$¢£¥€¤'

codes = tuple(ord(symbol) for symbol in symbols)

print(codes)

import array

codes = array.array('I', (ord(symbol) for symbol in symbols))

print(codes)