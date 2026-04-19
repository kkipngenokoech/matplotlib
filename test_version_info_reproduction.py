import matplotlib

def test_issue_reproduction():
    # Test that version_info tuple exists and is comparable
    assert hasattr(matplotlib, 'version_info'), "matplotlib should expose version_info tuple"
    
    version_info = matplotlib.version_info
    
    # Should be a tuple with at least major, minor, patch components
    assert isinstance(version_info, tuple), "version_info should be a tuple"
    assert len(version_info) >= 3, "version_info should have at least 3 components (major, minor, patch)"
    
    # Components should be integers (for major, minor, patch)
    assert all(isinstance(x, int) for x in version_info[:3]), "First 3 components should be integers"
    
    # Should be comparable with other tuples
    assert version_info >= (3, 0, 0), "Should be able to compare version_info with tuples"
    
    # Test that it's consistent with __version__ string
    version_str = matplotlib.__version__
    major, minor, patch = version_info[:3]
    assert version_str.startswith(f"{major}.{minor}.{patch}"), "version_info should match __version__ string"