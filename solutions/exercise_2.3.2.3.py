# Copyright 2020 AstroLab Software
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Poll the Fink servers only once at a time, plot alert, and save it.
reject alerts that are too close to a known Solar System object.
"""
from fink_client.consumer import AlertConsumer
from fink_client.configuration import load_credentials

from fink_client.visualisation import show_stamps
from fink_client.visualisation import extract_field

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import argparse

# For plots
font = {
    'weight': 'bold',
    'size': 22
}

matplotlib.rc('font', **font)

# Bands
filter_color = {1: '#1f77b4', 2: '#ff7f0e', 3: '#2ca02c'}
# [
#     '#1f77b4',  # muted blue
#     '#ff7f0e',  # safety orange
#     '#2ca02c',  # cooked asparagus green
#     '#d62728',  # brick red
#     '#9467bd',  # muted purple
#     '#8c564b',  # chestnut brown
#     '#e377c2',  # raspberry yogurt pink
#     '#7f7f7f',  # middle gray
#     '#bcbd22',  # curry yellow-green
#     '#17becf'   # blue-teal
# ]
filter_name = {1: 'g band', 2: 'r band', 3: 'i band'}

def is_close_to_sso(alert: dict) -> bool:
    """ Check if the alert is close to a known solar system object.

    Note that a value of -999.0 means no information, and the alert will be
    considered as NOT close to a solar system object.

    Parameters
    ----------
    alert: dict
        Alert data in a dictionary.
    """
    # Distance & name to known solar system object
    ssdistnr = alert['candidate']['ssdistnr']
    ssnamenr = alert['candidate']['ssnamenr']

    # Note that a value of -999.0 means no information.
    if ssdistnr > 0 and ssdistnr < 5:
        msg = """
        WARNING: alert close to known solar system object:
        {} arcsec from {}
        """.format(ssdistnr, ssnamenr)
        print(msg)
        return True
    return False


def plot_alert_data(alert: dict) -> None:
    """ Plot alert data (stamps and lightcurve)

    Parameters
    ----------
    alert: dict
        Dictionary containing alert data.
    """
    fig = plt.figure(num=0, figsize=(12, 4))
    show_stamps(alert, fig)

    # extract current and historical data as one vector
    mag = extract_field(alert, 'magpsf')
    error = extract_field(alert, 'sigmapsf')
    upper = extract_field(alert, "diffmaglim")

    # filter bands
    fid = extract_field(alert, "fid")

    # Rescale dates to end at 0
    jd = extract_field(alert, "jd")
    dates = np.array([i - jd[0] for i in jd])

    # Title of the plot (alert ID)
    title = alert["objectId"]

    # loop over filters
    fig = plt.figure(num=1, figsize=(12, 4))

    # Loop over each filter
    for filt in filter_color.keys():
        mask = np.where(fid == filt)[0]

        # Skip if no data
        if len(mask) == 0:
            continue

        # y data
        maskNotNone = mag[mask] != None
        plt.errorbar(
            dates[mask][maskNotNone], mag[mask][maskNotNone],
            yerr=error[mask][maskNotNone],
            color=filter_color[filt], marker='o',
            ls='', label=filter_name[filt], mew=4)
        # Upper limits
        plt.plot(
            dates[mask][~maskNotNone], upper[mask][~maskNotNone],
            color=filter_color[filt], marker='v', ls='', mew=4, alpha=0.5)
        plt.title(title)
    plt.legend()
    plt.gca().invert_yaxis()
    plt.xlabel('Days to candidate')
    plt.ylabel('Difference magnitude')
    plt.show()

def poll_single_alert(outdir: str) -> (str, dict):
    """ Connect to and poll fink servers once.

    Parameters
    ----------
    outdir: str
        Directory to store incoming alerts. It must exist.

    Returns
    ---------
    topic: str
        Topic name. None if no alert has been returned from the servers.
    alert: dict
        Alert data in a dictionary.
        None if no alert has been returned from the servers.
    """
    # Load configuration parameters
    conf = load_credentials()

    myconfig = {
        "username": conf['username'],
        'bootstrap.servers': conf['servers'],
        'group_id': conf['group_id']}

    if conf['password'] is not None:
        myconfig['password'] = conf['password']

    # Instantiate a consumer
    consumer = AlertConsumer(conf['mytopics'], myconfig)

    # Poll the servers
    topic, alert = consumer.poll_and_write(outdir, conf['maxtimeout'])

    # Analyse output
    if topic is not None:
        # Distance to known solar system object
        ssdistnr = alert['candidate']['ssdistnr']

        print("-" * 65)
        row = [
            alert['timestamp'], topic, alert['objectId'],
            alert['cdsxmatch'], alert['rfscore'], ssdistnr
        ]
        print("{:<25}|{:<10}|{:<15}|{:<10}|{:<5}|{:<10}".format(*row))
    else:
        print(
            'No alerts received in the last {} seconds'.format(
                conf['maxtimeout']))

    # Close the connection to the servers
    consumer.close()

    return topic, alert


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-outdir', type=str, default='.',
        help="Folder to store incoming alerts. It must exist.")
    args = parser.parse_args(None)

    topic, alert = poll_single_alert(args.outdir)

    if topic is not None and not is_close_to_sso(alert):
        plot_alert_data(alert)
