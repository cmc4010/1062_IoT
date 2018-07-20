import time, DAN, requests, random

ServerIP = '140.113.199.199' # https://test.iottalk.tw
Reg_addr = '0316092' #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='0316092'
DAN.profile['df_list']=['0316092']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

flag = 0 # 1: UP (neg) 2: DOWN (pos)
changeFlag = 0

# Start Device
while True:
    try:
    #Pull data from a device feature called "Dummy_Control"
        value1 = DAN.pull('0316092') # array

        if value1 != None:
            if(value1[0] == 1): #UP
                if flag != 1:
                    changeFlag = 1
                flag = 1
            else:
                if flag != 2:
                    changeFlag = 1
                flag = 2

            if changeFlag == 1:
                if flag == 1:
                    print('face up')
                else:
                    print('face down')

            changeFlag = 0

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
