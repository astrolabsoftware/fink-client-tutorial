# Fink client tutorials

## Goals for the tutorial

This repository contains short presentations about the status of the
Fink project and its roadmap until the full proposal submission (15/06/2020).
There are also tutorials to explore alert data and Fink client tools:

* Exploring ZTF Alerts
* Connect to Fink alert streams
* Fink filters: how they work?
* Fink science modules & broker added values
* Fink and external alert streams

Throughout all tutorials, we will use ZTF alert data that are currently available
and have similar structure to the expected one for LSST alerts.

## Before starting

1. Participants are expected to work from an Unix machine (mac/linux), with python3 installed (we recommend Anaconda). We cannot guarantee tutorials will work on Windows.
2. **Participants need an Internet connection:**
3. Install the `fink_client` (see instructions [here](https://github.com/astrolabsoftware/fink-client))
4. Make sure the installation went through properly
    ```bash
    # this should print a version >= 0.2.0
    python -c 'import fink_client; print(fink_client.__version__)'
    ```

## C'est parti!

Clone this repo, and open the `web/build/html/index.html` page:

```bash
git clone https://github.com/astrolabsoftware/fink-client-tutorial
cd fink-client-tutorial
open web/build/html/index.html
```

Then follow the tutorials one by one! Test data is under `datatest/`, solutions to exercises are under `solutions/`. For the the tutorials, you can use your favourite tool: Jupyter notebook, (i)python shell, scripts, IDE ...
