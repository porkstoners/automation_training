from nornir import InitNornir, init_nornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")
commands = ['show ip int br', 'show version', 'show int status']

def another_show_command_test(task):
    for cmd in commands:
        task.run(task=netmiko_send_command, command_string=cmd)

results = nr.run(task=another_show_command_test)
print_result(results)