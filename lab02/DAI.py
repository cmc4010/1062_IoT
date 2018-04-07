import time, DAN, requests, random

# ServerIP = '140.113.199.202' #Change to your IoTtalk IP or None for autoSearching
ServerIP = '140.113.199.199' # https://test.iottalk.tw
Reg_addr = None #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control','OneParameter','ThreeParameter']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

printFlag = 0

# Start Device
while True:
    try:
    #Pull data from a device feature called "Dummy_Control"
        value1 = DAN.pull('Dummy_Control') # array

        if value1 != None:
            if value1[0] == 1:
                printFlag = 1
            else:
                printFlag = 0

        if printFlag == 1:
            print (random.randint(1,101)) # between 1 and 100

    #Push data to a device feature called "Dummy_Sensor"
        # value2=random.uniform(1, 10)
        # DAN.push ('Dummy_Sensor', value2)

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
