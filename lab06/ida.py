import random

from dan import NoData

### The register server host, you can use IP or Domain.
host = '140.113.199.198' # test.iottalk.tw

### [OPTIONAL] The register port, default = 9992
# port = 9999

### [OPTIONAL] If not given or None, server will auto-generate.
device_name = 'Cheese1'

### [OPTIONAL] If not given or None, DAN will register using a random UUID.
### Or you can use following code to use MAC address for device_addr.
# from uuid import getnode
# device_addr = "{:012X}".format(getnode())
#device_addr = "aa8e5b58-8a9b-419b-b8d5-72624d61108d"

### [OPTIONAL] If not given or None, this device will be used by anyone.
username = 'user'

### The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'Dum_0316092'

### The input/output device features, please check IoTtalk document.
idf_list = ['Dummy_Sensor']
odf_list = ['Face_Detect']

### Set the push interval, default = 1 (sec)
### Or you can set to 0, and control in your feature input function.
push_interval = 10  # global interval
interval = {
    'Dummy_Sensor': 3,  # assign feature interval
}

def register_callback():
    print('register successfully')

def Dummy_Sensor():
    return random.randint(0, 100)
    # return NoData

def Face_Detect(data):  # data is a list
    # try:
    #     status
    # except NameError:
    #     print("status not defined")
    global status

    if data[2] < 0:
        if(status != 1):
            print("face up")
            status = 1
    else:
        if(status != 2):
            print ("face down")
            status = 2
