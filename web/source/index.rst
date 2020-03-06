=====================================
Fink client tutorial
=====================================

  *Feb 2020 version*


**Goals for the tutorial**

This repository contains short presentations about the status of the
Fink project and its roadmap until the full proposal submission (15/06/2020).
There are also tutorials to explore alert data and Fink tools. Participants will learn what is an alert and what it contains,
how to connect to Fink streams, build a Fink filter, a Fink science module, and interface
external alert streams to Fink.

Throughout all tutorials, we will use ZTF alert data that are currently available
and have similar structure to the expected one for LSST alerts.

**Before starting**

1. Participants are expected to work from an Unix machine (mac/linux), with python3 installed (we recommend Anaconda). We cannot guarantee tutorials will work on Windows.
2. **Participants need an Internet connection:**
3. You will also need to have `fink_client>=0.2` installed with dependencies:

.. code-block:: bash

  # Install fink-client somewhere on your computer
  git clone https://github.com/astrolabsoftware/fink-client
  cd fink-client
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt


Then, assuming you are using bash shell, update your `~/.bash_profile` with the path to the library and binaries:

.. code-block:: bash

  # Add these lines at the end of your ~/.bash_profile
  export FINK_CLIENT_HOME=${PWD}
  export PYTHONPATH=${FINK_CLIENT_HOME}:$PYTHONPATH
  export PATH=${FINK_CLIENT_HOME}/bin:$PATH


Finally source the file to activate the changes, and check the correct installation:

.. code-block:: bash

  source ~/.bash_profile
  python -c 'import fink_client; print(fink_client.__version__)'
  # should print 0.2.0

Tutorials
--------------

There will be 2h for tutorials. The first three are expected to be done
within the 2h - and the others can be done at home later.

.. toctree::
  :maxdepth: 1
  :numbered:

  Exploring ZTF Alerts                     <tasks/display_ztf_alerts.md>
  Connect to Fink alert streams            <tasks/stream-connection.md>
  Fink filters: how they work?             <tasks/fink-filters.md>
  Fink science modules & broker added values                   <tasks/fink-science.md>
  Fink and external alert streams          <tasks/fink-voevent.md>
  Afterword                                <tasks/afterword.md>
