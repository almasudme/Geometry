#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/mir/CMS_Lab/trl_study/scripts')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 100)
Cylinder_1 = geompy.MakeCylinderRHA(100, 50, 95*math.pi/180.)
geomObj_1 = geompy.MakeCommonList([Box_1, Cylinder_1], True)
geomObj_2 = geompy.MakeCutList(Box_1, [geomObj_1], True)
Box_1_vertex_21 = geompy.GetSubShape(Box_1, [21])
Box_1_edge_20 = geompy.GetSubShape(Box_1, [20])
Cylinder_2 = geompy.MakeCylinder(Box_1_vertex_21, Box_1_edge_20, 100, 150)
Common_1 = geompy.MakeCommonList([Box_1, Cylinder_1], True)
Common_2 = geompy.MakeCommonList([Box_1, Cylinder_2], True)
Cut_1 = geompy.MakeCutList(Box_1, [Common_1, Common_2], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudyInFather( Box_1, Box_1_vertex_21, 'Box_1:vertex_21' )
geompy.addToStudyInFather( Box_1, Box_1_edge_20, 'Box_1:edge_20' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )
geompy.addToStudy( Common_1, 'Common_1' )
geompy.addToStudy( Common_2, 'Common_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
