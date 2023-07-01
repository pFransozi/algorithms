x = 'ABC'

codes = [ord(x) for x in x]

print(x)
print(codes)

# variables assigned with the “Walrus operator” := remain
# accessible after those comprehensions or expressions return
codes = [last := ord(c) for c in x]

print(last)
print(c)
