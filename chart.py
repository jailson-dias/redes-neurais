

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
cmap = colors.ListedColormap(['red', 'green'])

fig, axes = plt.subplots(nrows=1)
axes.set_title('colormaps', fontsize=14)
axes.axis([-0.5, 6.5, 0, 1300])

label = ["a","b", "c", "d", "e", "f", "g"]
x = np.array([0,1,2,3,4,5,6])
plt.xticks(x, label)

# axes([0.08, 0.08, 0.94-0.08, 0.94-0.08])
# fig = plt.figure()
# fig.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.98)
# axes=axes.reshape(1,len(axes))
# axes.fill(9,3)

# plt.gca().set_position([0, 0, 1, 1]) # ponto inicial e final do grafico

# data = random.random((5,5))
a = [(0,0,1,0,0,0,1), (1,0,1,0,0,0,1), (1,0,0,0,0,0,1), (1,0,1,0,1,0,0),(0,0,1,0,1,0,1)]
for i in range(0,8):
    a += a
img = plt.imshow(a, cmap=cmap, interpolation='nearest', aspect='auto')
# img.set_cmap('hot')
# plt.axis('off')
# plt.savefig("test.png", bbox_inches='tight')
plt.show()

"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html
cmaps = [
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ]

cmap = colors.ListedColormap(['red', 'green', 'yellow', 'black', 'blue'])
# fig, axes = plt.subplots(nrows=50)

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

a = [(5,4,1)]
# for i in range(0, 20):
#     a += a

gradient = np.array(a)

print (gradient)

def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(ncols=2)
    # fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        
        ax.imshow(gradient, cmap=cmap, interpolation='nearest')
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

"""