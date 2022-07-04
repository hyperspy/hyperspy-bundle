.. _usage-label:

Usage
-----

Managing librairies and conda environements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   For standard version only, i.e. not supported for the portable version.

As an alternative to the Anaconda Navigator, the HyperSpy bundle includes
`gator <https://github.com/mamba-org/gator#gator>`_ to manage libraries
and conda environments.

.. figure:: _static/gator.png
   :width: 100 %
   :alt: Managing environments and libraries using gator
   :figwidth: 100%

   Managing environments and libraries using gator.

The packages can also be managed from the command line using
`conda <https://docs.conda.io/projects/conda>`__ or
`mamba <https://mamba.readthedocs.io>`__.
For example, the distribution can be updated easily using

.. code::

   $ conda update --all

or

.. code::

   $ mamba update --all

.. note::
   `conda <https://docs.conda.io/projects/conda>`__ is usually slow,
   when the distribution contains many libraries, as
   is the case for the hyperspy-bundle. `Mamba <https://mamba.readthedocs.io>`__
   is a fast drop-in replacement for conda.


Start Menu (Windows only)
^^^^^^^^^^^^^^^^^^^^^^^^^

Start menu shortcuts are created when the corresponding option have been selected
during :ref:`installation <install_windows-label>`. The HyperSpy-bundle Prompt is
a command line prompt with the base conda environment activated.

.. figure:: _static/windows_start_menu.png
   :width: 100 %
   :alt: Launching the interactive HyperSpy-bundle prompt console
   :figwidth: 50%

   Start menu shortcuts of the HyperSpy-bundle distribution.

Context Menu Shortcuts
^^^^^^^^^^^^^^^^^^^^^^

The context menu shortcuts are created when the corresponding option have been selected
during :ref:`installation <install_windows-label>` using the
`start_jupyter_cm <https://github.com/hyperspy/start_jupyter_cm>`_ tool. Using these
shortcuts, the jupyter QtConsole / Lab / Notebook will start from the current folder.

.. figure:: _static/jupyter_cm_windows.png
   :width: 100 %
   :alt: Launching the interactive HyperSpy-bundle prompt console
   :figwidth: 50%

   Jupyter context menu entries in windows.
