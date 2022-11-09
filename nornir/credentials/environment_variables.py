import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

""" 
This script pulls environment variables from the ~/.zshrc file but it could just as easily call them from the ~/.bashrc folder. 
If the variables are not set the script will fail with a key error like this - [KeyError: 'ARUSERNAME']

If you dont want this to be persisten you can just export echo $ARUSERNAME - this will be cleared upon restart of the terminal 


To check the variables from the cli run 
  echo $ARUSERNAME
  echo $ARPASSWORD 


To check the variables from the file cat the below: 

cat ~/.zshrc | grep arista
export ARUSERNAME=arista
export ARPASSWORD=arista

or 

cat ~/.bashrc | grep arista
export ARUSERNAME=arista
export ARPASSWORD=arista

"""

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["ARUSERNAME"]
nr.inventory.defaults.password = os.environ["ARPASSWORD"]


def credentials_test(task):
    task.run(send_command, command="show ip int br")

results = nr.run(task=credentials_test)
print_result(results)

