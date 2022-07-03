.. hyperspy-bundle documentation master file, created by
   sphinx-quickstart on Sun Jun 19 10:08:29 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to HyperSpy-bundle's Documentation!
===========================================

What is the HyperSpy-bundle
---------------------------

The hyperspy-bundle is an program, which install a python distribution including
hyperspy and other relevant scientific software and libraries. If you are brand
new to Python, this is the easiest way to install HyperSpy.

It is compatible with Windows, MacOS (Intel or native M1), or Linux and comes
with variants, which are optimised for AMD or Intel processor.
The portable version is supported on windows only

Included Software and Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Standard Version 
----------------

The standard version is very similar to the Anaconda/Miniconda/Miniforge distribution and it uses
conda/mamba package manager.
It is built using the constructor tool, which is used to build the Anaconda/Miniconda/Miniforge
distribution.

Difference with Anaconda/Miniconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Include the libraries and software mentioned above.
* The packages are download from the [*conda-forge*](https://conda-forge.org) channel only to
  avoid incompatibilities between the anaconda defaults and conda-forge channels.
* Include the `mamba` package manager, as faster alternative to `conda`.
* A configuration file `condarc` is added in the root folder of the installation to save
  the channels setting and pin the blas implementation.
* Adds context menu entries (right-click shortcut) to start the *Jupyter Notebook*, *Jupyter Lab* or *Juypter QtConsole*.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.
* Remove context menu entries when uninstalling on Windows only. For Linux and MaxOSX, no uninstall is provided and
  the context menu entries needs to be removed manually using `start_jupyter_cm --remove` from the conda environment before
  deleting the distribution.

Portable Version 
----------------


Table of Contents 
-----------------


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   download
   install
   usage
