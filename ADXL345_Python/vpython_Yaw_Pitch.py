from vpython import *
from time import*
import numpy as np
import serial 
ad=serial.Serial('com5',115200)


scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)

scene.width=800
scene.height=600




##########################################################################################
length_box=0.1
width_box=0.1
height_box=0.004

#breadBoard
breadBoardBody1=box(length=8,width=1.43,height=.2,opacity=1,pos=vector(0,0,.75))
breadBoardBody2=box(length=8,width=1.43,height=.2,opacity=1,pos=vector(0,0,-.75))
breadBoardBody3=box(length=8,width=2.93,height=.1,opacity=1,pos=vector(0,-0.15,0))    
breadBoardLine1=box(length=7.3,width=0.06,height=0.01,color=color.red,pos=vector(0,0.1+0.005,-1.39))
breadBoardLine2=box(length=7.3,width=0.06,height=0.01,color=color.red,pos=vector(0,0.1+0.005,1.02))
breadBoardLine3=box(length=7.3,width=0.06,height=0.01,color=color.blue,pos=vector(0,0.1+0.005,1.39))
breadBoardLine4=box(length=7.3,width=0.06,height=0.01,color=color.blue,pos=vector(0,0.1+0.005,-1.02))
# for j in np.arange(1,8,0.17):
#     for i in np.arange(1,1.85,0.17):
#         breadBoardbox=box(length=length_box,width=width_box,height=height_box,color=color.black,pos=vector(-4.5+j,0.1+0.005,-0.83+i))
#         breadBoardbox1=box(length=length_box,width=width_box,height=height_box,color=color.black,pos=vector(-4.5+j,0.1+0.005,-1.87+i))
# for j in np.arange(1,8,0.17):
#     for i in np.arange(0,0.34,0.17):
#         breadBoardbox2=box(length=length_box,width=width_box,height=height_box,color=color.black,pos=vector(-4.5+j,0.1+0.005,-1.28+i))
#         breadBoardbox3=box(length=length_box,width=width_box,height=height_box,color=color.black,pos=vector(-4.5+j,0.1+0.005,1.13+i))
##arduino
arduino=box(length=2,width=1,height=0.1,color=vector(30/255.0,78/255.0,141/255.0),pos=vector(2.5,0.1+0.05,0))
arduinoConnecter1=box(length=.25,width=.35,height=0.15,color=color.white,pos=vector(3.38,0.1+0.15,0))
arduinoConnecter2=box(length=.2,width=.3,height=0.08,color=color.black,pos=vector(3.41,0.1+0.16,0))
box_with_empty_space = compound([arduinoConnecter1, arduinoConnecter2], pos=vec(3.38,0.1+0.15,0), type='difference')
arduinoproccesor=box(length=.4,width=.4,height=0.03,color=color.black,pos=vector(2.75,0.1+0.15,0))
arduinoproccesor.rotate(angle=pi/4, axis=vector(0, 1, 0))
arduinoConnecter3=box(length=.25,width=.35,height=0.1,color=color.black,pos=vector(1.61,0.1+0.15,0))
# for i in np.arange(0,0.2,0.1):
#     for j in np.arange(0,0.3,0.1):
#         arduinoConnecter4=cylinder(length=.01,width=.04,height=0.2,color=color.white,pos=vector(1.57+i,0.37,-0.1+j))
# for k in np.arange(0,1.875,0.125):
#     arduinopins1 = pyramid(pos=vector(3.3-k, 0.2, 0.42), size=vector(.03,.04,.05), color=vector(195/255,199/255,195/255),rotate=pi/4, axis=vector(0, 1, 0))
#     arduinopins2= pyramid(pos=vector(3.3-k, 0.2, -0.42), size=vector(.03,.04,.05), color=vector(195/255,199/255,195/255),rotate=pi/4, axis=vector(0, 1, 0))
arduinobutton=box(length=.11,width=.15,height=0.03,color=color.black,pos=vector(2.3,0.1+0.15,0))
arduinobutton1=cylinder(length=.05,width=.1,height=0.03,color=color.white,pos=vector(2.275,0.1+0.17,0))
# for c in np.arange(0,0.6,0.15):
#     arduinoled=box(length=.1,width=.06,height=0.03,color=vector(247/255, 239/255, 148/255),pos=vector(2.1,0.1+0.15,-0.23+c))
# for o in np.arange(0,0.24,0.03):
#     arduinopins3=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(2.78+o,0.1+0.14,-0.25+o))
#     arduinopins3.rotate(angle=(pi/4), axis=vector(0,1, 0))
#     arduinopins4=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(2.73-o,0.1+0.14,0.24-o))
#     arduinopins4.rotate(angle=(pi/4), axis=vector(0,1,0))
#     arduinopins5=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(2.78+o,0.1+0.14,0.24-o))
#     arduinopins5.rotate(angle=-(pi/4), axis=vector(0,1,0))
#     arduinopins6=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(2.73-o,0.1+0.14,-0.24+o))
#     arduinopins6.rotate(angle=-(pi/4), axis=vector(0,1,0))
##ADXL345
myIMU=box(length=1.1,width=0.9,height=0.1,color=vector(5/255,53/255,95/255))
myIMU.pos=vector(0,0.1+0.05,0)
hole_cylinder = cylinder(pos=vec(.43, 0.206,-.32), axis=vec(0, 0,0.04), radius=0.08, color=vector(250/255, 248/255, 205/255))
hole_cylinder.rotate(angle=(pi/2), axis=vector(1,0, 0))
hole_cylinder1 = cylinder(pos=vec(-.43, 0.206,-.32), axis=vec(0, 0,0.04), radius=0.08, color=vector(250/255, 248/255, 205/255))
hole_cylinder1.rotate(angle=(pi/2), axis=vector(1,0, 0))
box_with_hole = compound([myIMU, hole_cylinder])
# for k in np.arange(0,1,0.125):
#     arduinoPins1 = pyramid(pos=vector(0.45-k, 0.2, 0.38), size=vector(.03,.04,.05), color=vector(195/255,199/255,195/255),rotate=pi/4, axis=vector(0, 1, 0))
imuprocessor=box(length=0.12,width=0.07,height=0.1,color=color.orange,pos=vector(0,.2,-.3))
imuprocessor1=box(length=0.35,width=0.23,height=0.1,color=color.black,pos=vector(0,.2,0))
# for s in np.arange(0,0.24,0.03):
#     arduinoPins3=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(-0.105+s,0.21,0.11))
#     arduinoPins3.rotate(angle=(pi/2), axis=vector(0,1, 0))
#     arduinoPins4=box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(-0.105+s,0.21,-0.11))
#     arduinoPins4.rotate(angle=(pi/2), axis=vector(0,1, 0))
##connections_Lines
line=box(size=vector(.87,0.03,0.05),color=color.blue,pos=vector(-.45,.1,0.9))
line.rotate(angle=(pi/2), axis=vector(0,1, 0))
line1=box(size=vector(.83,0.03,0.05),color=color.red,pos=vector(-.26,.1,0.75))
line1.rotate(angle=(pi/2), axis=vector(0,1, 0))
line2=box(size=vector(1.62,0.03,0.05),color=color.orange,pos=vector(1.2,.1,0.7))
line2.rotate(angle=(pi), axis=vector(0,1, 0))
line3=box(size=vector(1.62,0.03,0.05),color=color.orange,pos=vector(1,.1,0.85))
line3.rotate(angle=(pi), axis=vector(0,1, 0))
# Combine all objects into a list
all_shapes = [
    breadBoardBody1, breadBoardBody2, breadBoardBody3, breadBoardLine1, breadBoardLine2,
    breadBoardLine3, breadBoardLine4,arduino, arduinobutton, arduinobutton1, box_with_empty_space,
    arduinoproccesor, arduinoConnecter3, myIMU,
    hole_cylinder, hole_cylinder1, box_with_hole, imuprocessor,
    imuprocessor1,line, line1, line2, line3
]
# Add shapes generated in the for loops to the list
for j in np.arange(1, 8, 0.17):
    for i in np.arange(1, 1.85, 0.17):
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, -0.83 + i)))
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, -1.87 + i)))

