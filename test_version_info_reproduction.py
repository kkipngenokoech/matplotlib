import matplotlib

def test_issue_reproduction():
    # Test that version_info tuple exists and is comparable
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have version_info attribute"
    
    version_info = matplotlib.version_info
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    assert len(version_info) >= 2, "version_info should have at least major and minor components"
    
    # Test that components are integers for proper comparison
    for component in version_info[:2]:  # At least major and minor should be integers
        assert isinstance(component, int), f"version component {component} should be an integer"
    
    # Test that it can be compared with other tuples (the main use case)
    assert version_info >= (3, 0), "matplotlib version should be at least 3.0"
    assert version_info < (99, 0), "version comparison should work with tuples"