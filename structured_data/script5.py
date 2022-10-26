from textwrap import indent
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb
from rich import print as rprint    

nr = InitNornir(config_file="config.yaml")

""" This script uses TextFsm to parse data and present it in a structured format
    The example below looks at the interfaces and pulls details from the show version command
    When using TextFSM there are only certain commands that are mapped for Arista. 
    An example is show interface and show version
    You can check the support commands by running the following from you python venv with text fsm installed
    find | grep textfsm | grep arista 
    or from the github page - https://github.com/networktocode/ntc-templates/tree/master/ntc_templates/templates and search for Arista
"""

def pull_structured_data(task):
    version_result = task.run(task=send_command, command="show version")
    task.host["facts"] = version_result.scrapli_response.textfsm_parse_output()
    sw_version = nr.inventory.hosts['ny5-feed-sw1a']['facts'][0]['image']
    serial_number = nr.inventory.hosts['ny5-feed-sw1a']['facts'][0]['serial_number']
    memory = nr.inventory.hosts['ny5-feed-sw1a']['facts'][0]['total_memory']
    rprint(f"\n ### {task.host} ###\n sw_version: {sw_version}\n serial number:{serial_number}\n memory: {memory}")
    
    #interface_name = task.host["facts"][0]['interface']
    #interface_status = task.host["facts"][0]["bia"]
    #rprint(f"{task.host}:\n{interface_name} mac address: {interface_status}\n")




results = nr.run(task=pull_structured_data)
#print_result(results)

"""
You can enable ipdb trace to break into the debugger once the script has run - this is useful for checking paths 
in the parsed data.
Example

pp nr.inventory.hosts["cart-colo"]["facts"]
pp nr.inventory.hosts["cart-colo"]["facts"][2]["protocol_status"]


"""
#ipdb.set_trace()

    