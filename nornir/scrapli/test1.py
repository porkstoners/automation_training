from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="/mnt/googledrive/Training/Training/python/cbt_network_automation_python/nornir/config.yaml")

target_list = []

def log_buffer(task):
    result = task.run(task=send_command, command="show ip int br")
    task.host["facts"] = result.scrapli_response.genie_parse_output()
    logging_buffer = task.host["facts"]["logging"]
    for line in logging_buffer:
        if line.startswith("logging"):
            rprint("compliant")
    else:
        rprint("Not compliant")


nr.run(task=log_buffer)

