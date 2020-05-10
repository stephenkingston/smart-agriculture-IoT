import sys
import ibmiotf.device

organization = "ja8y5r"
deviceType = "commander"
deviceId = "11"
authMethod = "token"
authToken = "g0N)@0Txn91p5ESWeL"


def commandHandler(cmd):
    print("Command received: %s" % cmd.data)

    for key in cmd.data.keys():
        if key == 'waterpump':
            if cmd.data['waterpump'] == 'ON':
                print("Water pump is turned ON")

            elif cmd.data['waterpump'] == 'OFF':
                print("Water pump is turned OFF")

        if key == 'borewell':
            if cmd.data['borewell'] == 'ON':
                print("Bore well pump is turned ON")
            elif cmd.data['borewell'] == 'OFF':
                print("Bore well pump is turned OFF")


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:
    deviceCli.commandCallback = commandHandler
