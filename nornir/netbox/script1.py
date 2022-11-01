from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_list(task):
    task.run(task=send_command, command="show version")

results = nr.run(task=show_command_list)
print_result(results)


