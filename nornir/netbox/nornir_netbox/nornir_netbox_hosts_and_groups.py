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

all_hosts = (nr.inventory.hosts)

print("Standard print \n")  
print(all_hosts)

print(" \n\n ### Use print from rich module ")
# Use rprint to print clean structured format 
rprint(all_hosts)

print("\n\n Iterate throug the hosts and print")  
for i in all_hosts:
    print(f"Hostname: {i}")


"""
Pull a list of all avaliable groups 
"""

all_groups = (nr.inventory.groups)

print("## Standard print \n ##")  
print(all_groups)

print(" \n\n ### Use print from rich module ###")
# Use rprint to print clean structured format 
rprint(all_groups)

print("\n\n## Iterate through the groups and print ##")  
for i in all_groups:
    print(f"group Name: {i}")