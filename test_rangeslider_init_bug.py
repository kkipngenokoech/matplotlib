import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import numpy as np

def test_issue_reproduction():
    """Test that RangeSlider can be initialized with custom values."""
    fig, ax = plt.subplots()
    
    # Create a RangeSlider with custom initial values
    ax_slider = plt.axes([0.2, 0.1, 0.5, 0.03])
    
    # Try to initialize RangeSlider with custom values [0.3, 0.7]
    slider = RangeSlider(ax_slider, 'Range', 0.0, 1.0, valinit=(0.3, 0.7))
    
    # The bug prevents proper initialization, so the values won't match
    # what we requested. This assertion should fail on buggy code.
    actual_val = slider.val
    expected_val = (0.3, 0.7)
    
    # This should pass once the bug is fixed
    assert np.allclose(actual_val, expected_val, atol=1e-10), f"Expected {expected_val}, got {actual_val}"
    
    plt.close(fig)