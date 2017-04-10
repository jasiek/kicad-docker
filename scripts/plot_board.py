#!/usr/bin/env python

import sys
import transparency
import drill

from pcbnew import LoadBoard

try:
    filename = sys.argv[1]
except IndexError:
    print 'kicad_pcb source is required'
    sys.exit(1)

board = LoadBoard(filename)
transparency.generate(board, 'plot/')
board = LoadBoard(filename)
drill.generate(board, 'plot/')

