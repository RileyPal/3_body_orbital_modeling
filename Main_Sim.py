import numpy as np
import cmath as cm

G = 6.67430*10**-11 # m^3/(Kg*s^2)
mass1 = 5.97*10**24 # mass of the earth
mass2 = 7.35*10**22 # mass of the moon
mass3 = 408000 # mass of the ISS for example station mass
x1 = 0
y1 = 0
z1 = 0
vx1 = 0
vy1 = 0
vz1 = 0
vx2 = 0
vy2 = 1100 # Orbital velocity of moon at it's closest in meters/second
vz2 = 0
x2 = 364397*1000 # Rough periapsis for moons orbit in meters
y2 = 0
z2 = 0
body1 = [mass1, x1, y1, z1, vx1, vy1, vz1]
body2 = [mass2, x2, y2, z2, vx2, vy2, vy3]
body3 = [mass3, x3, y3, z3, ]
F1 = G*(body1[0]*body2[0])/((((body2[1]-body1[1])**2 + (body2[2]-body1[2])**2 + (body2[3]-body1[3])**2)**.5))**2 #force of body2 on body1
Dir1 = np.array([(body2[1]-body1[1]), (body2[2]-body1[2]), (body2[3]-body1[3])])
UnitDir1 = Dir1 / np.linalg.norm(Dir1) # unit vector for direction that body2 acts on body1
Dir2 = np.array([(body3[1]-body1[1]), (body3[2]-body1[2]), (body3[3]-body1[3])])
UnitDir2 = Dir2 / np.linalg.norm(Dir2) # unit vector for direction that body3 acts on body1
Dir3 = np.array([(body3[1]-body2[1]), (body3[2]-body2[2]), (body3[3]-body2[3])])
UnitDir3 = Dir3 / np.linalg.norm(Dir3) # unit vector for direction that body2 acts on body3
f1 = G*(body1[0]*body3[0])/(((((body3[1]-body1[1])**2) + (body3[2]-body1[2])**2 + (body3[3]-body1[3])**2))**.5)**2 #force of body3 on body 1
F2 = -F1 #force of body1 on body2
f2 = G*(body2[0]*body3[0])/(((((body3[1]-body2[1])**2)+(body3[2]-body2[2])**2+(body3[3]-body2[3])**2))**.5)**2 # force of body3 on body2
F3 = -f1 # force of body1 on body3
f3 = -f2 # force of body2 on body3
# F2, F3 and f3 here defined for redundancy
Forces_1 = F1 * UnitDir1 + f1 * UnitDir2  # Forces on body 1
Forces_2 = F1 * (-UnitDir1) + f2 * UnitDir3  # Forces on body 2
Forces_3 = f1 * (-UnitDir2) + f2 * (-UnitDir3)  # Forces on body 3


def update_body_position_velocity(body, forces, dt):
    """
    Updates the velocity and position of a single body given the forces acting on it.

    Parameters:
    - body: list containing [mass, x, y, z, vx, vy, vz] (position and velocity components)
    - forces: array containing [Fx, Fy, Fz] (force components acting on the body)
    - dt: time step (float)

    Returns:
    Updated body list with new position and velocity.
    """
    mass = body[0]  # The mass of the body

    # Extract the current position (x, y, z) and velocity (vx, vy, vz)
    x, y, z = body[1], body[2], body[3]
    vx, vy, vz = body[4], body[5], body[6]

    # Compute acceleration from forces: a = F / m
    ax, ay, az = forces[0] / mass, forces[1] / mass, forces[2] / mass

    # Update velocity: v_new = v_old + a * dt
    vx_new = vx + ax * dt
    vy_new = vy + ay * dt
    vz_new = vz + az * dt

    # Update position: r_new = r_old + v_new * dt
    x_new = x + vx_new * dt
    y_new = y + vy_new * dt
    z_new = z + vz_new * dt

    # Return the updated body information
    return [mass, x_new, y_new, z_new, vx_new, vy_new, vz_new]


# Time step for the simulation (in seconds)
dt = 60  # Example: 60 seconds (1 minute)

# Assuming Forces_1, Forces_2, and Forces_3 have already been computed for each body:
# - Forces_1 is the net force acting on body1 (Earth)
# - Forces_2 is the net force acting on body2 (Moon)
# - Forces_3 is the net force acting on body3 (Station)

# Body 1 (Earth): Update position and velocity based on forces acting on it
body1 = update_body_position_velocity(body1, Forces_1, dt)

# Body 2 (Moon): Update position and velocity based on forces acting on it
body2 = update_body_position_velocity(body2, Forces_2, dt)

# Body 3 (Station): Update position and velocity based on forces acting on it
body3 = update_body_position_velocity(body3, Forces_3, dt)

# Optional: print out the updated state for transparency
print("Updated state of Earth (Body 1):", body1)
print("Updated state of Moon (Body 2):", body2)
print("Updated state of Station (Body 3):", body3)