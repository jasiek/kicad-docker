import os
import re
from common import *
from ctypes import *
from ctypes.util import find_library
from data import *

class GerbvStacker:
    def __init__(self):
        self.gerbv = CDLL(find_library("gerbv"))
        self.layers = []

    def create_project(self):
        fun = self.gerbv.gerbv_create_project
        fun.restype = POINTER(GerbvProject)
        return fun()[0]

    def add_layer(self, filename):
        self.layers.append(filename)

    def export(self, filename):
        project = self.create_project()
        self._append_layers(project, self._sorted_layers())
        fun = self.gerbv.gerbv_export_png_file_from_project_autoscaled
        fun.argtypes = [POINTER(GerbvProject), c_int, c_int, c_char_p]
        fun(byref(project), 1024, 1024, filename)

    def export_svg(self, filename):
        project = self.create_project()
        self._append_layers(project, self._sorted_layers())
        fun = self.gerbv.gerbv_export_svg_file_from_project_autoscaled
        fun.argtypes = [POINTER(GerbvProject), c_char_p]
        fun(byref(project), filename)

    def _append_layers(self, project, layers):
        fun = self.gerbv.gerbv_open_layer_from_filename
        fun.argtypes = [POINTER(GerbvProject), c_char_p]
        for layer_filename in layers:
            fun(byref(project), layer_filename)

    def _sorted_layers(self):
        def idx_for_layer(filename):
            if ".Cu." in filename:
                return 0
            if ".Adhes." in filename:
                return 1
            if ".Paste." in filename:
                return 2
            if ".SilkS." in filename:
                return 3
            if "Dwgs.User" in filename:
                return 4
            if "Cmts.User" in filename:
                return 5
            if "Edge.Cuts" in filename:
                return 99
            return -1
        return sorted(self.layers, key=idx_for_layer)

def generate(input_dir, output_dir):
    maybe_create_dir(output_dir)
    for layer in ["-F.", "-B."]:
        s = GerbvStacker()
        for filename in os.listdir(input_dir):
            if "User" in filename or layer in filename:
                s.add_layer(input_dir + '/' + filename)

        s.export(output_dir + '/output' + layer + 'png')
        s.export_svg(output_dir + '/output' + layer + 'svg')
