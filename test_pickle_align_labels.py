import matplotlib.pyplot as plt
import pickle
import pytest


def test_pickle_figure_with_aligned_labels():
    """Test that figures can be pickled after calling align_labels()."""
    fig, (ax1, ax2) = plt.subplots(2, 1)
    
    # Add some labels
    ax1.set_xlabel('X Label 1')
    ax1.set_ylabel('Y Label 1')
    ax2.set_xlabel('X Label 2')
    ax2.set_ylabel('Y Label 2')
    
    # This should not raise an error
    pickle.dumps(fig)
    
    # Call align_labels - this is where the issue occurs
    fig.align_labels()
    
    # This should still work after alignment
    pickle.dumps(fig)
    
    plt.close(fig)


def test_pickle_figure_with_aligned_xlabels():
    """Test that figures can be pickled after calling align_xlabels()."""
    fig, (ax1, ax2) = plt.subplots(2, 1)
    
    ax1.set_xlabel('X Label 1')
    ax2.set_xlabel('X Label 2')
    
    fig.align_xlabels()
    
    # This should work
    pickle.dumps(fig)
    
    plt.close(fig)


def test_pickle_figure_with_aligned_ylabels():
    """Test that figures can be pickled after calling align_ylabels()."""
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    ax1.set_ylabel('Y Label 1')
    ax2.set_ylabel('Y Label 2')
    
    fig.align_ylabels()
    
    # This should work
    pickle.dumps(fig)
    
    plt.close(fig)


if __name__ == '__main__':
    test_pickle_figure_with_aligned_labels()
    test_pickle_figure_with_aligned_xlabels()
    test_pickle_figure_with_aligned_ylabels()
    print("All tests passed!")
