from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def update_ospf(task):
    task.run(task=send_configs_from_file, file="router_ospf_config.txt")

results = nr.run(task=update_ospf)
print_result(results)


