import matplotlib.pyplot as plt
import numpy as np
import warnings
from matplotlib.colors import to_hex

def test_issue_reproduction():
    """Test that reproduces NumPy 1.24 deprecation warning for out-of-bound uint8 conversion."""
    # Create a color value that when multiplied by 255 and rounded exceeds 255
    # This simulates the scenario where RGB values slightly > 1.0 cause the warning
    color_value = 1.008  # This will give 1.008 * 255 = 257.04, rounded to 257
    rgba_color = (color_value, 0.5, 0.3, 1.0)
    
    # Capture warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        
        # This should trigger the NumPy deprecation warning about converting 257 to uint8
        hex_color = to_hex(rgba_color)
        
        # Check if we got the expected deprecation warning
        deprecation_warnings = [warning for warning in w 
                              if issubclass(warning.category, DeprecationWarning)
                              and "NumPy will stop allowing conversion of out-of-bound Python integers" in str(warning.message)]
        
        # The test fails if we get the deprecation warning (current buggy behavior)
        assert len(deprecation_warnings) > 0, "Expected NumPy deprecation warning was not triggered"