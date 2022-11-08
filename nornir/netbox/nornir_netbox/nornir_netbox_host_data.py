from nornir import InitNornir
from rich import print as rprint 

nr = InitNornir(
    inventory={
        "plugin":"NetBoxInventory2",
        "options": {
            "nb_url": "http://127.0.0.1:8000",
            "nb_token": "0123456789abcdef0123456789abcdef01234567",
            "ssl_verify": False
        }
    }
)

""" 
Pull a list of all hosts currently in netbox 
"""

leafsw01 = (nr.inventory.hosts["leaf-sw01"].data)

print(f"\n\n ### Print all data for {leafsw01['name']} ### ")
rprint(leafsw01)

print(f"\n\n ### Print the tags for {leafsw01['name']} ###")
rprint(leafsw01["tags"])

print(f"\n\n ### Print the serial for {leafsw01['name']} ###")
rprint(leafsw01["serial"])
