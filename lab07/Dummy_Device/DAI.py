import time, DAN, requests, random

ServerIP = '140.113.199.202' #Change to your IoTtalk IP or None for autoSearching
Reg_addr=None #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control','OneParameter','ThreeParameter']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

total = 0
count = 0
# pushed = 0

while True:
    try:

        #Push data to a device feature called "Dummy_Sensor"
        value2=time.time()
        DAN.push ('Dummy_Sensor', value2)
        # print("pushed")

        #Pull data from a device feature called "Dummy_Control"
        value1=DAN.pull('Dummy_Control')
        if value1 != None:
            # print(value1[0])
            total += (time.time() - value1[0])
            count += 1;
            if(count == 10):
                print("average: ", total/10)
                count = 0
                total = 0

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(1)
