import matplotlib.pyplot as plt

# fmt = '[marker][line][color]' or '[color][marker][line]'
# colors:          marker:                      line:
# 'b': blue        '.': point marker            '-' : solid line style
# 'g': green       ',': pixel marker            '--': dashed line style
# 'r': red         'o': circle marker           '-.': dash-dot line style
# 'c': cyan        'v': triangle_down marker    ':' : dotted line style
# 'm': magenta     '^': triangle_up marker
# 'y': yellow      '<': triangle_left marker
# 'k': black       '>': triangle_right marker
# 'w': white       '1': tri_down marker
#                  '2': tri_up marker
#                  '3': tri_left marker
#                  '4': tri_right marker
#                  '8': octagon marker
#                  's': square marker
#                  'p': pentagon marker
#                  'P': plus (filled) marker
#                  '*': star marker
#                  'h': hexagon1 marker
#                  'H': hexagon2 marker
#                  '+': plus marker
#                  'x': x marker
#                  'X': x (filled) marker
#                  'D': diamond marker
#                  'd': thin_diamond marker
#                  '|': vline marker
#                  '_': hline marker

# default is 'b-' is blue line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-')

# 'ro' is red circles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# 'g^' is green trigangles
plt.plot([1, 2, 3, 4], [4, 3, 2, 1], 'g^')

# [xmin, xmax, ymin, ymax] [0-6, 0-20]
plt.axis((0, 6, 0, 20))

plt.show()
