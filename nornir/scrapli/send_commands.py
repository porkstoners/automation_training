from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_list(task):
    task.run(task=send_commands, commands=["show ip int br", "show version", "show run"])

results = nr.run(task=show_command_list)
print_result(results)


