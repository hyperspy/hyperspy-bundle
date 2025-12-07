Download one of the installers in the `"Assets"` section.

See below the information to select the most suitable installer for a given platform (`Windows`, `Linux` or `Mac`) and architecture / type (`AMD`, `Intel`, `Silicon`, `Portable`).

## Recommended: Anaconda-type distribution (Linux, MacOS and Windows)

The HyperSpy bundle is similar to the [Miniforge](https://github.com/conda-forge/miniforge)/[Anaconda](https://docs.anaconda.com/anaconda/) distribution and uses the `conda` or `mamba` package manager.

**[Installation instructions](https://hyperspy.org/hyperspy-bundle/install.html)**

For Windows and Linux, there is the choice between two variants:
- `Intel`: optimised for Intel architecture (uses the MKL library),
- `AMD`: optimised for AMD architecture (uses the openblas library).

For Mac, there are also two variants available:
- `Intel` for Mac computers with Intel CPU, with the MKL library
- `Silicon` for Mac computers with Apple Silicon (M1, M2, etc.) CPU, with the Accelerate library

For included packages, [see documentation](https://hyperspy.org/hyperspy-bundle/index.html#included-software-and-libraries).

This distribution is built using [constructor __CONSTRUCTOR_VERSION__](https://conda.github.io/constructor).

## Portable (Windows only)
The portable distribution is based on the [WinPython](https://winpython.github.io) distribution and is a self-extracting archive. Running the installer will install the distribution in the current directory. Since the distribution is portable, it can be moved to any directory or run from an external drive.


