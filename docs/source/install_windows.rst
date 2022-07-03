.. _install_windows-label:

Run the installer ``.exe`` file, accepting the default options. Doing so will
install HyperSpy into the folder you choose under a subfolder named
``hyperspy-bundle``.

.. figure:: _static/just_me_windows.png
   :width: 100 %
   :alt: Just Me (recommended)
   :figwidth: 50%

   A screenshot of the installation type selection. It is recommended to install
   for single user only (`Just Me`) to avoid permission issues when using python.

.. note::
   For more details, for example on multi-users installation, read the
   `anaconda installation <https://docs.anaconda.com/anaconda/install/windows>`_
   instructions.

In the advanced installation options section, you can choose it you want to
create the start menu and the context menu (right-click) shortcuts.

.. figure:: _static/installation_options_windows.png
   :width: 100 %
   :alt: Installation options
   :figwidth: 50%

   The advanced installation options section, where you can choose to install
   start menu and context menu shortcuts.

Depending on your system, the installation may take quite some 
time (especially on the "Setting up the package cache..." and 
"Setting up the base environment..." steps), but you should get a progress 
window that looks like:

.. figure:: _static/bundle_during_installation.png
   :width: 100 %
   :alt: Bundle installation progress
   :figwidth: 50%

   A screenshot during the bundle installation process




And that's it! All the installed programs should now be installed and they
distribution should be available from the terminal, the context menu or the
start menu (:ref:`usage-label`).