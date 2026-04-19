import matplotlib.pyplot as plt
import matplotlib.legend as mlegend
import pytest

def test_issue_reproduction():
    """Test that Legend.__init__ accepts draggable keyword argument."""
    fig, ax = plt.subplots()
    line, = ax.plot([1, 2, 3], [1, 2, 3], label='test')
    
    # This should work but currently fails because draggable is not accepted
    # as a keyword argument in Legend.__init__
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        legend = mlegend.Legend(ax, [line], ['test'], draggable=True)
    
    # Verify the current workaround works
    legend = mlegend.Legend(ax, [line], ['test'])
    legend.set_draggable(True)
    assert legend.get_draggable() is True