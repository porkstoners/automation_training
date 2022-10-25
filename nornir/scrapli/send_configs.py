from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="../config.yaml")

def update_ospf(task):
    task.run(task=send_configs, configs=["ntp server 123.123.123.123"])

results = nr.run(task=update_ospf)
print_result(results)


