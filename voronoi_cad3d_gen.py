#!/usr/bin/env python
def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _z_list = [vertex [2] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     _z = sum(_z_list) / _len
     return(_x, _y, _z)

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome
import json
salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/mir/CMS_Lab/voro')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
CYL_BASE_RADIUS = 0.5
CYL_HEIGHT=1


with open('/home/mir/CMS_Lab/voro/voronoi_data_temp.json') as f:
  voro_cubes = json.load(f)




geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)


####
def create_voronoi_cube(voro_data,cube_id):
  for i_region,region in enumerate(voro_data):
      region_center=voro_data[i_region]['original']
      region_center_vertex=geompy.MakeVertex(region_center[0],region_center[1],region_center[2])
      geompy.addToStudy( region_center_vertex, f'cube_{cube_id}_region_{i_region}_center_vertex' )
      vertices = []
      print('region vertices:')
      for i_vertex,vertex in enumerate(region['vertices']):
          
          print("Creating vertex",i_vertex,vertex)
          x,y,z=vertex[0],vertex[1],vertex[2]
          temp_vertex=geompy.MakeVertex(x,y,z)
          vertices.append(temp_vertex)        
          geompy.addToStudy( vertices[i_vertex], f'cube_{cube_id}_vertex_{i_region}_{i_vertex}' )
      print(f'region vertices={region["vertices"]}')

      faces = region['faces']
      lines=[]
      line_count=0
      cyl_count = 0
      print('face vertices in order:')   
      for i_face,face in enumerate(faces):
          print(i_face,face['vertices'])

          adjacent_cell = face['adjacent_cell']
          print(adjacent_cell)
          
          face_vertices_coordinates =[] 
          face_lines=[]        
          for i_face_vertex in range(len(face['vertices'])-1):
              line_name = f'cube_{cube_id}_Line_{line_count}'
              vertices_index_from = face['vertices'][i_face_vertex]
              vertices_index_to = face['vertices'][i_face_vertex+1]
              vertex_coordinate_from = vertices[vertices_index_from]
              vertex_coordinate_to = vertices[vertices_index_to]
              face_vertices_coordinates.append(region['vertices'][vertices_index_from])
              temp_line = geompy.MakeLineTwoPnt(vertex_coordinate_from, vertex_coordinate_to)
              face_lines.append(temp_line)
              
              geompy.addToStudy( temp_line, line_name )
              if adjacent_cell >-1:
                print(f'{line_name}')
              line_count +=1
          line_name = f'cube_{cube_id}_Line_{line_count}'
          
          vertices_index_from = face['vertices'][-1]
          vertices_index_to = face['vertices'][0]
          face_vertices_coordinates.append(region['vertices'][vertices_index_from])
          face_centroid = centroid(face_vertices_coordinates)
          
          temp_line = geompy.MakeLineTwoPnt(vertices[vertices_index_from], vertices[vertices_index_to])
          face_lines.append(temp_line)
          geompy.addToStudy( temp_line, line_name )
          lines.append(face_lines)
          line_count +=1
          
          print(f'{line_name}')
          print(f'face vertices coordinates = {face_vertices_coordinates}, centroid = {face_centroid}')
          print(face_lines)
          Face = geompy.MakeFaceWires(face_lines, 1)
          geompy.addToStudy( Face, f'cube_{cube_id}_face_{i_face}' )
          if adjacent_cell >-1:
            cylinder_base_center_vertex=geompy.MakeVertex(face_centroid[0],face_centroid[1],face_centroid[2])
            geompy.addToStudy( cylinder_base_center_vertex, f'cyliner_base_center_cube_{cube_id}_{i_region}_{cyl_count}' )
            cyl_count +=1
            Vector_Normal = geompy.GetNormal(Face, cylinder_base_center_vertex)
            geompy.addToStudy( Vector_Normal, f'cube_{cube_id}_vector_normal_{i_face}' )
            Cylinder = geompy.MakeCylinder(cylinder_base_center_vertex, Vector_Normal, CYL_BASE_RADIUS/2, CYL_HEIGHT/2)
            geompy.addToStudy( Cylinder, f'Cylinder_cube_{cube_id}_{i_region}_{cyl_count}' )
      break
    
for i_voro_cube,voro_cube in enumerate(voro_cubes):
  create_voronoi_cube(voro_cube,i_voro_cube)            

        
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
