from pcbnew import *

def generate(board, output_dir):
    pctl = PLOT_CONTROLLER(board)
    popt = pctl.GetPlotOptions()
    popt.SetOutputDirectory(output_dir)
    
    drlwriter = EXCELLON_WRITER( board )
    drlwriter.SetMapFileFormat( PLOT_FORMAT_PDF )

    mirror = False
    minimalHeader = False
    offset = wxPoint(0,0)
    # False to generate 2 separate drill files (one for plated holes, one for non plated holes)
    # True to generate only one drill file
    mergeNPTH = True
    drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )

    metricFmt = True
    drlwriter.SetFormat( metricFmt )

    genDrl = True
    genMap = True
    drlwriter.CreateDrillandMapFilesSet( pctl.GetPlotDirName(), genDrl, genMap );

    # One can create a text file to report drill statistics
    rptfn = pctl.GetPlotDirName() + 'drill_report.rpt'
    drlwriter.GenDrillReportFile( rptfn );
