import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

def test_issue_reproduction():
    """Test that RangeSlider can be initialized with custom values."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Create a simple plot area for the slider
    slider_ax = plt.axes([0.2, 0.02, 0.5, 0.03])
    
    # Try to create RangeSlider with custom initial values
    # This should work but currently fails due to the bug
    initial_values = (0.3, 0.7)
    range_slider = widgets.RangeSlider(
        slider_ax, 'Range', 0.0, 1.0, 
        valinit=initial_values
    )
    
    # Verify that the slider was initialized with the correct values
    current_val = range_slider.val
    
    # This assertion should pass but will fail due to the bug
    # The bug prevents proper initialization with custom values
    assert abs(current_val[0] - initial_values[0]) < 0.01, f"Expected {initial_values[0]}, got {current_val[0]}"
    assert abs(current_val[1] - initial_values[1]) < 0.01, f"Expected {initial_values[1]}, got {current_val[1]}"
    
    plt.close(fig)