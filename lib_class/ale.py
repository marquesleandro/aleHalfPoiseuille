# ==========================================
# Code created by Leandro Marques at 02/2019
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to apply ALE scheme

import sys
import numpy as np


def rotate(_npoints, _t, _dirichlet_pts):
 # vx = r*cos(wt), where w = 2pi/T
 # vy = r*sin(wt), where w = 2pi/T

 r = 0.2 # Amplitude
 T = 16.0   # Partition
 w = 2.0*np.pi/T

 vx_Ale = np.zeros([_npoints,1], dtype = float)
 vy_Ale = np.zeros([_npoints,1], dtype = float)


 for i in range(0, _npoints): 
  vx_Ale[i] = r*np.cos(w*_t)
  vy_Ale[i] = r*np.sin(w*_t)


 # Boundary Nodes
 for i in range(0, len(_dirichlet_pts)):
  v1 = _dirichlet_pts[i][1] - 1
  v2 = _dirichlet_pts[i][2] - 1

  vx_Ale[v1] = 0.0
  vy_Ale[v2] = 0.0



 return vx_Ale, vy_Ale
