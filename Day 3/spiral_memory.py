NUMBER = 361527

# Get the ring and the distance from the center (1).
ring = 0
cont = 0
for i in range(1,NUMBER,2):
    cont+=1
    if i**2>=NUMBER:
        ring = i
        break

# Get the ring just below ours.
lower_ring = ring-2

# We can know the index in the list of our number
index = NUMBER-lower_ring*lower_ring
center = int(ring/2)

side_coor = index%(ring-1)

print(abs(side_coor-center)+cont-1)
