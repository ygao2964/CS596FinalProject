import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys
from opensimplex import OpenSimplex


class Terrain(object):
    def __init__(self, speed, height, noiseType, step):
        """
        Initialize the graphics window and mesh
        """

        # parameters that change the shape of the wave
        self.speed = speed
        self.height = height
        self.noiseType = noiseType
        self.nsteps = step

        # setup the view window
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget()
        self.window.setWindowTitle('openGL: Wave Movement')
        self.window.setGeometry(0, 110, 960, 540)
        self.window.show()
        self.window.setCameraPosition(distance=30, elevation=10)

        # constants and arrays
        self.ypoints = range(-40, 40, self.nsteps)
        self.xpoints = range(-40, 40, self.nsteps)
        self.nfaces = len(self.ypoints)
        self.offset = 0

        # noise object in OpenSimplex
        self.tmp = OpenSimplex()

        # create the veritices array based on given type
        if self.noiseType == '2D':
            verts = np.array([
                [
                    x, y, 1.5 * self.tmp.noise2d(x=n / self.height, y=m / self.height)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)

        if self.noiseType == '3D':
            verts = np.array([
                [
                    x, y, 1.5 * self.tmp.noise3d(x=n / self.height, y=m / self.height, z=m / self.height)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)
        
        if self.noiseType == '4D':
            verts = np.array([
                [
                    x, y, 1.5 * self.tmp.noise4d(x=n / self.height, y=m / self.height, z=m / self.height, w=n / self.height)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)


        # create the faces and colors arrays
        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0, 0, 0, 0])
                colors.append([0, 0, 0, 0])

        faces = np.array(faces)
        colors = np.array(colors)

        # create the mesh item
        self.mesh1 = gl.GLMeshItem(
            vertexes=verts,
            faces=faces, faceColors=colors,
            smooth=True, drawEdges=True,
        )
        self.mesh1.setGLOptions('additive')
        self.window.addItem(self.mesh1)

    def update(self):
        """
        update the mesh and the noise 
        """

        #update the veritices array based on given noise type
        if self.noiseType == '2D':
            verts = np.array([
                [
                    x, y, 2.5 * self.tmp.noise2d(x=n / self.height + self.offset, y=m / self.height + self.offset)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)
        
        if self.noiseType == '3D':
            verts = np.array([
                [
                    x, y, 2.5 * self.tmp.noise3d(x=n / self.height + self.offset, y=m / self.height + self.offset, z=m / self.height + self.offset)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)

        if self.noiseType == '4D':
            verts = np.array([
                [
                    x, y, 2.5 * self.tmp.noise4d(x=n / self.height + self.offset, y=m / self.height + self.offset, z=m / self.height + self.offset, w=n / self.height + self.offset)
                ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
            ], dtype=np.float32)

        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0.1 * n / self.nfaces, 0.5 - 0.1 * n / self.nfaces, 1 - 0.1 * m / self.nfaces, 0.7])
                colors.append([0.1 * n / self.nfaces, 0.5 - 0.1 * n / self.nfaces, 1 - 0.1 * m / self.nfaces, 0.7])
                #slightly change the color while moving, making it looks more like wave

        faces = np.array(faces, dtype=np.uint32)
        colors = np.array(colors, dtype=np.float32)

        self.mesh1.setMeshData(
            vertexes=verts, faces=faces, faceColors=colors
        )
        self.offset -= self.speed

    def start(self):
        """
        get the graphics window start
        """
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def animation(self):
        """
        using update method to simulate animation
        """
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.start()
        self.update()


if __name__ == '__main__':
    """
        get inputs from command line and start the animation
    """

    #this parameter change the speed of the wave movement
    speed_input = input('Adjust the moving speed of the wave: (from 0.01 to 0.50):\n')
    # Type: float
    speed_input = float(speed_input)
    
    #this parameter change the height of each wave 
    height_input = input('Adjust the height of each wave: (from 1 to 10):\n')
    # Type: int
    height_input = 10/int(height_input) 
    
    #this parameter change the noise type that is used in OpenSimplex
    # Type: string
    noiseType_input = input('Change the noise type: (choose from 2D, 3D, 4D):\n')
    
    #this parameter change the width of each wave
    step_input = input('Adjust the width of each wave: (from 1 to 5):\n')
    # Type: Int
    step_input = int(step_input)

    t = Terrain(speed=speed_input, height=height_input, noiseType=noiseType_input, step= step_input)
    t.animation()

