The HyperSpy bundle is now based on the [Anaconda](https://docs.anaconda.com/anaconda/) distribution and uses the `conda` or `mamba` package manager.

**[Installation instructions](https://github.com/hyperspy/hyperspy-bundle#hyperspy-bundle-distribution)**

## Recommenced: Anaconda-type distribution (Linux, MacOS and Windows)

For Windows and Linux, there is the choice between two variants, which are optimised for Intel or AMD CPUs:
- `Intel`: with the MKL libraries,
- `AMD`: with the openblas libraries.

For included packages, [see construct.yaml](https://github.com/hyperspy/hyperspy-bundle/blob/__TAG__/conda_distribution/construct.yaml#L17-L42)

This distribution is built using [constructor 3.2.1](https://github.com/conda/constructor).

## Portable (Windows only)
The portable distribution is based on the [WinPython](https://winpython.github.io) distribution and is a self-extracting archive. Running the installer will install the distribution in the current directory. Since the distribution is portable it can be moved to any directory or run from an external drive.


