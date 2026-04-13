import matplotlib

def test_issue_reproduction():
    # Test that version_info tuple exists at top level
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have version_info attribute"
    
    # Test that version_info is a tuple
    version_info = matplotlib.version_info
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    
    # Test that version_info has at least major, minor components
    assert len(version_info) >= 2, "version_info should have at least major and minor version components"
    
    # Test that version_info components are integers (for proper comparison)
    assert all(isinstance(x, int) for x in version_info[:2]), "version_info major and minor should be integers"
    
    # Test that version_info can be compared (this is the main use case)
    # Should be able to do comparisons like: matplotlib.version_info >= (3, 5)
    test_comparison = version_info >= (0, 0)
    assert isinstance(test_comparison, bool), "version_info should support tuple comparison"