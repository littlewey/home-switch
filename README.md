# Setup instruction

> create credntials from template
```
$ cp credential-template.py credential.py
```
> install Phantomjs, for arm deb fetch from [here](https://github.com/fg2it/phantomjs-on-raspberry/releases/)
```
$ sudo dpkg -i Phantomjs*.deb
$ sudo apt -f install
```
> config.json
```
"accessories": [
   {
       "accessory": "Http",
       "name": "客厅暖灯",
       "switchHandling": "realtime",
       "http_method": "GET",
       "on_url":      "http://localhost:5000/homeswitch/controller/4/ON",
       "off_url":     "http://localhost:5000/homeswitch/controller/4/OFF",
       "status_url":  "http://localhost:5000/homeswitch/status/4",
       "status_on": "ON",
       "status_off": "OFF",
       "service": "Light",
       "brightnessHandling": "no",
       "brightness_url":     "",
       "brightnesslvl_url":  "",
       "sendimmediately": "",
       "username" : "",
       "password" : ""
   },
   {
    "accessory": "Http",
    "name": "客厅白灯",
    "switchHandling": "realtime",
    "http_method": "GET",
    "on_url":      "http://localhost:5000/homeswitch/controller/3/ON",
    "off_url":     "http://localhost:5000/homeswitch/controller/3/OFF",
    "status_url":  "http://localhost:5000/homeswitch/status/3",
    "status_on": "ON",
    "status_off": "OFF",
    "service": "Light",
    "brightnessHandling": "no",
    "brightness_url":     "",
    "brightnesslvl_url":  "",
    "sendimmediately": "",
    "username" : "",
    "password" : ""
   },
   {
    "accessory": "Http",
    "name": "餐桌灯",
    "switchHandling": "realtime",
    "http_method": "GET",
    "on_url":      "http://localhost:5000/homeswitch/controller/2/ON",
    "off_url":     "http://localhost:5000/homeswitch/controller/2/OFF",
    "status_url":  "http://localhost:5000/homeswitch/status/2",
    "status_on": "ON",
    "status_off": "OFF",
    "service": "Light",
    "brightnessHandling": "no",
    "brightness_url":     "",
    "brightnesslvl_url":  "",
    "sendimmediately": "",
    "username" : "",
    "password" : ""
   },
   {
    "accessory": "Http",
    "name": "客厅状态更新",
    "switchHandling": "no",
    "http_method": "GET",
    "on_url":      "http://localhost:5000/homeswitch/refresh",
    "off_url":     "http://localhost:5000/homeswitch/refresh",
    "status_url":  "http://localhost:5000/homeswitch/refreshStatus",
    "status_on": "ON",
    "status_off": "OFF",
    "service": "Light",
    "brightnessHandling": "no",
    "brightness_url":     "",
    "brightnesslvl_url":  "",
    "sendimmediately": "",
    "username" : "",
    "password" : ""
   },
]
```
