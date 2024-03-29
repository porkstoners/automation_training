from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_list(task):
    task.run(task=send_commands_from_file, file="show_commands.txt")

results = nr.run(task=show_command_list)
print_result(results)


