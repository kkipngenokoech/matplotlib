import matplotlib.colors as mcolors
import numpy as np
import warnings

def test_issue_reproduction():
    """Test that color values slightly above 1.0 cause NumPy deprecation warnings."""
    # Create a color with values slightly above 1.0 that would cause
    # the multiplication by 255 to exceed 255 (uint8 max)
    color_above_one = (1.004, 0.5, 0.5, 1.0)  # 1.004 * 255 = 256.02 -> rounds to 256
    
    # Capture warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        
        # This should trigger the NumPy deprecation warning
        hex_color = mcolors.to_hex(color_above_one)
        
        # Check if we got the expected deprecation warning
        deprecation_warnings = [warning for warning in w 
                              if issubclass(warning.category, DeprecationWarning)
                              and "NumPy will stop allowing conversion of out-of-bound Python integers" in str(warning.message)]
        
        # The test should fail because we expect NO deprecation warnings
        # but the current code produces them
        assert len(deprecation_warnings) == 0, f"Got {len(deprecation_warnings)} NumPy deprecation warnings: {[str(w.message) for w in deprecation_warnings]}"