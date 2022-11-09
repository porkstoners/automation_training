import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password

def credentials_test(task):
    task.run(send_command, command="show ip int br")

results = nr.run(task=credentials_test)
print_result(results)

