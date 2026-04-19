import matplotlib.pyplot as plt
from matplotlib import get_backend, rc_context
from matplotlib._pylab_helpers import Gcf

def test_issue_reproduction():
    # Create a figure under rc_context (this will be the first figure)
    with rc_context():
        fig1 = plt.figure()
    
    # Create a second figure normally
    fig2 = plt.figure()
    
    # Verify both figures are in Gcf.figs before calling get_backend()
    assert len(Gcf.figs) == 2
    assert fig1.number in Gcf.figs
    assert fig2.number in Gcf.figs
    
    # This call should not clear the figures, but it does due to the bug
    get_backend()
    
    # The bug causes figures to be cleared from Gcf.figs
    assert len(Gcf.figs) == 2, f"Expected 2 figures, but got {len(Gcf.figs)}"
    assert fig1.number in Gcf.figs, "Figure 1 should still be in Gcf.figs"
    assert fig2.number in Gcf.figs, "Figure 2 should still be in Gcf.figs"