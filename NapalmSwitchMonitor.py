#python project switch mac table enumeration/report 

from napalm import get_network_driver
import getpass
import json

passwd = getpass.getpass('Please enter the password: ') # Reads the output from the user and save it as a string

driver = get_network_driver('ios')
switch_01 = {
    "hostname": '10.10.20.19', 
    "username": "cisco",
    "password": passwd,
    "optional_args": {"secret": passwd}
    }

switch_01_conn = driver(**switch_01)
switch_01_conn.open()
print(f"Connecting to {switch_01['hostname']}")
output = switch_01_conn.get_mac_address_table() #get mac-address table method
switch_01_conn.close()

output_json = json.dumps(output, indent=4)
print(output_json)
