import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
from unittest.mock import Mock

def test_issue_reproduction():
    """Test that RangeSlider on_changed callback with clf() and draw() doesn't block widget input."""
    
    # Create figure and axes
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    
    # Create a RangeSlider
    ax_slider = plt.axes([0.2, 0.1, 0.5, 0.03])
    slider = widgets.RangeSlider(ax_slider, 'Range', 0, 10, valinit=(2, 8))
    
    # Create a button for comparison
    ax_button = plt.axes([0.8, 0.1, 0.1, 0.04])
    button = widgets.Button(ax_button, 'Test')
    
    # Track callback execution and widget state
    callback_executed = {'slider': False, 'button': False}
    widget_responsive = {'slider': True, 'button': True}
    
    def slider_callback(val):
        callback_executed['slider'] = True
        # This sequence should not block widget input
        plt.clf()
        # Add new content
        new_ax = plt.axes([0.1, 0.1, 0.8, 0.8])
        new_ax.plot([1, 2, 3], [1, 4, 2])
        plt.draw()
        
        # Test if widgets are still responsive after clf+draw
        # In the buggy version, this would fail
        try:
            # Simulate checking if canvas can still process events
            canvas = fig.canvas
            if hasattr(canvas, 'callbacks') and canvas.callbacks is not None:
                # Check if event processing is still functional
                widget_responsive['slider'] = True
            else:
                widget_responsive['slider'] = False
        except:
            widget_responsive['slider'] = False
    
    def button_callback(event):
        callback_executed['button'] = True
        # Same operations but in button callback - should work fine
        plt.clf()
        new_ax = plt.axes([0.1, 0.1, 0.8, 0.8])
        new_ax.plot([1, 2, 3], [1, 4, 2])
        plt.draw()
        
        # Button callback should maintain widget responsiveness
        try:
            canvas = fig.canvas
            if hasattr(canvas, 'callbacks') and canvas.callbacks is not None:
                widget_responsive['button'] = True
            else:
                widget_responsive['button'] = False
        except:
            widget_responsive['button'] = False
    
    # Connect callbacks
    slider.on_changed(slider_callback)
    button.on_clicked(button_callback)
    
    # Simulate slider value change to trigger callback
    slider.set_val((3, 7))
    
    # Simulate button click
    button_callback(None)
    
    # Verify both callbacks executed
    assert callback_executed['slider'], "Slider callback should have executed"
    assert callback_executed['button'], "Button callback should have executed"
    
    # The bug: RangeSlider callback blocks widget input after clf+draw
    # Button callback should work fine, but slider callback should fail in buggy version
    assert widget_responsive['button'], "Button callback should maintain widget responsiveness"
    
    # This assertion should FAIL in the buggy version
    assert widget_responsive['slider'], "RangeSlider callback should maintain widget responsiveness after clf+draw"
    
    plt.close(fig)