# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 14:41:24 2015

@author: ecksjoh
"""
import os,sys
import numpy as np
from vispy import app,gloo,scene,visuals
from vispy.scene.visuals import create_visual_node
from vispy.visuals.transforms import STTransform,MatrixTransform

#from vispy.io import read_mesh,load_data_file,load_crate

#from vispy.util.transforms import perspective,translate,rotate


"""
This example demonstrates how to create visuals.
"""

class dummy(scene.visuals.Cube):
    """
    creates a custom draft to demonstrate what is not working
    """
    def __init__(self,view,x,y,z,face_color,edge_color):
        scene.visuals.Cube.__init__(self,(x,y,z),color=face_color,edge_color=edge_color,parent=view)

    def trafo(self,x=0.,y=0.,z=0.,angle=0.,al=0.,be=0.,ga=0.):
        #Not Working
        self.transform = MatrixTransform()
        
        self.transform = self.transform.translate([x,y,z])
        self.transform = self.transform.rotate(angle,[al,be,ga])

#Volume = create_visual_node(visuals.VolumeVisual)

#Arrow = create_visual_node(visuals.ArrowVisual)
#Axis = create_visual_node(visuals.AxisVisual)
#Box = create_visual_node(visuals.BoxVisual)
#ColorBar = create_visual_node(visuals.ColorBarVisual)
#Compound = create_visual_node(visuals.CompoundVisual)
#Ellipse = create_visual_node(visuals.EllipseVisual)
#GridLines = create_visual_node(visuals.GridLinesVisual)
#Histogram = create_visual_node(visuals.HistogramVisual)
#Image = create_visual_node(visuals.ImageVisual)
#Isocurve = create_visual_node(visuals.IsocurveVisual)
#Isoline = create_visual_node(visuals.IsolineVisual)
#Isosurface = create_visual_node(visuals.IsosurfaceVisual)
#Line = create_visual_node(visuals.LineVisual)
#LinePlot = create_visual_node(visuals.LinePlotVisual)
#Markers = create_visual_node(visuals.MarkersVisual)
#Mesh = create_visual_node(visuals.MeshVisual)
#Plane = create_visual_node(visuals.PlaneVisual)
#Polygon = create_visual_node(visuals.PolygonVisual)
#Rectangle = create_visual_node(visuals.RectangleVisual)
#RegularPolygon = create_visual_node(visuals.RegularPolygonVisual)
#ScrollingLines = create_visual_node(visuals.ScrollingLinesVisual)
#Spectrogram = create_visual_node(visuals.SpectrogramVisual)
#SurfacePlot = create_visual_node(visuals.SurfacePlotVisual)
#Text = create_visual_node(visuals.TextVisual)

class mbTube(scene.visuals.Tube):
    """
    creates a custom tube:
        create_visual_node(visuals.TubeVisual)
        
    :param view: the view as obtained by call to e.g. scene.SceneCanvas().central_widget.add_view()
    :param path: An array of (x, y, z) points describing the path along which the tube will be extruded.
    :param radius: the radius
    :param face_color: the faces color
    :param tube_points: The number of points in the circle, default is 16

    """
    def __init__(self,view,radius,path,face_color,tube_points=16,closed=True):
        """        
        points : ndarray
            An array of (x, y, z) points describing the path along which the
            tube will be extruded.
        radius : float
            The radius of the tube. Defaults to 1.0.
        closed : bool
            Whether the tube should be closed, joining the last point to the
            first. Defaults to False.
        color : Color | ColorArray
            The color(s) to use when drawing the tube. The same color is
            applied to each vertex of the mesh surrounding each point of
            the line. If the input is a ColorArray, the argument will be
            cycled; for instance if 'red' is passed then the entire tube
            will be red, or if ['green', 'blue'] is passed then the points
            will alternate between these colours. Defaults to 'purple'.
        tube_points : int
            The number of points in the circle-approximating polygon of the
            tube's cross section. Defaults to 8.
        shading : str | None
            Same as for the `MeshVisual` class. Defaults to 'smooth'.
        vertex_colors: ndarray | None
            Same as for the `MeshVisual` class.
        face_colors: ndarray | None
            Same as for the `MeshVisual` class.
        mode : str
            Same as for the `MeshVisual` class. Defaults to 'triangles'.
        """
        super(mbTube, self).__init__(radius=radius,points=path,color=face_color,tube_points=tube_points,closed=closed,parent=view)

    def trafo(self,x=0.,y=0.,z=0.,angle=0.,al=0.,be=0.,ga=0.):
        self.transform = STTransform(translate=[x,y,z])

class mbFrame(scene.visuals.XYZAxis):
    """
    creates a custom Body Frame, a 3D axis for indicating coordinate system orientation. Axes are x=red, y=green, z=blue.
        create_visual_node(visuals.XYZAxisVisual)

    maybee this will become the subvisual in every mbVisual

    :param view: the view as obtained by call to e.g. scene.SceneCanvas().central_widget.add_view()

    """
    def __init__(self,view,*args, **kwargs):
        super(mbFrame, self).__init__(parent=view,*args, **kwargs)

    def trafo(self,x=0.,y=0.,z=0.,angle=0.,al=0.,be=0.,ga=0.):
        self.transform = STTransform(translate=[x,y,z])

class mbCube(scene.visuals.Cube):
    """
    creates a custom cube:
        create_visual_node(visuals.CubeVisual)

    :param view: the view as obtained by call to e.g. scene.SceneCanvas().central_widget.add_view()
    :param a: first edge lenght (in x direction)
    :param b: second edge lenght (in y direction)
    :param c: third edge lenght (in z direction)
    :param face_color: the faces color
    :param edge_color: the edge (wire) color

    """
    def __init__(self,view,a,b,c,face_color,edge_color):
        super(mbCube,self).__init__((a,b,c),color=face_color,edge_color=edge_color,parent=view)

    def trafo(self,x=0.,y=0.,z=0.,angle=0.,al=0.,be=0.,ga=0.):
        self.transform = STTransform(translate=[x,y,z])

class Cubo(scene.visuals.Cube):
    """
    creates a custom draft to demonstrate what is not working
    """
    def __init__(self,view,x,y,z,face_color,edge_color):
        super(Cubo,self).__init__(size=(x,y,z),color=face_color,edge_color=edge_color,parent=view)


class mbSphere(scene.visuals.Sphere):
    """
    creates a custom sphere:
        create_visual_node(visuals.SphereVisual)

    :param view: the view as obtained by call to e.g. scene.SceneCanvas().central_widget.add_view()
    :param radius: the radius
    :param face_color: the faces color
    :param edge_color: the edge (wire) color

        
        #sphere1 = scene.visuals.Sphere(radius=1, method='latitude', parent=view.scene,
        #                               edge_color='black')
        
        #sphere2 = scene.visuals.Sphere(radius=1, method='ico', parent=view.scene,
        #                               edge_color='black')
    
    """
    def __init__(self,view,radius,face_color,edge_color):
        super(mbSphere,self).__init__(radius,color=face_color,edge_color=edge_color,parent=view,method='ico')

    def trafo(self,x=0.,y=0.,z=0.,angle=0.,al=0.,be=0.,ga=0.):
        self.transform = STTransform(translate=[x, y, z])

canvas = scene.SceneCanvas(keys='interactive', bgcolor='white',
                           size=(800, 600), show=True)

view = canvas.central_widget.add_view()
view.camera = 'arcball'

body_frame = mbFrame(view.scene)

#cube = dummy(view.scene,2,3,1,'red','black')
#cube.trafo(x=-0.5,y=1.5)

#view,a,b,c,face_color,edge_color

#cube1 = Cubo(view.scene,2,3,1,'red','black')

cube = mbCube(view.scene,2,3,1,'red','black')

sphere = mbSphere(view.scene,2,'blue','black')

cube.trafo(x=4,y=-2)

cube.trafo(x=-2,y=4)
#
sphere.trafo(x=2.5,y=1.,z=2)


view.camera.set_range(x=[-3, 3])

if __name__ == '__main__' and sys.flags.interactive == 0:
    

    
    canvas.app.run()
    

    
    

#__root__ = os.path.realpath(os.path.join(os.path.dirname(__file__),".")) #"../"
#__icon_path__ = os.path.join(__root__,"mesh")
#
#

#
## Read cube data
##positions, faces, normals, texcoords = read_mesh(os.path.join(__root__,'cube.obj'))
##colors = np.random.uniform(0,1,positions.shape).astype('float32')
#
#def checkerboard(grid_num=8, grid_size=32):
#    row_even = grid_num // 2 * [0, 1]
#    row_odd = grid_num // 2 * [1, 0]
#    Z = np.row_stack(grid_num // 2 * (row_even, row_odd)).astype(np.uint8)
#    return 255 * Z.repeat(grid_size, axis=0).repeat(grid_size, axis=1)
#
#class Canvas(scene.SceneCanvas):
#    def __init__(self,name):
#        scene.SceneCanvas.__init__(self,title=name,bgcolor='white',size=(512, 512),keys='interactive',show=True)
#
#        self.timer = app.Timer('auto', self.on_timer)
#
#        # Build view, model, projection & normal
#        self.view = self.central_widget.add_view()
#        self.view.camera = 'arcball'
#
#        self.myc = mbCube(self.view)
#
#        self.view.camera.set_range(x=[-3, 3])
#
#        self.init_transforms()
#
#        self.timer.start()
#
#        self.show()
#
#    def on_draw(self, event):
#        gloo.clear(color=True, depth=True)
#        #self.program.draw('triangles', self.indices)
#        self.draw()
#
#
#    def on_resize(self, event):
#        self.activate_zoom()
#
#    def activate_zoom(self):
#        gloo.set_viewport(0, 0, *self.physical_size)
#        #projection = perspective(45.0, self.size[0] / float(self.size[1]),2.0, 10.0)
#        #self.program['projection'] = projection
##
#    def on_timer(self, event):
#        self.theta += .5
#        self.phi += .5
#        #self.myc.
#        #self.myc['u_model'] = np.dot(rotate(self.theta, (0, 0, 1)),
#                                       #rotate(self.phi, (0, 1, 0)))
#        self.update()
#
#    def init_transforms(self):
#        self.view       = np.eye(4,dtype=np.float32)
#        self.model      = np.eye(4,dtype=np.float32)
#        self.projection = np.eye(4,dtype=np.float32)
#
#        self.theta = 0
#        self.phi = 0
#
#        self.myc.transform = STTransform(translate=[-2.5, 0, 0])
#
#        #translate(self.view, )
#        #self.myc['u_model'] = self.model
#        #self.myc['u_view'] = self.view
#
#    def update_transforms(self,event):
#        self.theta += .5
#        self.phi += .5
#        self.model = np.eye(4, dtype=np.float32)
#        rotate(self.model, self.theta, 0,0,1)
#        rotate(self.model, self.phi,   0,1,0)
#        #self.program['u_model'] = self.model
#        self.update()
#
#
#if __name__ == '__main__' and sys.flags.interactive == 0:
#
#    c = Canvas('test')
#    c.show()
#    c.app.run()

## Things to learn
##myapp = app.Application()
#
##app.Canvas
#
##app.KeyEvent
##app.MouseEvent
#
##app.Timer()
#
###window/layout
##app.qt.QWidget()
##app.qt.QGridLayout()
##app.qt.QtSceneCanvas()
##
###dialogs
##app.qt.QtGui.QInputDialog.getItem() #dropdown and select
##app.qt.QtGui.QInputDialog.getInt() #get number sindide range
###app.qt.QtGui.QDialogButtonBox
##app.qt.QtGui.QFileDialog.getOpenFileName()
#
##visuals.BaseVisual.
#
##visuals.AxisVisual.view()
##visuals.GridLinesVisual.view()
##visuals.ArrowVisual
##visuals.PlaneVisual
##
###2d
###visuals.BoxVisual
##visuals.EllipseVisual
##visuals.RectangleVisual
##
###3d
##visuals.SphereVisual
##visuals.CubeVisual
##visuals.MeshVisual
##visuals.TubeVisual
##
##visuals.VolumeVisual
##
##visuals.CompoundVisual
##
##glsl.colormaps
##glsl.antialias
##glsl.markers
##glsl.collections
##
##gloo.VertexBuffer
##
##gloo.FrameBuffer
##
##gloo.IndexBuffer
##if  __name__ == "__main__":
##    myapp.run()
##
##
##    myapp.quit()