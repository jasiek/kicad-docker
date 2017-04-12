#!/usr/bin/env python

import os
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

os.mkdir('outputs')
    
transparency.generate(LoadBoard(filename), 'outputs/pdf/')
drill.generate(LoadBoard(filename), 'outputs/drill/')
gerbers.generate(LoadBoard(filename), 'outputs/gerbers/')

