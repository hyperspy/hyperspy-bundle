<p align="center">
<a href="https://github.com/hyperspy/hyperspy-bundle/releases"><img src="./images/download_button.png"></a>
</p>


# HyperSpy Bundle Distribution

These python distributions include:
- [HyperSpy](https://hyperspy.org)
- [HyperSpyUI](https://hyperspy.org/hyperspyUI)
- [atomap](https://atomap.org)
- [pyxem](www.pyxem.org)
- [kikuchipy](https://kikuchipy.org)

## Conda based distribution

This distribution is very similar to the Anaconda distribution and is available for Windows, MacOSX and Linux.
It is built using the [constructor](https://github.com/conda/constructor) tool, which is used to build the
anaconda and miniconda distribution. It uses the conda package manager.

### Installation

Run the installer. *Single user* installation is recommended.
For more details, see the [Anaconda installation instructions](https://docs.anaconda.com/anaconda/install).

On MacOSX, the installer is currently not identified as trusted party by macOS, meaning that macOS will not allow
to run the installer simply by double-clicking on it. However, control-clicking the app icon, then choosing Open
from the shortcut menu will allow to run the installer, as explained in the [macOS documentation](https://support.apple.com/en-gb/guide/mac-help/mh40616/mac).


### Differences with Anaconda/Miniconda

* Include the packages mentioned above
* The conda packages are download from the *anaconda main*, *conda-forge* channels in this order of priority 
  and these channels are set up in the installed environment.
* Adds context menu entries (right-click shortcut) to start the *Jupyter Notebook*, *Jyputer Lab* or *Juypter QtConsole*.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.
* Remove context menu entries when uninstalling on Windows only. For Linux and MaxOSX, no uninstall is provided and
  the context menu entries needs to be removed manually using `start_jupyter_cm --remove` from the conda environment before
  deleting the distribution.

### Silent installation on Windows

```
start /wait "" HyperSpy-bundle-2020.02.05-Windows-x86_64.exe /S /D=%UserProfile%\HyperSpy-bundle
```

See the [Anaconda documentation](https://docs.anaconda.com/anaconda/install/silent-mode) for more information.

## Winpython based distribution (Portable)

HyperSpy Bundle does not interact with any other Python installation, so it can be safely installed alongside other
Python distributions. Since it is a portable distribution, it can be installed on external harddrive or it can be moved to any other
folder.

### Installation

Run the installer (self-extracting archive), the distribution will be installed in the current folder.

### Differences with WinPython

* Include the packages mentioned above.

## Download

See [Releases](https://github.com/hyperspy/hyperspy-bundle/releases) for download links.

Older releases (including HyperSpy <= 1.3) are available in [HyperSpy's GitHub repository](https://github.com/hyperspy/hyperspy/releases).
