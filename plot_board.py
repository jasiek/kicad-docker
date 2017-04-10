#!/usr/bin/env python

import sys

from pcbnew import *
filename=sys.argv[1]

board = LoadBoard(filename)

pctl = PLOT_CONTROLLER(board)

popt = pctl.GetPlotOptions()

popt.SetOutputDirectory("plot/")

# Set some important plot options:
popt.SetPlotFrameRef(False)
popt.SetLineWidth(FromMM(0.35))

popt.SetAutoScale(False)
popt.SetScale(1)
popt.SetMirror(False)
popt.SetUseGerberAttributes(True)
popt.SetExcludeEdgeLayer(False);
popt.SetScale(1)
popt.SetUseAuxOrigin(True)

# This by gerbers only (also the name is truly horrid!)
popt.SetSubtractMaskFromSilk(False)
popt.SetPlotReference(False)
popt.SetPlotValue(False)
popt.SetPlotInvisibleText(False)
popt.SetDrillMarksType(PCB_PLOT_PARAMS.NO_DRILL_SHAPE)

plot_plan = [
    ( "F.Cu", F_Cu, "Top layer", True ),
    ( "B.Cu", B_Cu, "Bottom layer", False ),
]

for layer_info in plot_plan:
    popt.SetMirror(layer_info[3])
    pctl.SetLayer(layer_info[1])
    pctl.OpenPlotfile(layer_info[0], PLOT_FORMAT_PDF, layer_info[2])
    pctl.PlotLayer()

pctl.ClosePlot()

drlwriter = EXCELLON_WRITER( board )
drlwriter.SetMapFileFormat( PLOT_FORMAT_PDF )

mirror = False
minimalHeader = False
offset = wxPoint(0,0)
# False to generate 2 separate drill files (one for plated holes, one for non plated holes)
# True to generate only one drill file
mergeNPTH = False
drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )

metricFmt = True
drlwriter.SetFormat( metricFmt )

genDrl = True
genMap = True
print 'create drill and map files in %s' % pctl.GetPlotDirName()
drlwriter.CreateDrillandMapFilesSet( pctl.GetPlotDirName(), genDrl, genMap );

# One can create a text file to report drill statistics
rptfn = pctl.GetPlotDirName() + 'drill_report.rpt'
print 'report: %s' % rptfn
drlwriter.GenDrillReportFile( rptfn );
