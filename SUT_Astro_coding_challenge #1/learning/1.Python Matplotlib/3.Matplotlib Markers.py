import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([0, 3, 4, 5, 6, 7, 8])
ypoints2 = np.array([3, 8, 1, 10])

# use argument "marker" to emphasize each point
# with a specified marker
# ms to set the size of the markers
# argument markeredgecolor 'mec' to set the color of the edge
    # of the markers
# argument markerfacecolor 'mfc' to set the color inside
    #the edge of the markers
    

plt.plot(ypoints, marker = '.', ms = 20, mec = 'r', mfc = 'b')

#  Marker	Description
#  'o'	     Circle	
#  '*'	     Star	
#  '.'	     Point	
#  ','	     Pixel	
#  'x'	     X	
#  'X'	     X (filled)	
#  '+'	     Plus	
#  'P'	     Plus (filled)	
#  's'	     Square	
#  'D'	     Diamond	
#  'd'	     Diamond (thin)	
#  'p'	     Pentagon	
#  'H'	     Hexagon	
#  'h'	     Hexagon	
#  'v'	     Triangle Down	
#  '^'	     Triangle Up	
#  '<'	     Triangle Left	
#  '>'	     Triangle Right	
#  '1'	     Tri Down	
#  '2'	     Tri Up	
#  '3'	     Tri Left	
#  '4'	     Tri Right	
#  '|'	     Vline	
#  '_'	     Hline

# parameter called fmt have syntax like this
# marker|line|color

# You can also use Hexadecimal color values:
    # follow html color support

plt.plot(ypoints2, 'o:g', mec = '#4CAF50', mfc = '#4CAF50')

# If you leave out the line value in the fmt parameter,
# no line will be plotted.

#   Line Syntax	  Description
#   '-'	          Solid line	
#   ':'	          Dotted line	
#   '--'	      Dashed line	
#   '-.'	      Dashed/dotted line

#   Color Syntax	Description
#    'r'	        Red	
#    'g'	        Green	
#    'b' 	        Blue	
#    'c'	        Cyan	
#    'm'	        Magenta	
#    'y' 	        Yellow	
#    'k'	        Black	
#    'w'	        White

plt.show()