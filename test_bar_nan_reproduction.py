import numpy as np
import matplotlib.pyplot as plt
import pytest

def test_issue_reproduction():
    """Test that ax.bar handles all-NaN x-position data without raising StopIteration."""
    fig, ax = plt.subplots()
    
    # This should not raise an exception but currently does in 3.6.1
    # Expected behavior: return a BarCollection with NaN values
    result = ax.bar([np.nan], [0])
    
    # Verify that we get a BarContainer back (not None)
    assert result is not None
    
    # Clean up
    plt.close(fig)