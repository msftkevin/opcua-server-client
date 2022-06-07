from opcua import Client
from time import sleep

def read_value(node_id):
    client_node = client.get_node(node_id)
    client_node_value = client_node.get_value()
    return(client_node_value)




if __name__ == '__main__':
    client = Client('opc.tcp://127.0.0.1:4880')
    try:
        client.connect()

        node = client.get_node('ns=2;s="TS1_Temperature"')
        print(node)
        while True:
            temperature = node.get_value()
            print(temperature)
            sleep(2)
    finally:
        client.disconnect()