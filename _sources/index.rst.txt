.. hyperspy-bundle documentation master file, created by
   sphinx-quickstart on Sun Jun 19 10:08:29 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================
The HyperSpy-bundle
===================

What is the HyperSpy-bundle?
============================

The hyperspy-bundle is a program, which installs a python distribution including
hyperspy and other relevant scientific software and libraries for the analysis of
multidimensional datasets. It aims at making the installation of a Python distribution
very easy and integrating with existing established practices in the scientific
research community. If you are brand new to python, this is the easiest way to
install HyperSpy.

.. button-link:: https://github.com/hyperspy/hyperspy-bundle/releases/latest
    :color: primary
    :shadow:
    :align: center

    :octicon:`desktop-download` Download installer

Table of Contents 
=================


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   download
   install
   usage
   verify
   contribute

Variants of the HyperSpy-bundle
===============================

It is compatible with Windows, MacOS (Intel and Apple Silicon), or Linux and comes
with variants, which are optimised for AMD (using openblas) or Intel (using MKL) processors.
The portable version is supported on windows only.

Standard Version 
----------------

The standard version is very similar to the `Anaconda <https://www.anaconda.com/products/distribution>`_ /
`Miniforge <https://github.com/conda-forge/miniforge>`_ distribution and it uses the `conda <https://docs.conda.io/projects/conda>`__ / 
`mamba <https://mamba.readthedocs.io>`__ package manager.
It is built using the `constructor <https://github.com/conda/constructor>`_ tool, which is used to build the Anaconda / Miniforge
distribution installer.

Difference with Anaconda/Miniconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Includes the libraries and software :ref:`listed below <included_librairies-label>`.
* The packages are downloaded from the `conda-forge <https://conda-forge.org>`_ channel `only`, to
  avoid incompatibilities between the anaconda *defaults* and *conda-forge* channels.
* Includes the `mamba <https://mamba.readthedocs.io>`__ package manager, as faster alternative to `conda <https://docs.conda.io/projects/conda>`__.
* A configuration file ``.condarc`` is added in the root folder of the installation to save
  the channel's settings and pin the `blas` implementation.
* Adds context menu entries (right-click shortcut) to start the *Jupyter Notebook*, *Jupyter Lab* or *Juypter QtConsole*.
  See `start_jupyter_cm <https://github.com/hyperspy/start_jupyter_cm>`_ for details.
* Removes context menu entries when uninstalling on Windows only. For Linux and MaxOSX, no uninstall is provided and
  the context menu entries need to be removed manually using ``start_jupyter_cm --remove`` from the conda environment before
  deleting the distribution.

Portable Version 
----------------

The portable version of the HyperSpy Bundle does not interact with other Python installations, and
it can be safely installed alongside other Python distributions. As a portable distribution,
no shortcut is installed and it can be installed on an external harddrive or it can be moved to any other folder.

It is based on the `WinPython <https://winpython.github.io/>`_ distribution.

Difference with WinPython
^^^^^^^^^^^^^^^^^^^^^^^^^

It includes the additional libraries  :ref:`listed below <included_librairies-label>` - except ovito and conda-related libraries.


.. _included_librairies-label:

Included Software and Libraries
===============================

The HyperSpy-bundle distribution includes the following software and libraries:

.. include:: specs.rst

