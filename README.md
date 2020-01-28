<p align="center">
<a href="https://github.com/hyperspy/hyperspy-bundle/releases"><img src="./images/download_button.png"></a>
</p>


# HyperSpy Bundle Distribution

## Conda based distribution

This distribution is very similar to the Anaconda distribution and is available for Windows, MacOSX and Linux.
It is built using the [constructor](https://github.com/conda/constructor) tool, which is used to build the
anaconda and miniconda distribution. It uses the conda package manager.

### Differences with Anaconda/Miniconda

* The conda packages are download from the *anaconda main*, *conda-forge* channels in this order of priority 
  and these channels are set up in the installed environment.
* Adds context menu entries (right-click shortcut) to start the *Jupyter Notebook*, *Jyputer Lab* or *Juypter QtConsole*.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.
* Remove context menu entries when uninstalling on Windows only. For Linux and MaxOSX, no uninstall is provided and
  the context menu entries needs to be removed manually using `start_jupyter_cm --remove` from the conda environment before
  deleting the distribution.

## Winpython based distribution

A customised, installable [WinPython](http://winpython.github.io/) distribution
that includes [HyperSpy](http://hyperspy.org/),
[HyperSpyUI](http://hyperspy.org/hyperspyUI/) and all their dependencies.

HyperSpy Bundle does not interact with any other Python installation, so it can be safely installed alongside other
Python distributions. Moreover it is portable, so it can be installed to an USB
key.

### Differences with WinPython

* Includes [HyperSpy](http://hyperspy.org/),
  [HyperSpyUI](http://hyperspy.org/hyperspyUI/) and all their dependencies.
* Installs (and uninstalls) like any other Windows package
* Adds a `HyperSpy Bundle` entry to the `Start Menu` to easily launch
  [Jupyter](https://jupyter.org) and [HyperSpyUI](http://hyperspy.org/hyperspyUI/) and the WinPython console.
* Adds context (right-click) menu entries to start the *Jupyter Notebook*, *Jyputer Lab* or *Juypter QtConsole*.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.

## Download

See [Releases](https://github.com/hyperspy/hyperspy-bundle/releases) for download links.

Older releases (including HyperSpy <= 1.3) are available in [HyperSpy's GitHub repository](https://github.com/hyperspy/hyperspy/releases).

**Note**: If HyperSpy fails to start you may need to install install the Visual C++ 2015
   [x64 and x86](https://www.visualstudio.com/downloads/download-visual-studio-vs#d-visual-c)
   for CPython 3.5) redistributable packages.

