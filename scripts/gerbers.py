from pcbnew import *

FRONT_LAYERS = [
    ("F.Cu", F_Cu),
    ("F.Adhes", F_Adhes),
    ("F.Paste", F_Paste),
    ("F.SilkS", F_SilkS),
    ("F.CrtYd", F_CrtYd),
    ("F.Fab", F_Fab)
]

BACK_LAYERS = [
    ("B.Cu", B_Cu),
    ("B.Adhes", B_Adhes),
    ("B.Paste", B_Paste),
    ("B.SilkS", B_SilkS),
    ("B.CrtYd", B_CrtYd),
    ("B.Fab", B_Fab)
]

OTHER_LAYERS = [
    ("Dwgs.User", Dwgs_User),
    ("Cmts.User", Cmts_User),
    ("Eco1.User", Eco1_User),
    ("Eco2.User", Eco2_User),
    ("Edge.Cuts", Edge_Cuts),
    ("Margin", Margin)
]

def generate(board, output_dir):
    pctl = PLOT_CONTROLLER(board)
    popt = pctl.GetPlotOptions()
    popt.SetOutputDirectory(output_dir)

    # Set some important plot options:
    popt.SetPlotFrameRef(False)     #do not change it
    popt.SetLineWidth(FromMM(0.35))
    
    popt.SetAutoScale(False)        #do not change it
    popt.SetScale(1)                #do not change it
    popt.SetMirror(False)
    popt.SetUseGerberAttributes(True)
    popt.SetUseGerberProtelExtensions(False)
    popt.SetExcludeEdgeLayer(False);
    popt.SetScale(1)
    popt.SetUseAuxOrigin(True)
    
    # This by gerbers only (also the name is truly horrid!)
    popt.SetSubtractMaskFromSilk(False)

    all_layers = FRONT_LAYERS + BACK_LAYERS + OTHER_LAYERS
    for layer_info in all_layers:
        pctl.SetLayer(layer_info[1])
        pctl.OpenPlotFile(layer_info[0], PLOT_FORMAT_GERBER, layer_info[0])
        if pctl.PlotLayer() == False:
            return False

    pctl.ClosePlot()

    
