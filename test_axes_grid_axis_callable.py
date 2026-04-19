import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib.axes import Axes


class MockGeoAxes(Axes):
    """Mock axes class that mimics cartopy's GeoAxes behavior where axis is a callable."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store the original axis dict
        self._axis_dict = super().axis
        
    @property
    def axis(self):
        """Return a callable that returns the axis dict, mimicking GeoAxes behavior."""
        return lambda: self._axis_dict


def test_issue_reproduction():
    """Test that AxesGrid fails with non-default axis class where axis is callable."""
    fig = plt.figure()
    
    # This should raise TypeError: 'method' object is not subscriptable
    # when _tick_only tries to access ax.axis["bottom"] and ax.axis["left"]
    grid = AxesGrid(fig, 111, nrows_ncols=(1, 1), axes_class=MockGeoAxes)
    
    plt.close(fig)