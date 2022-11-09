import sys
import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

""" 
Script uses the argv module - this takes an argument after the script name which is the default username. 
e.x > "python3 pass_arguments_into_script.py arista"
For any devices that dont have their username hardcoded in either the groups or the hosts .yaml file will use the arista username
In this example the devices in aristanorth and aristasouth have their usernames set via the group but telx-colo does not so it will
use the argument provided by the default value. This means we do not need to hardcode a default value into our script which is a good thing.   
"""

nr = InitNornir(config_file="config.yaml")

north_password = getpass.getpass(prompt="Enter the north group password: ")
south_password = getpass.getpass(prompt="Enter the south group password: ")
telx_colo = getpass.getpass(prompt="Enter telex-colo password: ")

nr.inventory.groups["north"].password = north_password
nr.inventory.groups["south"].password = south_password
nr.inventory.hosts["telx-colo"].password = telx_colo
nr.inventory.defaults.username = sys.argv[1] # Specifies the command line argument for default username (e.x python3 script1.py arista) 

def credentials_test(task):
    task.run(send_command, command="show ip int br")

results = nr.run(task=credentials_test)
print_result(results)

