import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

""" 
This uses the GPG encrypted envrionment credentials - the script needs to be launched with: 

env $(gpg --decrypt encrypted.env.gpg) python3 encrypted_variables.py

If the file has not been decrypted already you will be prompted for the passphrase. 
"""

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["DEFAULT_USERNAME"]
nr.inventory.defaults.password = os.environ["DEFAULT_PASSWORD"]


def credentials_test(task):
    task.run(send_command, command="show ip int br")

results = nr.run(task=credentials_test)
print_result(results)

