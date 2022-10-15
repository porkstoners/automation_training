
from nornir import InitNornir, init_nornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")

def another_config_test(task):
    task.run(task=netmiko_send_config, config_commands=['router ospf 15', "network 10.0.0.0/24"])


results = nr.run(task=another_config_test)
print_result(results)

