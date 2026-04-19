import matplotlib.pyplot as plt
import matplotlib.patches as patches
from io import BytesIO

def test_issue_reproduction():
    """Test that set_visible(False) works for 3D projection axes."""
    fig = plt.figure(figsize=(6, 4))
    
    # Create a 3D subplot
    ax = fig.add_subplot(111, projection='3d')
    
    # Add some content to make the axes visible
    ax.plot([0, 1], [0, 1], [0, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y') 
    ax.set_zlabel('Z')
    
    # Set the axes to be invisible
    ax.set_visible(False)
    
    # Render to a buffer to capture what would be drawn
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    
    # Get the rendered image data
    import matplotlib.image as mpimg
    img = mpimg.imread(buf)
    
    # Check if the image is mostly empty (white/transparent)
    # If set_visible(False) works correctly, the image should be mostly empty
    # We'll check if most pixels are white (close to 1.0 in normalized RGB)
    white_threshold = 0.95
    white_pixels = (img[:, :, :3] > white_threshold).all(axis=2)
    white_ratio = white_pixels.sum() / white_pixels.size
    
    # If visibility works correctly, most of the image should be white
    # This assertion will FAIL on the current buggy code because the 3D axes
    # will still be drawn despite set_visible(False)
    assert white_ratio > 0.9, f"Expected mostly white image (>90% white pixels), got {white_ratio:.2%} white pixels. The 3D axes should be invisible but is still being drawn."
    
    plt.close(fig)