for j in np.arange(1, 8, 0.17):
    for i in np.arange(0, 0.34, 0.17):
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, -1.28 + i)))
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, 1.13 + i)))
for j in np.arange(1, 8, 0.17):
    for i in np.arange(0, 0.34, 0.17):
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, -1.28 + i)))
        all_shapes.append(box(length=length_box, width=width_box, height=height_box,
                              color=color.black, pos=vector(-4.5 + j, 0.1 + 0.005, 1.13 + i)))

for i in np.arange(0, 0.2, 0.1):
    for j in np.arange(0, 0.3, 0.1):
        all_shapes.append(cylinder(length=0.01, width=0.04, height=0.2, color=color.white,
                                   pos=vector(1.57 + i, 0.37, -0.1 + j)))

for k in np.arange(0, 1.875, 0.125):
    all_shapes.append(pyramid(pos=vector(3.3 - k, 0.2, 0.42), size=vector(.03, .04, .05),
                              color=vector(195/255, 199/255, 195/255), rotate=pi/4, axis=vector(0, 1, 0)))
    all_shapes.append(pyramid(pos=vector(3.3 - k, 0.2, -0.42), size=vector(.03, .04, .05),
                              color=vector(195/255, 199/255, 195/255), rotate=pi/4, axis=vector(0, 1, 0)))

