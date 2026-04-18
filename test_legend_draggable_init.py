import matplotlib.pyplot as plt
import matplotlib.legend as mlegend
from matplotlib.lines import Line2D

def test_issue_reproduction():
    """Test that Legend constructor should accept draggable parameter."""
    fig, ax = plt.subplots()
    
    # Create some dummy handles and labels for the legend
    handles = [Line2D([0], [0], color='red')]
    labels = ['Test Line']
    
    # This should work but currently fails because draggable is not a valid parameter
    try:
        legend = mlegend.Legend(ax, handles, labels, draggable=True)
        # If we get here, the parameter was accepted
        # Check that the legend is actually draggable
        assert hasattr(legend, '_draggable') and legend._draggable is not None
    except TypeError as e:
        # This is what currently happens - draggable is not a recognized parameter
        assert 'draggable' in str(e)
        raise AssertionError("Legend constructor should accept 'draggable' parameter but doesn't")