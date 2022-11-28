#
# png_overlay ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
from PIL import Image
import os

Gstr_title = r"""
                                          _             
                                         | |            
 _ __  _ __   __ _     _____   _____ _ __| | __ _ _   _ 
| '_ \| '_ \ / _` |   / _ \ \ / / _ \ '__| |/ _` | | | |
| |_) | | | | (_| |  | (_) \ V /  __/ |  | | (_| | |_| |
| .__/|_| |_|\__, |   \___/ \_/ \___|_|  |_|\__,_|\__, |
| |           __/ |_____                           __/ |
|_|          |___/______|                         |___/ 
"""

Gstr_synopsis = """


    NAME

       png_overlay

    SYNOPSIS

        docker run --rm fnndsc/pl-png_overlay png_overlay               \\
            [-b|--background <bgFileName>]                              \\
            [-o|--overlay <overlayFileName>]                            \\
            [-s|--outputFileName <opFileName>]                          \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-png_overlay png_overlay                   \
                /incoming /outgoing

    DESCRIPTION

        `png_overlay` ...

    ARGS
    
        [-b|--background <bgFileName>]
        Name of the input background file.
        Default is 'leg.png'
        
        [-o|--overlay <overlayFileName>]
        Name of the input overlay/mask file.
        Default is 'composite.png'
        
        [-s|--outputFileName <opFileName>]
        Name of the output file.
        Default is 'overlay.png'

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Png_overlay(ChrisApp):
    """
    An app to create an overlay PNG with two input PNGs
    """
    PACKAGE                 = __package__
    TITLE                   = 'A ChRIS plugin app to create an overlay PNG with two input PNGs'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument(  '--background','-b',
                            dest         = 'background',
                            type         = str,
                            optional     = True,
                            help         = 'Input background file name',
                            default      = 'leg.png')
                            
        self.add_argument(  '--overlay','-o',
                            dest         = 'overlay',
                            type         = str,
                            optional     = True,
                            help         = 'Input overlay file name',
                            default      = 'composite.png')
                            
        self.add_argument(  '--outputFileName','-s',
                            dest         = 'outputFileName',
                            type         = str,
                            optional     = True,
                            help         = 'Output file name',
                            default      = 'overlay.png')
                            
    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        
        for root,dirs,files in os.walk(options.inputdir):
            for dir in dirs:
                dir_name = os.path.join(root,dir)
        
                background_path = os.path.join(dir_name,options.background)
                overlay_path = os.path.join(dir_name,options.overlay)
                output_dir = os.path.join(options.outputdir,dir)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
        
                background = Image.open(background_path)
                overlay = Image.open(overlay_path)
                
                
                # Print image details to std. output
                print(f"\nReading images from {dir_name}")
                print(f"Shape of {options.background} is {background.size}")
                print(f"Shape of {options.overlay} is {overlay.size}")
                
                overlay = overlay.resize(background.size,Image.ANTIALIAS)
                background.paste(overlay, (0,0),mask=overlay)
                background.save(os.path.join(output_dir,options.outputFileName))

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
