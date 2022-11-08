from nornir import InitNornir
from rich import print as rprint 
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
    inventory={
        "plugin":"NetBoxInventory2",
        "options": {
            "nb_url": "http://127.0.0.1:8000",
            "nb_token": "0123456789abcdef0123456789abcdef01234567",
            "filter_parameters": {
                "name": ["spine-sw-01","spine-sw-02"]
            }
        }
    }
)



def random_task(task):
    task.run(task=send_command, command="show version")

results = nr.run(task=random_task)
print_result(results)


