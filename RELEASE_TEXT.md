The HyperSpy bundle is similar to the [Miniforge](https://github.com/conda-forge/miniforge)/[Anaconda](https://docs.anaconda.com/anaconda/) distribution and uses the `conda` or `mamba` package manager.

**[Installation instructions](https://hyperspy.org/hyperspy-bundle/install.html)**

## Recommended: Anaconda-type distribution (Linux, MacOS and Windows)

For Windows and Linux, there is the choice between two variants, which are optimised for Intel or AMD CPUs:
- `Intel`: with the MKL library,
- `AMD`: with the openblas library.

For Mac, there are also two variants available:
- `Intel` for Mac computers with Intel CPU, with MKL library
- `Silicon` for Mac computers with Apple Silicon (M1, M2, etc.) CPU, with the Accelerate library

For included packages, [see documentation](https://hyperspy.org/hyperspy-bundle/index.html#included-software-and-libraries).

This distribution is built using [constructor 3.6.0](https://github.com/conda/constructor).

## Portable (Windows only)
The portable distribution is based on the [WinPython](https://winpython.github.io) distribution and is a self-extracting archive. Running the installer will install the distribution in the current directory. Since the distribution is portable, it can be moved to any directory or run from an external drive.


