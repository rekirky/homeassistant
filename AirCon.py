# Desired features
# Turn aircon on/off - done
# Enable zones
# Set zones percentage
#

import requests
import xml.etree.ElementTree as ET
url = "http://192.168.86.56/"

site = "http://192.168.86.56/"
def login():
    url = "http://192.168.86.56/login"
    params = {"password": "password"}
    response = requests.get(url, params=params)


def turn_on_of(state):
    global site
    state = int(state)
    login()
    if state == 0:
        url = f"{site}/temData?airconOnOff=1"
    else:
        url = f"{site}/temData?airconOnOff=0"
    requests.get(url)
    
def get_on_off():
    login()
    url = "http://192.168.86.56/getSystemData"
    response = requests.get(url)
    root = ET.fromstring(response.text)
    aircon_on_off = root.find(".//airconOnOff").text
    return(aircon_on_off)

def get_zone_info(zone=1):
    login()
    print(zone)
    global site
    url = f"{site}getZoneData?zone={zone}"
    print(url)
    response = requests.get(url)
    return(response.text)

def set_zone_info(zone=1,setting=1,percent=100):
    print(zone)
    login()
    global site
    url = f"{site}setZoneData"
    params = {"zone": {zone}, "zoneSetting":{setting}, "zoneuserPercentSetting":{percent}}
    response = requests.get(url, params=params)

def dashboard():
    login()
    if get_on_off() == 0:
        status = "Off"
    else:
        status = "On"
    print(status)

def parse_zone_info(zone):
    raw = get_zone_info(zone)
    print(raw)


def get_zone_on_off(zone):
    global url
    login()
    site = f"{url}getZoneData?zone={zone}"
    response = requests.get(site)
    root = ET.fromstring(response.text)
    zone_on_off = root.find(".//setting").text
    return(zone_on_off)


#dashboard()

#get_on_off()
#parse_zone_info(1)

print(get_zone_info(1))
#print(get_zone_on_off(1))