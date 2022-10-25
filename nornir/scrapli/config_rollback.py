from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/opt/Training/python/automation_training/nornir/config.yaml")
""" This function looks at the screen output after a command and responding accordingly.
    In this example when we run the copy run command and it completes successfully we expect 
    to see the command back: "Copy completed successfully". The function will wait untill we 
    receive this or it times out
"""
def commit_flash(task):
    cmds = [("copy run flash:ipvzero2", "Copy completed successfully."), ("\n", f"{task.host}#")]
    task.run(task=send_interactive, interact_events=cmds)

results = nr.run(task=commit_flash)
print_result(results)
