.. _usage-label:

Usage
=====

Managing libraries and conda environments
-----------------------------------------

.. note::
   For the standard version only, `i.e.` not supported for the portable version.

As an alternative to the Anaconda Navigator, the HyperSpy bundle includes
`gator <https://github.com/mamba-org/gator>`_ to manage libraries
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

.. _context_menu_shortcuts-label:

Context Menu Shortcuts
----------------------

The context menu shortcuts are created when the corresponding option has been selected
during :ref:`installation <install_windows-label>` using the
`start_jupyter_cm <https://github.com/hyperspy/start_jupyter_cm>`_ tool. Using these
shortcuts, the jupyter QtConsole / Lab / Notebook will start from the current folder.

.. figure:: _static/jupyter_cm_windows.png
   :width: 100 %
   :alt: Launching the interactive HyperSpy-bundle prompt console
   :figwidth: 40%

   Jupyter context menu entries.

.. _menu_shortcuts-label:

Menu Shortcuts
--------------

Start menu shortcuts are created when the corresponding option has been selected
during :ref:`installation <install_windows-label>`. The shortcuts are provided by
the conda packages and if further conda packages are installed and contain shortcuts,
they will appear in this menu.
The HyperSpy-bundle Prompt is a command line prompt with the base conda environment
activated and is useful to run conda/mamba, python scripts or programs from the
command line.

.. figure:: _static/windows_start_menu.png
   :width: 100 %
   :alt: Launching the interactive HyperSpy-bundle prompt console
   :figwidth: 45%

   Start menu shortcuts of the HyperSpy-bundle distribution.

.. note::
   Support for menu shorcuts on Linux and MacOS is possible since beginning of 2024
   and not packages currently supports it.
 

Installation alongside other Python Distribution
------------------------------------------------

The hyperspy-bundle will install a python distribution alongside existing python
distribution. The easiest way to use the python distribution installed by the
hyperspy-bundle is to use the shortcuts defined above
(:ref:`constext_menu <context_menu_shortcuts-label>` and :ref:`menu shortcut <menu_shortcuts-label>`).  



Alternatively, it is possible to:

* activate the desired environment from a terminal - 
  see `how to activate environment <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>`_
  from the conda documentation for more information.
* select the `desired kernel <https://jupyterlab.readthedocs.io/en/latest/user/running.html>`_
  from jupyter notebook or jupyterlab.

.. note::
   To check which python distribution you are using, you can import a library and find its location
   using the ``__file__`` attribute, for example:

   .. code:: python

      import hyperspy
      print("Location of the hyperspy library:", hyperspy.__file__)
   
   The path of the file will contain the path of the python distribution which should help you
   to identify which python distribution is being used.


.. note::
   ``conda``/``mamba`` uses a `configuration file <condarc_doc_>`_ (``.condarc``) to allow
   users to save ``conda`` settings. The hyperspy-bundle includes such a configuration file
   in the distribution but user-defined ``.condarc`` file saved in other location (for example,
   the *home* folder) can overwrite the default settings defined in the hyperspy-bundle.
   See the `conda documentation <condarc_doc_>`_ for more information on ``conda`` uses
   ``.condarc`` files.

.. _condarc_doc: https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html
