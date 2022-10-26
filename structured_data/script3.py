import json
from urllib import response
from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import EOSDriver

""" This script is just using scrapli and does not use Nornir it is just an example that was used to help get texfsm working"""

my_devices = [
    {
        "host": "192.168.86.200",
        "auth_username": "doug",
        "auth_password": "q1w2e3r4",
        "port": 22,
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "192.168.86.201",
        "auth_username": "doug",
        "auth_password": "q1w2e3r4",
        "port": 22,
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "192.168.86.202",
        "auth_username": "doug",
        "auth_password": "q1w2e3r4",
        "port": 22,
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
]

for device in my_devices:
    with EOSDriver(**device) as conn:
        response = conn.send_command("show interfaces")
        structured_result = json.dumps(response.textfsm_parse_output(), indent=2)
        print(structured_result)
        print("\n\n\n")