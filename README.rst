pl-png_overlay
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-png_overlay?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-png_overlay

.. image:: https://img.shields.io/github/license/fnndsc/pl-png_overlay
    :target: https://github.com/FNNDSC/pl-png_overlay/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-png_overlay/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-png_overlay/actions


.. contents:: Table of Contents


Abstract
--------

An app to create an overlay PNG with two input PNGs


Description
-----------


``png_overlay`` is a *ChRIS ds-type* application that takes in ... as ... files
and produces ...


Usage
-----

.. code::

    docker run --rm fnndsc/pl-png_overlay png_overlay
        [-b|--background <bgFileName>]                              
        [-o|--overlay <overlayFileName>]                            
        [-s|--outputFileName <opFileName>]                          
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

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


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-png_overlay png_overlay --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-png_overlay png_overlay                        \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-png_overlay .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-png_overlay nosetests

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
