import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import csv

def truncate(n, decimals=3):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

""" def ideal():
    v0=20
    g=-9.81
    alpha=45
    t=0
    dt=0.01

    idealX=0
    idealY=0

    while idealY>=0:
        t+=dt
        idealX=v0*t
        idealY=g/2*t*t+v0*t*math.sin(math.radians(alpha))
        listParabolX.append(idealX)
        listParabolY.append(idealY) """

#constant:
g=-9.81
m=1.0
rho=1.22
cd=0.47
ar=0.078
dt=0.01

#initial:
v0x=20.0
v0y=5.0
v0z=10.0
alpha=45.0
x0=0.0
y0=0.0
z0=0.0

#variable:
t=0.0

x=x0
y=y0
z=z0

vx=v0x
vy=v0y
vz=v0z

ax=0.0
ay=0.0
az=0.0

fx=0.0
fy=0.0
fz=0.0

fg=0.0

fdx=0.0
fdy=0.0
fdz=0.0

maxX=0.0
maxY=0.0
maxZ=0.0

startX=x
startY=y
startZ=z

#lists
listT=[]
listX=[]
listY=[]
listZ=[]
listVx=[]
listVy=[]
listVz=[]
listAx=[]
listAy=[]
listAz=[]

#listParabolX=[] #ideal flight curve x-values
#listParabolY=[] #ideal flight curve y-values

print("\nSTARTING...\n")
print("t,x,y,z,vx,vy,vz,ax,ay,az")

# open csv file in the write mode
f=open("./data/data.csv","w",encoding="UTF8")

# create the csv writer
writer=csv.writer(f)

#header for csv file
header="t","x","y","z","vx","vy","vz","ax","ay","az"

# write a row to the csv file
writer.writerow(header)

#sim loop
while z >= 0.0:
    print(truncate(t,2),truncate(x,3),truncate(y,3),truncate(z,3),truncate(vx,3),truncate(vy,3),truncate(vz,3),truncate(ax,3),truncate(ay,3),truncate(az,3))

    dataRow=truncate(t,2),truncate(x,3),truncate(y,3),truncate(z,3),truncate(vx,3),truncate(vy,3),truncate(vz,3),truncate(ax,3),truncate(ay,3),truncate(az,3)
    # write a row to the csv file
    writer.writerow(dataRow)
    
    listT.append(t)
    listX.append(x)
    listY.append(y)
    listZ.append(z)
    listVx.append(vx)
    listVy.append(vy)
    listVz.append(vz)
    listAx.append(ax)
    listAy.append(ay)
    listAz.append(az)
    
    t+=dt

    v0x=vx
    v0y=vy
    v0z=vz


    x0=v0x*dt

    if x<(x+x0):
        maxX=x+x0

    x+=x0

    y0=v0y*dt

    if y<(y+y0):
        maxY=y+y0

    y+=y0

    z0=v0z*dt

    if z<(z+z0):
        maxZ=z+z0

    z+=z0
    
    fg=m*g
    
    if vx>0.0:   
        fdx=-0.5*rho*cd*vx*vx*ar
    else:
        fdx=0.5*rho*cd*vx*vx*ar
    
    if vy>0.0:   
        fdy=-0.5*rho*cd*vy*vy*ar
    else:
        fdy=0.5*rho*cd*vy*vy*ar
    
    if vz>0.0:   
        fdz=-0.5*rho*cd*vy*vy*ar
    else:
        fdz=0.5*rho*cd*vy*vy*ar

    fx=fdx
    fy=fdy
    fz=fg+fdz

    ax=fx/m
    ay=fy/m
    az=fz/m

    v0x=ax*dt
    v0y=ay*dt
    v0z=az*dt

    vx+=v0x
    vy+=v0y
    vz+=v0z

# close csv file
f.close()

print("maxX:",truncate(maxX,3))
print("maxY:",truncate(maxY,3))
print("maxZ:",truncate(maxZ,3))

#print(listX) #debug
#print(listY) #debug
#print(listZ) #debug

print("\nFINISHED")

#ax=plt.axes()

"""ax.set(facecolor="black")
ax.patch.set_alpha(1.0)"""

fig = plt.figure()

"""fig.patch.set_facecolor("gray")
fig.patch.set_alpha(0.6)"""

#ideal()

ax = plt.axes(projection="3d")
ax.set_aspect('equal')
ax.plot3D(listX,listY,listZ,color='b',label="sim",linestyle='-')
#plt.plot(listParabolX,listParabolY,color='r',label="ideal",linestyle='--')
plt.title("Projectile Flight Path")
#plt.xlabel("x / m")
#plt.ylabel("y / m")
plt.legend()
plt.show()
