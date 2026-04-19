import matplotlib.pyplot as pyplot
import matplotlib.widgets as widgets

# Test script to reproduce the issue
fig, ax = pyplot.subplots()
pyplot.subplots_adjust(bottom=0.25)

# Create initial plot
ax.plot([1, 2, 3], [1, 4, 2])

# Create range slider
ax_slider = pyplot.axes([0.2, 0.1, 0.5, 0.03])
slider = widgets.RangeSlider(ax_slider, 'Range', 0, 10, valinit=(2, 8))

# Create button for comparison
ax_button = pyplot.axes([0.8, 0.1, 0.1, 0.04])
button = widgets.Button(ax_button, 'Reset')

def on_slider_changed(val):
    print(f"Slider changed: {val}")
    pyplot.clf()  # This causes the issue
    ax = pyplot.gca()
    ax.plot([1, 2, 3], [val[0], val[1], (val[0]+val[1])/2])
    pyplot.draw()  # This completes the problematic sequence

def on_button_clicked(event):
    print("Button clicked")
    pyplot.clf()  # This works fine
    ax = pyplot.gca()
    ax.plot([1, 2, 3], [1, 4, 2])
    pyplot.draw()  # This works fine

slider.on_changed(on_slider_changed)
button.on_clicked(on_button_clicked)

pyplot.show()
