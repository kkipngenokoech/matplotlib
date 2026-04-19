import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider

def test_issue_reproduction():
    """Test that RangeSlider can be initialized with custom valinit values."""
    fig, ax = plt.subplots()
    
    # Create some dummy data
    img = np.random.rand(10, 10)
    
    # Create a slider axis
    slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
    
    # This should work but currently fails with IndexError: index 4 is out of bounds for axis 0 with size 4
    # The error occurs in RangeSlider.set_val method when trying to access xy[4]
    slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max(), valinit=[0.0, 0.0])
    
    # If we get here without error, the bug is fixed
    assert slider.val == (0.0, 0.0)
    
    plt.close(fig)