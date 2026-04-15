import matplotlib

def test_issue_reproduction():
    # Test that matplotlib exposes a version_info tuple for easy version comparisons
    # This should be similar to sys.version_info
    
    # Check that version_info attribute exists
    assert hasattr(matplotlib, 'version_info'), "matplotlib should have a version_info attribute"
    
    # Check that version_info is a tuple
    version_info = matplotlib.version_info
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    
    # Check that it has at least 3 elements (major, minor, patch)
    assert len(version_info) >= 3, "version_info should have at least 3 elements (major, minor, patch)"
    
    # Check that the first 3 elements are integers
    assert all(isinstance(x, int) for x in version_info[:3]), "First 3 elements should be integers"
    
    # Test that it can be compared with other tuples (the main use case)
    # This should work without raising an exception
    result = version_info >= (3, 0, 0)
    assert isinstance(result, bool), "version_info should be comparable with tuples"