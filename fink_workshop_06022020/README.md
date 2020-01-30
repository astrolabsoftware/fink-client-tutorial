# Fink workshop, 6 February 2020 @ IJCLab

Welcome to the first Fink Workshop!

## Goals for the workshop

This first Fink workshop contains short presentations about the status of the
Fink project and its roadmap until the full proposal submission (15/06/2020).
There are also tutorials to explore alert data and Fink tools. Participants will learn what is an alert and what it contains,
how to connect to Fink streams, build a Fink filter, a Fink science module, and interface external alert streams to Fink.

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
3. You will also need to have `fink_client>=0.2` installed with dependencies:

```bash
# Install fink-client somewhere on your computer
git clone https://github.com/astrolabsoftware/fink-client
cd fink-client
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Then, assuming you are using bash shell, update your `~/.bash_profile` with the path to the library and binaries:

```bash
# Add these lines at the end of your ~/.bash_profile
export FINK_CLIENT_HOME=${PWD}
export PYTHONPATH=${FINK_CLIENT_HOME}:$PYTHONPATH
export PATH=${FINK_CLIENT_HOME}/bin:$PATH
```

Finally source the file to activate the changes, and check the correct installation:

```bash
source ~/.bash_profile
python -c 'import fink_client; print(fink_client.__version__)'
# should print 0.2.0
```

## Get started

Tutorials and instruction are located under `docs.zip`. Clone this repo (and you can even give it a star - to ease its retrieval, and well... increase its visibility as well), walk to `fink_workshop_06022020`, unzip the file, and open the `docs/html/index.html` page:

```bash
git clone https://github.com/astrolabsoftware/fink-tutorials
cd fink_workshop_06022020
unzip -o docs.zip
open docs/html/index.html
```

Then follow the tutorials one by one! Test data is under `datatest/`, solutions to exercises are under `solutions/`. For the the tutorials, you can use your favourite tool: Jupyter notebook, (i)python shell, scripts, IDE ...
