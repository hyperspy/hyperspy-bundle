# HyperSpy WinPython Bundle Distribution


A customised, installable [WinPython](http://winpython.github.io/) distribution
that includes [HyperSpy](http://hyperspy.org/),
[HyperSpyUI](http://hyperspy.org/hyperspyUI/) and all their dependencies.

HyperSpy Bundle does not interact with any other Python
installation, so it can be safely installed alongside other
Python distributions. Moreover it is portable, so it can be installed to an USB
key.

## Differences with WinPython

* Includes [HyperSpy](http://hyperspy.org/),
  [HyperSpyUI](http://hyperspy.org/hyperspyUI/) and all their dependencies.
* Installs (and uninstalls) like any other Windows package
* Adds a `HyperSpy Bundle` entry to the `Start Menu` to easily launch
  [Jupyter](https://jupyter.org) and [HyperSpyUI](http://hyperspy.org/hyperspyUI/) and the WinPython console.
* When installing with administrator rights for all users adds context
  (right-click) menu entries to start the Jupyter Notebook and Juypter QtConsole.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.

## Download

See [Releases](https://github.com/hyperspy/hyperspy-bundle/releases) for download links.

Older releases (including HyperSpy <= 1.3) are available in [HyperSpy's GitHub repository](https://github.com/hyperspy/hyperspy/releases).

**Note**: If HyperSpy fails to start you may need to install install the Visual C++ 2015
   [x64 and x86](https://www.visualstudio.com/downloads/download-visual-studio-vs#d-visual-c)
   for CPython 3.5) redistributable packages.

