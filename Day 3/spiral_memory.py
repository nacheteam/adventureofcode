NUMBER = 361527

ring = 0
cont = 0
for i in range(1,NUMBER,2):
    cont+=1
    if i**2>=NUMBER:
        ring = i
        break

lower_ring = ring-2
ring_values = []
for i in range(lower_ring*lower_ring,ring*ring):
    ring_values.append(i)

index = NUMBER-lower_ring*lower_ring
center = int(ring/2)

side_coor = index%(ring-1)

print(abs(side_coor-center)+cont-1)
