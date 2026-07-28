import cmath

def polar_coordinates(z):
    r = abs(z)
    phase = cmath.phase(z)
    
    return r, phase
    
z = complex(input().strip())

r, theta = polar_coordinates(z)

print(r)
print(theta)
