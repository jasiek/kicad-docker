#!/usr/bin/env python

import sys
import transparency
import drill
import gerbers
import images
from common import maybe_create_dir

from pcbnew import LoadBoard

try:
    filename = sys.argv[1]
except IndexError:
    print 'kicad_pcb source is required'
    sys.exit(1)

maybe_create_dir('outputs')
    
transparency.generate(LoadBoard(filename), 'outputs/pdf/')
drill.generate(LoadBoard(filename), 'outputs/drill/')
gerbers.generate(LoadBoard(filename), 'outputs/gerbers/')
images.generate('outputs/gerbers/', 'outputs/images/')
