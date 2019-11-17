#!/usr/bin/env python3
# encoding: utf-8
# CHIEUX Romuald - ENSIL-ENSCI - MIX5A
#
#   ##############################################
#   # Circular trajectory for Neo-Farm challenge #
#   ##############################################

from math import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import json
import numpy as np


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
    

