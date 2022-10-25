from pydoc import importfile
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="../config.yaml")
""" This function replaces the running config with a config from the flash drive
    This is useful for rolling back to a well know good configuration.
    - commit good configuration to flash --> run automation changes --> if changes do not work, rollback to the required version - 
"""
def rollin_rollin_rollin(task):
    task.run(task=send_command, command="configure replace flash:ipvzero")

results = nr.run(task=rollin_rollin_rollin)
print_result(results)