import numpy as np
import cmath as cm

G = 6.67430*10**-11 # m^3/(Kg*s^2)
mass1 = 5.97*10**24 # mass of the earth
mass2 = 7.35*10**22 # mass of the moon
mass3 = 408000 # mass of the ISS
x1 = 0
y1 = 0
z1 = 0
body1 = [mass1, x1, y1, z1]
body2 = [mass2, x2, y2, z2]
body3 = [mass3, x3, y3, z3]
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

Forces_1 = np.array([F1*UnitDir1[0] + f1*UnitDir2[0] + , F1*UnitDir1[1] + f1*UnitDir2[1], F1*UnitDir1[2] + f1*UnitDir2[2]])
