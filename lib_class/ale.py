# ==========================================
# Code created by Leandro Marques at 02/2019
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to apply ALE scheme

import sys
import numpy as np


def rotate(_npoints, _x, _y, _dt, _t, _dirichlet_pts):
 # x = r*cos(wt), where w = 2pi/T
 # y = r*sin(wt), where w = wpi/T

 r = 0.001
 T = 8.0
 w = 2.0*np.pi/T

 x_Ale = np.zeros([_npoints,1], dtype = float)
 y_Ale = np.zeros([_npoints,1], dtype = float)

 vx_Ale = np.zeros([_npoints,1], dtype = float)
 vy_Ale = np.zeros([_npoints,1], dtype = float)


 for i in range(0, _npoints): 
  x_Ale[i] = r*np.cos(w*_t)
  y_Ale[i] = r*np.cos(w*_t)

  vx_Ale[i] = (x_Ale[i] - _x[i])/_dt
  vy_Ale[i] = (y_Ale[i] - _y[i])/_dt


 # Boundary Nodes
 for i in range(0, len(_dirichlet_pts)):
  v1 = _dirichlet_pts[i][1] - 1
  v2 = _dirichlet_pts[i][2] - 1

  x_Ale[v1] = _x[v1]
  x_Ale[v2] = _x[v2]

  y_Ale[v1] = _y[v1]
  y_Ale[v2] = _y[v2]

  vx_Ale[v1] = 0.0
  vy_Ale[v2] = 0.0

 return x_Ale, y_Ale, vx_Ale, vy_Ale
