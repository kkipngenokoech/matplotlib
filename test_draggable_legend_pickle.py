import matplotlib.pyplot as plt
import pickle
import pytest

def test_issue_reproduction():
    """Test that pickling a figure with draggable legend fails."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], label='test')
    legend = ax.legend(draggable=True)
    
    # This should fail with TypeError: cannot pickle 'FigureCanvasQTAgg' object
    # or similar canvas-related pickle error
    with pytest.raises((TypeError, AttributeError)) as exc_info:
        pickle.dumps(fig)
    
    # Verify the error is related to canvas pickling
    assert "canvas" in str(exc_info.value).lower() or "pickle" in str(exc_info.value).lower()