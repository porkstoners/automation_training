from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/mnt/googledrive/Training/Training/python/cbt_network_automation_python/nornir/config.yaml")

command_list = ["show run sec ntp", "show int status", "show lldp neigh"]

def show_command_test(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)

results = nr.run(task=show_command_test)
print_result(results)