for c in np.arange(0, 0.6, 0.15):
    all_shapes.append(box(length=.1, width=.06, height=0.03, color=vector(247/255, 239/255, 148/255),
                          pos=vector(2.1, 0.1 + 0.15, -0.23 + c)))

for o in np.arange(0, 0.24, 0.03):
    all_shapes.append(box(length=.07, width=.015, height=0.027, color=color.white,
                          pos=vector(2.78 + o, 0.1 + 0.14, -0.25 + o),angle=(pi/4), axis=vector(0,1, 0)))
    all_shapes.append(box(length=.07, width=.015, height=0.027, color=color.white,
                          pos=vector(2.73 - o, 0.1 + 0.14, 0.24 - o),angle=(pi/4), axis=vector(0,1, 0)))
    all_shapes.append(box(length=.07, width=.015, height=0.027, color=color.white,
                          pos=vector(2.78 + o, 0.1 + 0.14, 0.24 - o),angle=-(pi/4), axis=vector(0,1, 0)))
    all_shapes.append(box(length=.07, width=.015, height=0.027, color=color.white,
                          pos=vector(2.73 - o, 0.1 + 0.14, -0.24 + o),angle=-(pi/4), axis=vector(0,1, 0)))
for k in np.arange(0,1,0.125):
    all_shapes.append(pyramid(pos=vector(0.45-k, 0.2, 0.38), size=vector(.03,.04,.05), color=vector(195/255,199/255,195/255),rotate=pi/4, axis=vector(0, 1, 0)))
for s in np.arange(0,0.24,0.03):
    all_shapes.append(box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(-0.105+s,0.21,0.11),angle=(pi/2), axis=vector(0,1, 0)))
    all_shapes.append(box(length=.07,width=.015,height=0.027,color=color.white,pos=vector(-0.105+s,0.21,-0.11),angle=(pi/2), axis=vector(0,1, 0)))
# Create a compound object
myOBJ = compound(all_shapes)
########################################################################################################################

Xarrow=arrow(axis=vector(1,0,0),length=2,shaftwidth=.2,color=color.red)
Yarrow=arrow(axis=vector(0,1,0),length=2,shaftwidth=.2,color=color.green)
Zarrow=arrow(axis=vector(0,0,1),length=2,shaftwidth=.2,color=color.blue)

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

while (True):
    pitch=0*toRad
    while(ad.inWaiting()==0):
        pass
    dataPacket=ad.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitDataPacket=dataPacket.split(",")
    pitch=float(splitDataPacket[0])*toRad
    roll=float(splitDataPacket[1])*toRad
    rate(50)
    yaw=0
    k=-vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
    y=vector(0,1,0)
    s=cross(k,y)
    v=cross(s,k)
    vrot=v*cos(roll)+cross(k,-v)*sin(roll)

    frontArrow.axis=k
    sideArrow.axis=cross(k,vrot)
    upArrow.axis=vrot
    myOBJ.axis=k
    myOBJ.up=vrot
    sideArrow.length=2
    frontArrow.length=6
    upArrow.length=1