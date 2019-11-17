# Neo.Farm : Circular Trajectory Program cir_mvt.py

​	**Neo.Farm** is a start-up company which objective is to develop an environmentally friendly farm thanks to a CNC like robotic system. Some operations need to perform circular trajectory. However, the controller used for the robot take in input the coordinates of an arrival point and control the robot to move its tool to this coordinates in a straight line.

​	To make a circular movement, one can imagine a set of n points (with n great enough) and make a continuous piecewise circular trajectory.

## Program description :

​	The program **cir_mvt.py** is a program dedicated for **Neo.Farm** to create a .json file called ***cir_mvt.json*** which describes a circular trajectory over the 3 Cartesian planes XY , YZ , XZ by a succession of n points evenly spaced. This set of points form a continuous piecewise circular trajectory of desired radius and oriented angle.

## Statements :

- Starting point will always be at coordinates : (0,0,0)
- Circle center is always on an axis.

## Inputs :

This program has several inputs :

plane :	 Is the Cartesian plane where the circle will be described. It is either : XY , XZ or XZ. It must respect the Python string format such as : "XY" or "YZ" or "XZ".

axis :		Is the axis where the center is located. For example, if the chosen plane is XZ, axis must be either X or Z, then the circle center will be located on the desired axis.

R :			Is the radius of the circle in cm. Radius can be either positive or negative

angle :	  Is the oriented angle (in degree) of this continuous piecewise circular trajectory. When angle is positive movement will be counter-clockwise, clockwise if negative.

## Parameter :

n :			Is an integer which is the maximum number of points that will describe the continuous piecewise circular trajectory with n <= 50.

dtheta :	Is a portion of the angle desired in radians such that :
$$
d_{theta} = \frac{2.|angle|.\pi}{360.n}
$$
Coord :	Is the list of points coordinates such that : 
$$
Coord = [[0,0,0],...,[X_k,Y_k,Z_k],...,[X_{n-1},Y_{n-1},Z_{n-1}]] \\
k = 0,...,n-1
$$


## Output :

***cir_mvt.json*** : json file with the following structure :

> ```json
> {'POINT_LIST': [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [-1, 3, 0], [-1, 4, 0], [-1, 5, 0], [-2, 5, 0], [-2, 6, 0], [-2, 7, 0], [-3, 7, 0], [-3, 8, 0], [-4, 8, 0], [-5, 8, 0], [-5, 9, 0], [-6, 9, 0], [-7, 9, 0], [-7, 10, 0], [-8, 10, 0], [-9, 10, 0], [-10, 10, 0]], 'NB_POINT': 21}
> ```

Note that coordinates values in this example are made with the following command :

```python
>>> cir_mvt('XY','X',10,90)
```

For better overview, if 2 consecutives iterations give the same coordinates points then there will be only one point considered. 

## Program structure :

1. Header

2. Library import

3. Function

   1. Description

   2. Parameters

   3. Computation

   4. json data structure creation

      

## Program backup :

```python
#!/usr/bin/env python3
# encoding: utf-8
# CHIEUX Romuald - ENSIL-ENSCI - MIX5A
#
#   ##############################################
#   # Circular trajectory for Neo-Farm challenge #
#   ##############################################

from math import *
import json

def cir_mvt(plane,axis,R,angle):
    # See README.md for all informations
    
    # Parameters
    n=50
    dtheta = abs(angle)*2*pi/(360*n)
    Coord = [[0,0,0]]
    
    # Computation
    
    for i in range(n-1):
        Cio = round(R*(cos((i+1)*dtheta)-1))
        Sio = round(R*sin((i+1)*dtheta))
        # XY Plane
        if plane.upper()=="XY" and axis.upper() == "X":
            if angle > 0:
                if Coord[-1] != [Cio,Sio,0]:
                    Coord.append([Cio,Sio,0])
            elif angle < 0:
                if Coord[-1] != [-Cio,Sio,0]:
                    Coord.append([-Cio,Sio,0])
        if plane.upper()=="XY" and axis.upper() == "Y":
            if angle > 0:
                if Coord[-1] != [Sio,-Cio,0]:
                    Coord.append([Sio,-Cio,0])
            elif angle < 0:
                if Coord[-1] != [Sio,Cio,0]:
                    Coord.append([Sio,Cio,0])

        # YZ Plane
        if plane.upper()=="YZ" and axis.upper() == "Y":
            if angle > 0:
                if Coord[-1] != [0,Cio,Sio]:
                    Coord.append([0,Cio,Sio])
            elif angle < 0:
                if Coord[-1] != [0,-Cio,Sio]:
                    Coord.append([0,-Cio,Sio])

        if plane.upper()=="YZ" and axis.upper() == "Z":
            if angle > 0:
                if Coord[-1] != [0,Sio,-Cio]:
                    Coord.append([0,Sio,-Cio])
            elif angle < 0:
                if Coord[-1] != [0,Sio,Cio]:
                    Coord.append([0,Sio,Cio])
                
        # XZ Plane
        if plane.upper()=="XZ" and axis.upper() == "Z":
            if angle > 0:
                if Coord[-1] != [Sio,0,Cio]:
                    Coord.append([Sio,0,Cio])
            elif angle < 0:
                if Coord[-1] != [Sio,0,-Cio]:
                    Coord.append([Sio,0,-Cio])

        if plane.upper()=="XZ" and axis.upper() == "X":
            if angle > 0:
                if Coord[-1] != [-Cio,0,Sio]:
                    Coord.append([-Cio,0,Sio])
            elif angle < 0:
                if Coord[-1] != [Cio,0,Sio]:
                    Coord.append([Cio,0,Sio])

    #json data structure
    data = {}
    data["NB_POINT"]=len(Coord)
    data["POINT_LIST"]=Coord

    #output
    return data
```

