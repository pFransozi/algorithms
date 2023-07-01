symbols = '$¢£¥€¤'
codes = []
codes_listcomp = [ord(symbol) for symbol in symbols]

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)
print(codes_listcomp)