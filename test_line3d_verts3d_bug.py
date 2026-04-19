import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D

def test_issue_reproduction():
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # First, create Line3D with numpy arrays (this works)
    x_array = np.array([1, 2, 3])
    y_array = np.array([1, 2, 3])
    z_array = np.array([1, 2, 3])
    
    line = Line3D(x_array, y_array, z_array)
    ax.add_line(line)
    
    # Try to draw - this should work
    fig.canvas.draw()
    
    # Now create another Line3D with scalar values after the array operation
    # This is where the bug manifests - the _verts3d attribute gets corrupted
    x_scalar = 1
    y_scalar = 2  
    z_scalar = 3
    
    line2 = Line3D(x_scalar, y_scalar, z_scalar)
    ax.add_line(line2)
    
    # This should trigger the AttributeError: 'Line3D' object has no attribute '_verts3d'
    # when the draw method tries to access self._verts3d
    fig.canvas.draw()
    
    plt.close(fig)