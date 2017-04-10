#!/usr/bin/env python

import sys
import transparency
import drill
import gerbers

from pcbnew import LoadBoard

try:
    filename = sys.argv[1]
except IndexError:
    print 'kicad_pcb source is required'
    sys.exit(1)

transparency.generate(LoadBoard(filename), 'plot/')
drill.generate(LoadBoard(filename), 'plot/')
# Doesn't quite work
# gerbers.generate(LoadBoard(filename), 'plot/')

