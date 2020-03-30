# ==========================================
# Code created by Leandro Marques at 03/2019
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to remesh domain

import sys
import numpy as np


def remeshing(_npoints, _nelem, _IEN, _x, _y, _dxmax, _neighbors_nodes, _neighbors_elements):
 for e in range(0, len(_IEN)):
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]

  x1 = np.sqrt((_x[v1] - x[v2])**2)
  x2 = np.sqrt((_x[v2] - x[v3])**2)
  x3 = np.sqrt((_x[v3] - x[v1])**2)

  y1 = np.sqrt((_y[v1] - y[v2])**2)
  y2 = np.sqrt((_y[v2] - y[v3])**2)
  y3 = np.sqrt((_y[v3] - y[v1])**2)

  edge1 = np.sqrt(x1**2 + y1**2)
  edge2 = np.sqrt(x2**2 + y2**2)
  edge3 = np.sqrt(x3**2 + y3**2)

  if edge1 > _dxmax:
   _npoints = _npoints + 1
   vnew = _npoints

   xnew = (_x[v1] + _x[v2])/2.0
   ynew = (_y[v1] + _y[v2])/2.0

   _x.vstack(xnew)
   _y.vstack(ynew)

   IEN1 = [v1,vnew,v3]
   IEN2 = [v2,v3,vnew]
   np.delete(_IEN,e,0)
   _IEN = np.vstack((_IEN,IEN1))
   _IEN = np.vstack((_IEN,IEN2))

   _neighbors_nodes[vnew] = []
   _neighbors_nodes[vnew].extend(IEN1)
   _neighbors_nodes[vnew].extend(IEN2)

   _neighbors_nodes[v1].remove(v2)
   _neighbors_nodes[v2].remove(v1)
   _neighbors_nodes[v1].extend(vnew)
   _neighbors_nodes[v2].extend(vnew)
   _neighbors_nodes[v1] = list(set(_neighbors_nodes[v1]))
   _neighbors_nodes[v2] = list(set(_neighbors_nodes[v2]))
   _neighbors_nodes[vnew] = list(set(_neighbors_nodes[vnew]))

   _nelem = len(_IEN)
 
   _neighbors_elements[v1].remove(e)
   _neighbors_elements[v2].remove(e)
   _neighbors_elements[v3].remove(e)
   _neighbors_elements[v1].append(_nelem)
   _neighbors_elements[vnew].append(_nelem)
   _neighbors_elements[v3].append(_nelem)
   _neighbors_elements[v2].append(_nelem+1)
   _neighbors_elements[v3].append(_nelem+1)
   _neighbors_elements[vnew].append(_nelem+1)
   _neighbors_elements[v1] = list(set(_neighbors_elements[v1]))
   _neighbors_elements[v2] = list(set(_neighbors_elements[v2]))
   _neighbors_elements[v3] = list(set(_neighbors_elements[v3]))
   _neighbors_elements[vnew] = list(set(_neighbors_elements[vnew]))


---------------------continuar elif para edge2 e edge3 ------------------------------------

def Laplacian_smoothing(_neighbors_nodes, _npoints, _x, _y, _dt):
 vx_laplaciansmooth = np.zeros([_npoints,1], dtype = float)
 vy_laplaciansmooth = np.zeros([_npoints,1], dtype = float)
 
 for i in range(0,_npoints):
  num_nghb = len(_neighbors_nodes[i])
  x_distance = 0.0
  y_distance = 0.0
  
  for j in range(0,num_nghb):
   node_nghb = _neighbors_nodes[i][j]

   x_distance = x_distance + (1.0/num_nghb)*(_x[node_nghb] - _x[i])
   y_distance = y_distance + (1.0/num_nghb)*(_y[node_nghb] - _y[i])

  vx_laplaciansmooth[i] = x_distance/_dt
  vy_laplaciansmooth[i] = y_distance/_dt

 return vx_laplaciansmooth, vy_laplaciansmooth


def Velocity_smoothing(_neighbors_nodes, _npoints, _vx, _vy):
 vx_velocitysmooth = np.zeros([_npoints,1], dtype = float)
 vy_velocitysmooth = np.zeros([_npoints,1], dtype = float)
 
 for i in range(0,_npoints):
  num_nghb = len(_neighbors_nodes[i])
  
  for j in range(0,num_nghb):
   node_nghb = _neighbors_nodes[i][j]

   vx_velocitysmooth = vx_velocitysmooth + (1.0/num_nghb)*_vx[node_nghb]
   vy_velocitysmooth = vy_velocitysmooth + (1.0/num_nghb)*_vy[node_nghb]


 return vx_velocitysmooth, vy_velocitysmooth


