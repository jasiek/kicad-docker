#!/usr/bin/env python

import sys
import transparency
import drill

try:
    filename = sys.argv[1]
except IndexError:
    print 'kicad_pcb source is required'
    sys.exit(1)

board = LoadBoard(filename)
transparency.generate(board, 'plot/')
drill.generate(board, 'plot/')

