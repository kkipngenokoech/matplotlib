import numpy as np
import matplotlib.pyplot as plt
import pytest


def test_bar_all_nan_x():
    """Test that ax.bar handles all-NaN x data without raising StopIteration."""
    fig, ax = plt.subplots()
    
    # This should not raise an exception
    result = ax.bar([np.nan], [0])
    
    # Should return a BarContainer
    assert hasattr(result, 'patches')
    # Should have empty patches for all-NaN case
    assert len(result.patches) == 0
    
    plt.close(fig)


def test_bar_all_nan_x_multiple():
    """Test that ax.bar handles multiple all-NaN x values."""
    fig, ax = plt.subplots()
    
    # This should not raise an exception
    result = ax.bar([np.nan, np.nan, np.nan], [1, 2, 3])
    
    # Should return a BarContainer
    assert hasattr(result, 'patches')
    # Should have empty patches for all-NaN case
    assert len(result.patches) == 0
    
    plt.close(fig)


def test_bar_mixed_nan_x():
    """Test that ax.bar handles mixed NaN/valid x data correctly."""
    fig, ax = plt.subplots()
    
    # This should work and create bars for valid data only
    result = ax.bar([np.nan, 1, np.nan, 2], [1, 2, 3, 4])
    
    # Should return a BarContainer
    assert hasattr(result, 'patches')
    # Should have 2 patches for the 2 valid x values
    assert len(result.patches) == 2
    
    plt.close(fig)


def test_bar_nan_height_works():
    """Test that ax.bar with NaN height still works (regression test)."""
    fig, ax = plt.subplots()
    
    # This should work as before
    result = ax.bar([0], [np.nan])
    
    # Should return a BarContainer
    assert hasattr(result, 'patches')
    # Should have empty patches when height is NaN
    assert len(result.patches) == 0
    
    plt.close(fig)


def test_bar_empty_data():
    """Test that ax.bar handles empty data correctly."""
    fig, ax = plt.subplots()
    
    # This should work
    result = ax.bar([], [])
    
    # Should return a BarContainer
    assert hasattr(result, 'patches')
    # Should have empty patches
    assert len(result.patches) == 0
    
    plt.close(fig)


if __name__ == '__main__':
    test_bar_all_nan_x()
    test_bar_all_nan_x_multiple()
    test_bar_mixed_nan_x()
    test_bar_nan_height_works()
    test_bar_empty_data()
    print("All tests passed!")
