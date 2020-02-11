# Fink workshop, 6 February 2020 @ IJCLab

Welcome to the first Fink Workshop!

## Goals for the workshop

This first Fink workshop contains short presentations about the status of the
Fink project and its roadmap until the full proposal submission (15/06/2020).
There are also tutorials to explore alert data and Fink tools:

* Exploring ZTF Alerts
* Connect to Fink alert streams
* Fink filters: how they work?
* Fink science modules & broker added values
* Fink and external alert streams

Throughout all tutorials, we will use ZTF alert data that are currently available
and have similar structure to the expected one for LSST alerts.

## How to reach the room

The workshop will be held at **IJCLab (ex-LAL, building 200), room 101**. IJCLab is a laboratory situated on the Orsay Campus, 30km south from Paris center.

- From Paris to Orsay: From Paris center, take the `RER B` southward (`Saint-Rémy-Lès-Chevreuse` direction). Stop at `Orsay-ville` station.
- From Orsay RER station to IJCLab: [Google Maps direction](https://goo.gl/maps/BpdAiKeU9gpzGJkx9). It is a 15min walk inside the campus. Ask for LAL or building 200 if you are lost.
- In IJCLab: Enter the building (you might have to ring), and turn right. Pass 3 doors until you find a stairway on your left. Climb the stairs and the `room 101` is located at the top of the stairs on the right.

## Before starting

1. Participants are expected to work from an Unix machine (mac/linux), with python3 installed (we recommend Anaconda). We cannot guarantee tutorials will work on Windows.
2. **Participants need an Internet connection:** eduroam should be available on the room, so make sure you get an account before the workshop!
3. Install the `fink_client` (see instructions [here](https://github.com/astrolabsoftware/fink-client))
4. Make sure the installation went through properly
    ```bash
    # this should print a version >= 0.2.0
    python -c 'import fink_client; print(fink_client.__version__)'
    ```

## C'est parti!

Clone this repo (and you can even give it a star - to ease its retrieval, and well... increase its visibility as well), walk to `fink_workshop_06022020`, and open the `web/build/html/index.html` page:

```bash
git clone https://github.com/astrolabsoftware/fink-tutorials
cd fink-tutorials/fink_workshop_06022020
open web/build/html/index.html
```

Then follow the tutorials one by one! Test data is under `datatest/`, solutions to exercises are under `solutions/`. For the the tutorials, you can use your favourite tool: Jupyter notebook, (i)python shell, scripts, IDE ...
