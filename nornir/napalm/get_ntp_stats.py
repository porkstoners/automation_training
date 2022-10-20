from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")

""" 
Look at the Napalm page for support commands
https://napalm.readthedocs.io/en/latest/support/index.html#list-of-supported-optional-arguments

"""

def get_running_config(task):
    task.run(task=napalm_get, getters="get_route_to(8.8.8.8)")

results = nr.run(task=get_running_config)
print_result(results)



