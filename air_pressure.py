# sample code for calculating the air pressure at given height, z

import math 

p0 = 101325 #Pa
g = 9.8 #m/s^2
R = 8.314 #J/mol*K
M = .0289698 #MM of air, kg/mol

z = 0 # height in m
T = 273.15 #K

p = p0*math.exp(-g*z*M/(T*R))

# function for calculating pressure change with height for given z and T
def pressure_at_z(z, T):
    p = p0*math.exp(-g*z*M/(T*R))
    return(p)


def lapserate(z):
    T_lapse = (-6.5*z)+T
    return(T_lapse)

pressure = pressure_at_z(150,280)
print(pressure)

T_list = [] #K
Z_list = range(0,1000,100) #m

pressures_save = []
for x in range(0,len(Z_list)):
    T_lapse = lapserate(Z_list[x])
    T_list.append(T_lapse)
    ps_run = pressure_at_z(Z_list[x], T_lapse)
    pressures_save.append(ps_run)
    print(Z_list[x], T_lapse, ps_run)

print(pressures_save)