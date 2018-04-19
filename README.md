# HyperSpy WinPython Bundle Distribution


A customised, installable [WinPython](http://winpython.github.io/) distribution
that includes HyperSpy and all its dependencies.

HyperSpy Bundle does not interact with any other Python
installation, so it can be safely installed alongside other
Python distributions. Moreover it is portable, so it can be installed to an USB
key.

## Differences with WinPython

* Includes HyperSpy and all its dependencies
* Installs (and uninstalls) like any other Windows package
* Adds a `HyperSpy Bundle` entry to the `Start Menu` to easily launch
  [Jupyter](https://jupyter.org) and [HyperSpyUI](http://hyperspy.org/hyperspyUI/) and the WinPython console.
* When installing with administrator rights for all users adds context
  (right-click) menu entries to start the Jupyter Notebook and Juypter QtConsole.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.

## Installation

See [Releases](https://github.com/hyperspy/hyperspy-bundle/releases) for download links.

Older releases are available in `GitHub <https://github.com/hyperspy/hyperspy/releases>`_.

**Note**: If HyperSpy fails to start you may need to install install the Visual C++ 2015
   (`x64 and x86 <https://www.visualstudio.com/downloads/download-visual-studio-vs#d-visual-c>`_
   for CPython 3.5) redistributable packages.

