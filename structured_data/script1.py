from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.functions import print_structured_result



nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    task.run(task=send_command, command="show version")

    

results = nr.run(task=pull_structured_data)
print_structured_result(results)
