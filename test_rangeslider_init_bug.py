import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

def test_issue_reproduction():
    """Test that RangeSlider can be initialized with custom values."""
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    
    # Create axes for the range slider
    ax_slider = plt.axes([0.2, 0.1, 0.5, 0.03])
    
    # Try to create a RangeSlider with custom initial values
    # This should work but fails due to the bug in set_val method
    initial_values = [0.3, 0.7]
    
    try:
        range_slider = widgets.RangeSlider(
            ax_slider, 'Range', 0.0, 1.0, 
            valinit=initial_values
        )
        
        # Check if the slider was initialized with the correct values
        actual_values = range_slider.val
        
        # This assertion should pass but will fail due to the bug
        # The bug prevents proper initialization of the slider values
        assert np.allclose(actual_values, initial_values, atol=1e-10), \
            f"Expected {initial_values}, got {actual_values}"
            
    except Exception as e:
        # If there's an exception during initialization, that's also a bug
        assert False, f"RangeSlider initialization failed: {e}"
    
    plt.close(fig)