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
""" Poll the Fink servers only once at a time """
from fink_client.consumer import AlertConsumer
from fink_client.configuration import load_credentials

def poll_single_alert() -> None:
    """ Connect to and poll fink servers once.
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
    topic, alert = consumer.poll(conf['maxtimeout'])

    # Analyse output
    if topic is not None:
        print("-" * 65)
        row = [
            alert['timestamp'], topic, alert['objectId'],
            alert['cdsxmatch'], alert['rfscore']
        ]
        print("{:<25}|{:<10}|{:<15}|{:<10}|{:<5}|".format(*row))
    else:
        print(
            'No alerts received in the last {} seconds'.format(
                conf['maxtimeout']
            )
        )

    # Close the connection to the servers
    consumer.close()


if __name__ == "__main__":
    """ Poll the servers only once at a time """
    poll_single_alert()
