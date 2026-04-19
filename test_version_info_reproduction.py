import matplotlib

def test_issue_reproduction():
    # Test that matplotlib has a version_info tuple attribute
    # This should be a tuple of integers like (3, 5, 2) for version "3.5.2"
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have version_info attribute"
    
    version_info = matplotlib.version_info
    
    # version_info should be a tuple
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    
    # version_info should contain at least major and minor version numbers as integers
    assert len(version_info) >= 2, "version_info should have at least major and minor version"
    assert all(isinstance(x, int) for x in version_info[:2]), "version components should be integers"
    
    # Should be comparable with other tuples for version checking
    assert version_info >= (0, 0), "version_info should be comparable with tuples"