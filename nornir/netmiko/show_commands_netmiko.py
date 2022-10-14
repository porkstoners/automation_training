from nornir import InitNornir, init_nornir
from nornir_netmiko.tasks import netmiko_send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")

def another_show_command_test(task):
    task.run(task=netmiko_send_commands, command_string="show ip int br")

results = nr.run(task=another_show_command_test)
print_result(results)