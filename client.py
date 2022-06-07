from opcua import Client
client = Client('opc.tcp://127.0.0.1:4880')

try:
    client.connect()
    while True:
        client.
finally:
    print("Connection closed.")
    client.close()