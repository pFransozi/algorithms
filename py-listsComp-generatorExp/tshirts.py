colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# a listcomp that generates a list of tuples (color, size).
# color than size
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

# size than color
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

#a for nested way to generate the above list of tuples.
for color in colors:
    for size in sizes:
        print((color, size))