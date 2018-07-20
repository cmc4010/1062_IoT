
## Important

- A device can act as input device, output device, or both

## Key words
DA: device app
DAN: device app to network
DAI: device app to IoT
IDA: IoT to device app

## SETUP

1. Install python
2. Install pip
3. Get "requests" python module

I used

`python3 -m pip install requests`

because

`python -m pip install requests`

did not have a matching distribution ( not compatible ? ).

## RUN

`python3 DAI.py`

## Dummy Device (JS)

### Hierarchy

1. jquery
2. csmapi
3. dan
4. dai
5. ida

#### csmapi Doc

csmapi global variables
  ENDPOINT
    server IP

set_endpoint (endpoint)
  get ENDPOINT

get_endpoint ()
  set ENDPOINT

register (mac_addr, profile, callback)
  register your device

deregister (mac_addr, callback)
  deregister your device

pull (mac_addr, odf_name, callback)
  get data from output device

push (mac_addr, idf_name, data, callback)
  send data to input device

#### dan Doc

dan global variables
  RETRY_COUNT
  RETRY_INTERVAL
  POLLING_INTERVAL
  _pull
  _push
  _mac_addr
  _profile
  _registered
  _idf_list
  _odf_list
  _df_list
  _df_selected
  _odf_timestamp
  _suspended
  _ctl_timestamp

init

register

push

deregister

#### dai

#### ida

## Dummy Device v2

### Prerequisite

`pip3 install paho-mqtt`
