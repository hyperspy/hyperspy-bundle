.. _contribute-label:

Development
===========

How is the HyperSpy-bundle made
-------------------------------

The development of the hyperspy-bundle takes place at the 
`hyperspy/hyperspy-bundle <https://github.com/hyperspy/hyperspy-bundle>`_ github
repository.
All installers are automatically built and tested using the
`GitHub actions <https://github.com/hyperspy/hyperspy-bundle/actions>`_ platforms.
The anaconda/miniforge-like version is built using
`constructor <https://github.com/conda/constructor>`_ and
`conda-forge <https://conda-forge.org/>`_ packages.

The portable version is built by installing relevant libraries in
`WinPython <https://winpython.github.io/>`_ and compressing the distribution into to a 7zip auto-extracting archives.

Release
-------

Releases are made when the need arises, typically when new software or libraries are
available or changes in the conda-forge infrastructure which would benefit users.

Changelog
---------

The changelog is available on `GitHub <https://github.com/hyperspy/hyperspy-bundle/releases>`_.