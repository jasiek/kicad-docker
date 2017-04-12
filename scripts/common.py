import os

def maybe_create_dir(output_dir):
    try:
        os.mkdir(output_dir)
    except OSError:
        pass
    
