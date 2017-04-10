from pcbnew import *

def generate(board, output_dir):
    pctl = PLOT_CONTROLLER(board)
    popt = pctl.GetPlotOptions()

    popt.SetOutputDirectory(output_dir)

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
