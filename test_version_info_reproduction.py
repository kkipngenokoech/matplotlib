import matplotlib

def test_issue_reproduction():
    # Test that matplotlib exposes a version_info tuple for easy version comparison
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have a version_info attribute"
    
    version_info = matplotlib.version_info
    
    # version_info should be a tuple
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    
    # version_info should contain at least major, minor components as integers
    assert len(version_info) >= 2, "version_info should have at least major and minor components"
    assert all(isinstance(x, int) for x in version_info[:2]), "major and minor version components should be integers"
    
    # Should be comparable with other tuples (this is the main use case)
    # This should work without raising an exception
    comparison_result = version_info >= (3, 0)
    assert isinstance(comparison_result, bool), "version_info should be comparable with tuples"