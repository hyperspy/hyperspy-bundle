<p align="center">
<a href="https://github.com/hyperspy/hyperspy-bundle/releases"><img src="./images/download_button.png"></a>
</p>


# HyperSpy Bundle Distribution

These python distributions include:
- [ase](https://wiki.fysik.dtu.dk/ase)
- [atomap](https://atomap.org)
- [HyperSpy](https://hyperspy.org)
- [HyperSpyUI](https://hyperspy.org/hyperspyUI)
- [LumiSpy](https://github.com/LumiSpy/lumispy)
- [kikuchipy](https://kikuchipy.org)
- [particlespy](https://epsic-dls.github.io/ParticleSpy/index.html)
- [pystackreg](https://github.com/glichtner/pystackreg)
- [pyxem](www.pyxem.org)
- [nglview](http://nglviewer.org/nglview/latest)


## Anaconda-type distribution

This distribution is very similar to the Anaconda distribution and is available for Windows, MacOSX and Linux.
It is built using the [constructor](https://github.com/conda/constructor) tool, which is used to build the
anaconda and miniconda distribution. It uses the conda package manager.

### Installation

Run the installer. *Single user* installation is recommended.
For more details, see the [Anaconda installation instructions](https://docs.anaconda.com/anaconda/install).

On MacOSX, the installer is currently not identified as trusted party by macOS, meaning that macOS will not allow
to run the installer simply by double-clicking on it. However, control-clicking the app icon, then choosing Open
from the shortcut menu will allow to run the installer, as explained in the [macOS documentation](https://support.apple.com/en-gb/guide/mac-help/mh40616/mac).

### Package manager (GUI)

As an alternative to the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/index.html), the HyperSpy bundle includes
[`mamba_gator`](https://github.com/mamba-org/gator) to manage conda environments and packages.

### Command prompt on Windows

Similarly to the `Anaconda Prompt` shortcut available in the Anaconda distribution, the HyperSpy bundle provides a start menu shortcut of a command prompt with the base environment activated and it is called `Miniforge Prompt`.

### Differences with Anaconda/Miniconda

* Include the libraries and software mentioned above.
* The packages are download from the [*conda-forge*](https://conda-forge.org) channel only to avoid incompatibilities between the anaconda defaults and conda-forge channels.
* Include the `mamba` package manager, as faster alternative to `conda`.
* A configuration file `condarc` is added in the root folder of the installation to save the channels setting and pin the blas implementation.
* Adds context menu entries (right-click shortcut) to start the *Jupyter Notebook*, *Jupyter Lab* or *Juypter QtConsole*.
  See [start_jupyter_cm](https://github.com/hyperspy/start_jupyter_cm) for details.
* Remove context menu entries when uninstalling on Windows only. For Linux and MaxOSX, no uninstall is provided and
  the context menu entries needs to be removed manually using `start_jupyter_cm --remove` from the conda environment before
  deleting the distribution.

### Silent installation on Windows

Using the command prompt
```
start /wait "" HyperSpy-bundle-2020.02.05-Windows-x86_64.exe /S /D=%UserProfile%\HyperSpy-bundle
```

Using PowerShell
```
Start-Process -Wait -FilePath HyperSpy-bundle-2020.02.05-Windows-x86_64.exe -ArgumentList /S /D=$env:UserProfile\HyperSpy-bundle
```

See the [Anaconda documentation](https://docs.anaconda.com/anaconda/install/silent-mode) for more information.

## Portable distribution

The portable version of the HyperSpy Bundle does not interact with other Python installation, and it can be safely installed alongside other Python distributions. As a portable distribution, no shortcut is installed and it can be installed on external harddrive or it can be moved to any other folder.

### Installation

Run the installer (self-extracting archive), the distribution will be installed in the current folder.

### Differences with WinPython

* Include the packages mentioned above.

## Download

See [Releases](https://github.com/hyperspy/hyperspy-bundle/releases) for download links.

Older releases (including HyperSpy <= 1.3) are available in [HyperSpy's GitHub repository](https://github.com/hyperspy/hyperspy/releases).
