from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")

""" 
Look at the Napalm page for support commands
https://napalm.readthedocs.io/en/latest/support/index.html#list-of-supported-optional-arguments
You can specify a VRF if needed by adding vrf="{vrf_name}

"""

def ping_a_host(task):
    task.run(task=napalm_ping, dest="8.8.8.8")

results = nr.run(task=ping_a_host)
print_result(results)

