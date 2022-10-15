from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")

def send_more_commands(task):
    task.run(task=netmiko_send_config, config_file="/opt/Training/python/automation_training/nornir/netmiko/config.txt")

results = nr.run(task=send_more_commands)
print_result(results)

