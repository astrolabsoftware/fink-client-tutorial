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

  pip install fink-client

Finally, in order to connect and poll alerts from Fink, you need to get your credentials:

1. Subscribe to one or more Fink streams at https://forms.gle/2td4jysT4e9pkf889.
2. After filling the form, we will send your credentials. Register them on your laptop by simply running:
  ```
  # You need fink-client installed - see above
  fink_client_register -username <USERNAME> -group_id <GROUP_ID> ...
  ```

Tutorials
--------------

The tutorials should take around 2h. The first three are the most important for users
and they are expected to be doable within the 2h.
The other tutorials expose more complex parts of the broker.

.. toctree::
  :maxdepth: 1
  :numbered:

  Exploring ZTF Alerts                     <tasks/display_ztf_alerts.md>
  Connect to Fink alert streams            <tasks/stream-connection.md>
  Fink filters: how they work?             <tasks/fink-filters.md>
  Fink science modules & broker added values                   <tasks/fink-science.md>
  Fink and external alert streams          <tasks/fink-voevent.md>
  Afterword                                <tasks/afterword.md>
