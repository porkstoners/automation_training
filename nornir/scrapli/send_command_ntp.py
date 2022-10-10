from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# create a variable for the Init nornir modules and call the location of the config file. 
nr = InitNornir(config_file="/mnt/googledrive/Training/Training/python/cbt_network_automation_python/nornir/config.yaml")

def show_ntp_status(task):
    task.run(task=send_command, command="show run sec ntp")

result = nr.run(task=show_ntp_status)
print_result(result)


