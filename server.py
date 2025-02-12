from opcua import Server
from time import sleep
import datetime
import random

# create OPCUA server
server = Server()

endpoint = 'opc.tcp://127.0.0.1:4880'           # set endpoint for server
server.set_endpoint(endpoint)                   # assign OPCUA endpoint
server.register_namespace('OPCUA_MTC_PLC1')     # register a namespace "PLC1"
objects = server.get_objects_node()             # define an 'objects' folder node

# create a Temperature Sensor node
temperature_sensor = objects.add_object('ns=2;s="TS1"', 'Temperature Sensor 1')
temperature_sensor.add_variable('ns=2;s="TS1_VendorName"', 'TS1 Vendor Name', 'Contoso Sensor')
temperature_sensor.add_variable('ns=2;s="TS1_SerialNumber"', 'TS1 Serial Number', 987654321)
node_temperature = temperature_sensor.add_variable('ns=2;s="TS1_Temperature"', 'TS1 Temperature', 20)

# create a Pressure Sensor node
pressure_sensor = objects.add_object('ns=2;s="PS1"', 'Pressure Sensor 1')
pressure_sensor.add_variable('ns=2;s="PS1_VnedorName"', 'PS1 Vendor Name', 'Contoso Sensor')
pressure_sensor.add_variable('ns=2;s="PS1_SerialNumber"', 'PS1 Serial Number', 543219876)
node_pressure = pressure_sensor.add_variable('ns=2;s="PS1_Pressure"', 'PS1 Pressure', 18.7)



temperature = 20.0  # TODO: Replace with temperature from Sense Hat
pressure = 25.5     # TODO: Replace with pressure from Sense Hat
humidity =  8.0     # TODO: Replace with humidity from Sense Hat
magnetometer = 1.0  # TODO: Replace with magnetometer from Sense Hat

try:
    print('Starting OPCUA Server...')
    server.start()
    print('Server online')

    while True:
        # set Node values for temperature and pressure
        # TODO: replace with Sense Hat temperature and pressure
        temperature += random.uniform(-1, 1)
        node_temperature.set_value(temperature)
        pressure +=  random.uniform(-1, 1)
        node_pressure.set_value(pressure)

        print('temp: {t}, press: {p}'.format(t = temperature, p = pressure))
        sleep(1)
finally:
    server.stop()
    print('Server offline')

