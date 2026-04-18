import matplotlib.pyplot as plt
from matplotlib import get_backend, rc_context
from matplotlib._pylab_helpers import Gcf

def test_issue_reproduction():
    # Clear any existing figures
    plt.close('all')
    
    # Create first figure under rc_context
    with rc_context({'figure.figsize': (6, 4)}):
        fig1 = plt.figure()
    
    # Create second figure normally
    fig2 = plt.figure()
    
    # Both figures should be in Gcf.figs
    assert len(Gcf.figs) == 2
    assert fig1.number in Gcf.figs
    assert fig2.number in Gcf.figs
    
    # Call get_backend() - this should not clear figures
    backend = get_backend()
    
    # Figures should still be present after get_backend()
    assert len(Gcf.figs) == 2, f"Expected 2 figures, got {len(Gcf.figs)}"
    assert fig1.number in Gcf.figs, "Figure 1 missing from Gcf.figs after get_backend()"
    assert fig2.number in Gcf.figs, "Figure 2 missing from Gcf.figs after get_backend()"