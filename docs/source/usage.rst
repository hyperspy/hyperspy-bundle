.. _usage-label:

Usage
-----

Start Menu (Windows only)
^^^^^^^^^^^^^^^^^^^^^^^^^


Context Menu shortcuts
^^^^^^^^^^^^^^^^^^^^^^

The context menu shortcuts will be installed.

Jupyter Notebook
^^^^^^^^^^^^^^^^



Jupyter QtConsole
^^^^^^^^^^^^^^^^^


If you would like to test that your installation is working properly, you can
run a small test example by opening the "Qt Console". This is an interactive
Python interpreter that allows you to type in Python statements directly. You
can start the Qt Console from within the "Miniforge Prompt", which you will
find in the Start Menu:

.. figure:: _static/bundle_test_qtconsole.png
   :width: 100 %
   :alt: Launching the interactive Miniforge prompt console
   :figwidth: 50%

   Launching the interactive Miniforge Prompt from the Start Menu

Once the Miniforge prompt opens, type ``jupyter qtconsole`` and press "Enter"
to launch the QT Console:

.. figure:: _static/bundle_launching_qtconsole.png
   :width: 100 %
   :alt: Launching the QT Console from the Miniforge prompt
   :figwidth: 50%

   Launching the QT console from the Miniforge prompt

.. include:: testing_install.rst

The Qt Console is an interactive Python interpreter that allows you to enter
Python statements directly and immediately see their output. Once the console
has opened and you see a prompt that says ``In [1]:``, copy the following code
snippet at the location of the blinking cursor:

..  code-block:: python

    %matplotlib qt
    import hyperspy.api as hs
    s = hs.datasets.artificial_data.get_core_loss_eels_signal(add_powerlaw=True)
    s.remove_background()

Very briefly, this code is loading the interactive plotting libraries, loading
HyperSpy, creating an example EELS signal from some artificial data, and then
telling the interpreter you want to interactively remove the Power Law
background. Press ``Shift-Enter`` within the console to run the lines of code
you pasted in (it may take a few moments to run if this is the first time
you've used HyperSpy on your machine):

.. figure:: _static/bundle_test_qtconsole_code.png
   :width: 100 %
   :alt: Entering the example code into the Qt Console
   :figwidth: 70%

   Entering the example code into the Qt Console

Eventually, you should see a spectrum window and a small tool window for
removing the background open (they may be stacked on top of each other;
drag them out of the way, if so). If you click and drag on part of the spectrum
display, HyperSpy will fit a Power Law to the signal within that region,
and also show you a preview of the background-subtracted signal:

.. figure:: _static/bundle_test_bgremoval.gif
   :width: 100 %
   :alt: Removing the background from a test signal
   :figwidth: 90%

   By clicking and dragging on the spectrum display, a region is created (shown
   in red). The fitted background is shown in blue, and a preview of the
   background-subtracted signal is displayed in green.

Clicking "OK" in the *Background removal tool* window will perform the
background subtraction, and replace the window with one showing the resulting
signal:

.. figure:: _static/bundle_test_bgremoval_sig.png
   :width: 100 %
   :alt: Removing the background from a test signal
   :figwidth: 50%


