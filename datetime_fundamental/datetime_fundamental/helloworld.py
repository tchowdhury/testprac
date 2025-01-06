import boto3
import json
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return f'Hi, {name}'


def listThing():

    client = boto3.client('iot')

    response = client.list_thing_types(
    thingTypeName = 'thing_type_A'
    )
    return response

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = listThing()
    print(len(x['thingTypes']))
