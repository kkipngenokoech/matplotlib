import matplotlib.pyplot as plt
import pytest

def test_issue_reproduction():
    """Test that seaborn-colorblind style is accessible from style library."""
    # This should not raise a KeyError - the style should be available
    # either directly or through some backward compatibility mechanism
    the_rc = plt.style.library["seaborn-colorblind"]
    assert the_rc is not None