import matplotlib

def test_issue_reproduction():
    # Test that version_info exists and is a comparable tuple
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have version_info attribute"
    
    version_info = matplotlib.version_info
    
    # Should be a tuple
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    
    # Should contain integers for easy comparison
    assert all(isinstance(x, int) for x in version_info), "version_info should contain integers"
    
    # Should be comparable with other tuples (basic functionality test)
    assert version_info >= (3, 0, 0), "version_info should be comparable with tuples"
    
    # Should have at least major.minor components
    assert len(version_info) >= 2, "version_info should have at least major and minor version components"