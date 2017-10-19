
import numpy as np
import matplotlib.pyplot as plt


# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html
cmaps = [
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ]


# fig, axes = plt.subplots(nrows=50)

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

gradient = np.array([(0,3), (1,2),(0,1)])

print (gradient)

def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(ncols=8, nrows=1)
    # fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        
        ax.imshow(gradient, cmap=plt.get_cmap(name), clim=(0,0.1))
        # pos = list(ax.get_position().bounds)
        # x_text = pos[0] - 0.01
        # y_text = pos[1] + pos[3]/2.
        # fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()


for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list, nrows)

plt.show()