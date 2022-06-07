from time import sleep
import random
from opcua import Server

# create OPCUA server
server = Server()

# set endpoint for server
endpoint = 'opc.tcp://127.0.0.1:4880'

server.set_endpoint(endpoint)       # assign OPCUA endpoint
server.register_namespace('PLC1')   # register a namespace "PLC1"
objects=server.get_objects_node()   # define an 'objects' folder node

# create a Temperature Sensor node
temperature_sensor = objects.add_object('ns=2;s="TS1"', 'Temperature Sensor 1')
temperature_sensor.add_variable('ns=2;s="TS1_VnedorName"', 'TS1 Vendor Name', 'Contoso Sensor')
temperature_sensor.add_variable('ns=2;s="TS1_SerialNumber"', 'TS1 Serial Number', 987654321)
node_temperature = temperature_sensor.add_variable('ns=2;s="TS1_Temperature"', 'TS1 Temperature', 20)

# create a Pressure Sensor node
pressure_sensor = objects.add_object('ns=2;s="PS1"', 'Pressure Sensor 1')
pressure_sensor.add_variable('ns=2;s="PS1_VnedorName"', 'PS1 Vendor Name', 'Contoso Sensor')
pressure_sensor.add_variable('ns=2;s="PS1_SerialNumber"', 'PS1 Serial Number', 543219876)
node_pressure = pressure_sensor.add_variable('ns=2;s="PS1_Temperature"', 'PS1 Temperature', 18.7)

current_temperature = 20.0  # TODO: Replace with temperature from Sense Hat
current_pressure = 25.5     # TODO: Replace with pressure from Sense Hat

try:
    print('Starting OPCUA Server...')
    server.start()
    print('Server online')

    while True:
        # set Node values for temperature and pressure
        # TODO: replace with Sense Hat temperature and pressure
        current_temperature += random.uniform(-1, 1)
        node_temperature.set_value(current_temperature)
        current_pressure +=  random.uniform(-1, 1)
        node_pressure.set_value(current_pressure)

        print('temp: {t}, press: {p}'.format(t = current_temperature, p = current_pressure))
        sleep(2)
finally:
    server.stop()
    print('Server offline')

