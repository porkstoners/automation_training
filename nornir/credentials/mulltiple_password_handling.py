import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

""" 
## Use multiple passwords in an environment - manual prompt
Script uses the getpass module to prompt for a password
Variable is called when referencing the group or host object    
"""

nr = InitNornir(config_file="config.yaml")
north_password = getpass.getpass(prompt="Enter the north group password: ")
south_password = getpass.getpass(prompt="Enter the south group password: ")
telx_colo = getpass.getpass(prompt="Enter telex-colo password: ")

nr.inventory.groups["north"].password = north_password
nr.inventory.groups["south"].password = south_password
nr.inventory.hosts["telx-colo"].password = telx_colo


def credentials_test(task):
    task.run(send_command, command="show ip int br")

results = nr.run(task=credentials_test)
print_result(results)

