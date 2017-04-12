import os
from common import *
from ctypes import *
from ctypes.util import find_library
from data import *

Colours = [
    GdkColor(0, 65530, 32000, 32000)
]

class GerbvStacker:
    def __init__(self):
        self.gerbv = CDLL(find_library("gerbv"))
        self.create_project()
        self.current_layer_idx = 0

    def create_project(self):
        fun = self.gerbv.gerbv_create_project
        fun.restype = POINTER(GerbvProject)
        self.project = fun()[0]

    def add_layer(self, filename):
        fun = self.gerbv.gerbv_open_layer_from_filename
        fun.argtypes = [POINTER(GerbvProject), c_char_p]
        fun(byref(self.project), filename)
        self.project.file.color = Colours[self.current_layer_idx]
        self.current_layer_idx += 1

    def export(self, filename):
        fun = self.gerbv.gerbv_export_png_file_from_project_autoscaled
        fun.argtypes = [POINTER(GerbvProject), c_int, c_int, c_char_p]
        fun(byref(self.project), 640, 480, filename)
    

def generate(input_dir, output_dir):
    maybe_create_dir(output_dir)
    for filename in os.listdir(input_dir):
        s = GerbvStacker()
        s.add_layer(input_dir + '/' + filename)
        s.export(output_dir + '/' + filename + '.png')
    
    
    
