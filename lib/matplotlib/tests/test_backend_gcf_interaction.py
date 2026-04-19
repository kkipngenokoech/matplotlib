import matplotlib.pyplot as plt
from matplotlib import get_backend, rc_context
from matplotlib._pylab_helpers import Gcf
import pytest


def test_get_backend_preserves_figures_created_in_rc_context():
    """Test that get_backend() doesn't clear figures created under rc_context."""
    # Clear any existing figures
    plt.close('all')
    
    # Create a figure under rc_context
    with rc_context({'figure.figsize': (6, 4)}):
        fig1 = plt.figure()
    
    # Create another figure normally
    fig2 = plt.figure()
    
    # Verify both figures are in Gcf.figs
    assert len(Gcf.figs) == 2
    assert fig1.number in Gcf.figs
    assert fig2.number in Gcf.figs
    
    # Call get_backend() - this should not clear figures
    backend = get_backend()
    
    # Verify figures are still in Gcf.figs
    assert len(Gcf.figs) == 2, f"Expected 2 figures, got {len(Gcf.figs)}"
    assert fig1.number in Gcf.figs, "Figure created in rc_context was cleared"
    assert fig2.number in Gcf.figs, "Normal figure was cleared"
    
    # Verify plt.close() still works
    plt.close(fig2)
    assert len(Gcf.figs) == 1
    assert fig1.number in Gcf.figs
    assert fig2.number not in Gcf.figs
    
    # Clean up
    plt.close('all')


def test_get_backend_preserves_figures_mixed_creation_order():
    """Test with different creation orders of figures."""
    # Clear any existing figures
    plt.close('all')
    
    # Create a normal figure first
    fig1 = plt.figure()
    
    # Create a figure under rc_context
    with rc_context({'figure.figsize': (8, 6)}):
        fig2 = plt.figure()
    
    # Create another normal figure
    fig3 = plt.figure()
    
    # Verify all figures are in Gcf.figs
    assert len(Gcf.figs) == 3
    
    # Call get_backend() - this should not clear figures
    backend = get_backend()
    
    # Verify figures are still in Gcf.figs
    assert len(Gcf.figs) == 3
    assert fig1.number in Gcf.figs
    assert fig2.number in Gcf.figs
    assert fig3.number in Gcf.figs
    
    # Clean up
    plt.close('all')


def test_get_backend_with_only_rc_context_figures():
    """Test when all figures are created under rc_context."""
    # Clear any existing figures
    plt.close('all')
    
    # Create multiple figures under rc_context
    with rc_context({'figure.figsize': (5, 5)}):
        fig1 = plt.figure()
        fig2 = plt.figure()
    
    # Verify figures are in Gcf.figs
    assert len(Gcf.figs) == 2
    
    # Call get_backend() - this should not clear figures
    backend = get_backend()
    
    # Verify figures are still in Gcf.figs
    assert len(Gcf.figs) == 2
    assert fig1.number in Gcf.figs
    assert fig2.number in Gcf.figs
    
    # Clean up
    plt.close('all')


def test_get_backend_multiple_calls():
    """Test that multiple calls to get_backend() don't cause issues."""
    # Clear any existing figures
    plt.close('all')
    
    # Create a figure under rc_context
    with rc_context({'figure.figsize': (7, 5)}):
        fig1 = plt.figure()
    
    # Call get_backend() multiple times
    backend1 = get_backend()
    backend2 = get_backend()
    backend3 = get_backend()
    
    # Verify figure is still in Gcf.figs
    assert len(Gcf.figs) == 1
    assert fig1.number in Gcf.figs
    
    # Verify all calls return the same backend
    assert backend1 == backend2 == backend3
    
    # Clean up
    plt.close('all')
