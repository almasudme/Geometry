import pyvoro as voro
import json
import random
import numpy as np
cube_side = 10
cube_gap = 2
n_cubex = 1
n_cubey = 1
n_cubez = 1
n_voronoi_centers = 2

cubes=[]
def random_center_generator(limit_x,limit_y,limit_z):
   
    ret = np.random.rand(n_voronoi_centers,3)*cube_side
    ret = ret.tolist()
    for i_ret , point in enumerate(ret):
        ret[i_ret][0] = ret[i_ret][0]+limit_x[0]
        ret[i_ret][1] = ret[i_ret][1]+limit_y[0]
        ret[i_ret][2] = ret[i_ret][2]+limit_z[0]
    return ret
for i_cubex in range(n_cubex):
    for i_cubey in range(n_cubey):
        for i_cubez in range(n_cubez):
            limit_x = [(cube_gap+cube_side)*i_cubex+0.0, (cube_gap+cube_side)*i_cubex+10.0]
            limit_y = [(cube_gap+cube_side)*i_cubey+0.0, (cube_gap+cube_side)*i_cubey+10.0]
            limit_z = [(cube_gap+cube_side)*i_cubez+0.0, (cube_gap+cube_side)*i_cubez+10.0]
            voro_centroids = random_center_generator(limit_x,limit_y,limit_z)
            print(voro_centroids)
            voro_data = voro.compute_voronoi(
            voro_centroids, # point positions
            [limit_x, limit_y, limit_z], # limits
            2.0, # block size

            )
            cubes.append(voro_data)

with open('voronoi_data_temp.json', 'w') as f:
    json.dump(cubes,f,indent=2 )
